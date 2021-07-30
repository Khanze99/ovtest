from sqlalchemy import Column, ForeignKey, String, Integer, MetaData, Table, Text
from sqlalchemy.orm import relationship, backref

from core.database import Base


class Image(Base):
    __tablename__ = "image"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(Text)
    image = Column(String)

    def __repr__(self):
        return f"Image: {self.name}"


class NegativeImage(Base):
    __tablename__ = "negative_image"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(Text)
    negative_image = Column(String)
    image_id = Column(Integer, ForeignKey("image.id"))
    image = relationship("Image", backref=backref("original_image", uselist=False))

    def __repr__(self):
        return f"Negative image: {self.name}"
