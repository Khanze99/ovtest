from sqlalchemy import Column, String, Integer, Text

from core.database import Base


class Image(Base):
    __tablename__ = "ovision_image"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(Text)
    image = Column(String)
    negative_image = Column(String)

    def __repr__(self):
        return f"Image: {self.name}"
