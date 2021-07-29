from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from .schemas import ImageBase
from core.utils import get_db
from . import service

router = APIRouter()


@router.get('/get_last_images')
async def last_images(db: Session = Depends(get_db)):
    images = service.get_last_images(db)
    return images


@router.post('/negative_image/')
async def post_negative_image(image: ImageBase):
    image64 = image.image
    name = image.name
    return {}
