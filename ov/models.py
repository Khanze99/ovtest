from sqlalchemy import Column, ForeignKey, String, Integer, MetaData, Table, Text
from sqlalchemy.orm import relationship, backref

from core.database import Base


class Image(Base):
    __tablename__ = "image"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(Text)
    image = Column(String)


class NegativeImage(Base):
    __tablename__ = "negative_image"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(Text)
    negative_image = Column(String)
    image_id = Column(Integer, ForeignKey("image.id"))
    image = relationship("Image", backref=backref("image", uselist=False))

