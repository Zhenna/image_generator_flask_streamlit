from flask import Flask, request, render_template, flash, send_file
from inference import text2image

app = Flask(__name__)
app.secret_key = "super secret key"
# RuntimeError: The session is unavailable because no secret key was set.

# os.mkdir("static")
IMAGE_PATH = "static/image.jpg"


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/loading", methods=["GET", "POST"])
def show_loader():
    return render_template("loading.html")


@app.route("/download")
def download_img():
    return send_file(IMAGE_PATH, as_attachment=True)
    # send_from_directory(directory="static", filename="image.jpg")


@app.route("/index_response", methods=["GET", "POST"])
def generate_image():
    user_input = request.form.get("user_input")
    model = request.form.get("models")

    im, start, end = text2image(prompt=user_input, repo_id=model)
    im.save(IMAGE_PATH)

    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)

    msg = "Prcoessing time: {:0>2}:{:0>2}:{:05.2f}.".format(
        int(hours), int(minutes), seconds
    )
    flash(
        msg,
        category="success",
    )

    return render_template(
        "index_response.html",
        image_url=IMAGE_PATH,
    )
