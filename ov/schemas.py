from typing import Optional

from pydantic import BaseModel


class ImageBase(BaseModel):
    image: Optional[str]


class ImageList(ImageBase):
    id: int
    name: Optional[str]
    negative_image: Optional[str]

    class Config:
        orm_mode = True
