import base64

from fastapi import FastAPI
from dotenv import load_dotenv

from ov.schemas import ImageBase64

load_dotenv()
app = FastAPI()


@app.get('/get_last_images')
async def get_last_images():
    return {"messages": "Hello world"}


@app.post('/negative_image/')
async def post_negative_image(image64: ImageBase64):
    ...
    return {}
