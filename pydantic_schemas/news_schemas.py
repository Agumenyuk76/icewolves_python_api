from typing import List

from pydantic import BaseModel, HttpUrl

class NewsList(BaseModel):
    id: int
    title: str
    message: str
    photo: str
    added_at: str
    photos: List[HttpUrl]

class GetNewsSchema(BaseModel):
    news: List[NewsList]