import base64

from fastapi import APIRouter, Request
from fastapi import Depends
from sqlalchemy.orm import Session

from .schemas import ImageBase
from core.utils import get_db
from . import service
from .templates import templates
from .service import image2base64, base64_2_image

router = APIRouter()


@router.get('/get_last_images')
async def last_images(request: Request, db: Session = Depends(get_db)):
    images = service.get_last_images(db)
    for image in images:
        image.image = image2base64(img_path=image.image)
    return templates.TemplateResponse("images.html", {"request": request, "images": images})


@router.post('/negative_image/')
async def post_negative_image(image: ImageBase):
    image64 = image.image
    image = base64_2_image(image64)
    print(image)
    return {}
