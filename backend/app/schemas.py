from typing import Optional
from pydantic import BaseModel, Field

class BookBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=200)
    author: str = Field(..., min_length=2, max_length=100)

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=2, max_length=200)
    author: Optional[str] = Field(None, min_length=2, max_length=100)
    available: Optional[bool] = Field(None)

class BookResponse(BookBase):
    id: int
    available: bool
    class Config:
        from_attributes = True