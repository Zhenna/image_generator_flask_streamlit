# image_generator_flask_streamlit

Repo structure
```
├── static
│   └── (generated images)
├── templates
│   ├── index_response.html
│   └── index.html
├── .gitignore
├── app.py
├── streamlit_app.py
├── inference.py
├── requirements.txt
└── README.md

```

## How to use

1. Install dependencies
```shell
pip install -r requirements.txt
```

2. Run the Flask app and paste the local host url in your browser
```
flask run
```

3. Run the Streamlit app and paste the local host url in your browser
```
streamlit run streamlit_app.py
```