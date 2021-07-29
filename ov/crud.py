from sqlalchemy.orm import Session

from ov import models, schemas


def get_last_images(db: Session):
    return db.query(models.Image).limit(3)


def create_image(db: Session, image: schemas.ImageCreate):
    db_image = models.Image(**image.dict())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image
