import base64
import uuid
import re
from typing import Optional
from PIL import Image, ImageOps

from sqlalchemy.orm import Session

from .models import Image as ImageModel
from .config import settings
from .schemas import ImageCreate


def get_last_images(db: Session):
    return db.query(ImageModel).order_by(ImageModel.id.desc()).limit(3).all()


def create_image_db(db: Session, image: ImageCreate):
    image = ImageModel(**image.dict())
    db.add(image)
    db.commit()
    db.refresh(image)

    return image


def image2base64(img_path: Optional[str]):
    """
    decode image to base64
    :param img_path: str
    :return: image64: str
    """

    prefix = 'data:image/{};base64,'
    ext = img_path.split('.')[-1]
    with open(img_path, mode='rb') as img:
        image64 = prefix.format(ext) + base64.b64encode(img.read()).decode('utf-8')

    return image64


def base64_2_image(image64: Optional[str]):
    """

    :param image64: str
    :return: img_path: str
    """
    pattern = r'(jpeg|png)'
    header, encoded = image64.split(',', 1)
    name = str(uuid.uuid4())
    img_format = re.findall(pattern, header)
    filename = name + '.' + img_format[0]
    img_decode = base64.b64decode(encoded)

    with open(settings.ORIGINAL_IMAGE_URL + filename, mode="wb") as file:
        file.write(img_decode)

    return filename


def create_negative_image(image: Optional[str]):
    """

    :param image: str filename
    :return: negative_mage: str filename
    """
    invert_filename = f'negative_{image}'
    img = Image.open(settings.ORIGINAL_IMAGE_URL + image)
    img_invert = ImageOps.invert(img)
    img_invert.save(settings.NEGATIVE_IMAGE_URL + invert_filename)

    return invert_filename
