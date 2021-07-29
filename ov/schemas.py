from typing import Optional

from pydantic import BaseModel


class ImageBase(BaseModel):
    name: Optional[str]
    image: Optional[str]


class ImageList(ImageBase):
    id: int

    class Config:
        orm_mode = True


