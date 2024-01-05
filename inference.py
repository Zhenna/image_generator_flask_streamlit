from typing import Literal
from diffusers import StableDiffusionPipeline
import torch
import time


seed = 2024
generator = torch.manual_seed(seed)

NUM_ITERS_TO_RUN = 1
NUM_INFERENCE_STEPS = 25
NUM_IMAGES_PER_PROMPT = 1


def text2image(
    prompt: str,
    repo_id: Literal[
        "dreamlike-art/dreamlike-photoreal-2.0",
        "hakurei/waifu-diffusion",
        "prompthero/openjourney",
        "stabilityai/stable-diffusion-2-1",
        "runwayml/stable-diffusion-v1-5",
        "nota-ai/bk-sdm-small",
        "CompVis/stable-diffusion-v1-4",
    ],
):
    start = time.time()

    if torch.cuda.is_available():
        print("Using GPU")
        pipeline = StableDiffusionPipeline.from_pretrained(
            repo_id,
            torch_dtype=torch.float16,
            use_safetensors=True,
        ).to("cuda")
    else:
        print("Using CPU")
        pipeline = StableDiffusionPipeline.from_pretrained(
            repo_id,
            torch_dtype=torch.float32,
            use_safetensors=True,
        )

    for _ in range(NUM_ITERS_TO_RUN):
        images = pipeline(
            prompt,
            num_inference_steps=NUM_INFERENCE_STEPS,
            generator=generator,
            num_images_per_prompt=NUM_IMAGES_PER_PROMPT,
        ).images
    end = time.time()

    return images[0], start, end
