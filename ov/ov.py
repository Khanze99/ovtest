from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session

from .schemas import ImageBase, ImageCreate
from core.utils import get_db
from . import service
from .templates import templates
from .service import (
    image2base64, base64_2_image,
    create_image_db, create_negative_image
)
from .config import settings

router = APIRouter()


@router.get('/get_last_images')
async def last_images(db: Session = Depends(get_db)):
    images = service.get_last_images(db)
    for image in images:
        image.image = image2base64(img_path=settings.ORIGINAL_IMAGE_URL + image.image)
        image.negative_image = image2base64(img_path=settings.NEGATIVE_IMAGE_URL + image.negative_image)
    return {'images': images}


@router.post('/negative_image/')
async def post_negative_image(image: ImageBase, db: Session = Depends(get_db)):
    if not image.name or not image.image:
        raise HTTPException(status_code=400, detail="send name and image base64 encode")
    image64 = image.image
    image_filename = base64_2_image(image64)
    negative_image = create_negative_image(image_filename)
    cr_img = ImageCreate(**{'name': image.name, 'image': image_filename, 'negative_image': negative_image})
    saved_image = create_image_db(db, cr_img)
    return {"negative_image": image2base64(settings.NEGATIVE_IMAGE_URL + saved_image.negative_image)}
