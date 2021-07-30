import base64

from fastapi import APIRouter, Request
from fastapi import Depends
from sqlalchemy.orm import Session

from .schemas import ImageBase
from core.utils import get_db
from . import service
from .templates import templates

router = APIRouter()


@router.get('/get_last_images')
async def last_images(request: Request, db: Session = Depends(get_db)):
    images = service.get_last_images(db)
    prefix = 'data:image/{};base64,'
    for image in images:
        with open(image.image, mode='rb') as img:
            ext = image.image.split('.')[-1]
            image.image = prefix.format(ext) + base64.b64encode(img.read()).decode('utf-8')
    return templates.TemplateResponse("images.html", {"request": request, "images": images})


@router.post('/negative_image/')
async def post_negative_image(image: ImageBase):
    image64 = image.image
    name = image.name
    return {}
