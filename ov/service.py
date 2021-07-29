from sqlalchemy.orm import Session

from .models import Image


def get_last_images(db: Session):
    return db.query(Image).order_by(Image.id.desc()).limit(3).all()