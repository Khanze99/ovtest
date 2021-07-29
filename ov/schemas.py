from typing import Optional

from pydantic import BaseModel


class ImageBase(BaseModel):

    name: Optional[str]
    image: Optional[str]


class Image(ImageBase):
    id: int

    class Config:
        orm_mode = True


class ImageCreate(ImageBase):
    pass


class ImageBase64(BaseModel):
    image: Optional[str]