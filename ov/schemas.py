from typing import Optional

from pydantic import BaseModel


class ImageBase(BaseModel):
    image: Optional[str]
    name: Optional[str]

    class Config:
        orm_mode = True


class Image(ImageBase):
    id: int
    negative_image: Optional[str]


class ImageCreate(ImageBase):
    negative_image: Optional[str]
