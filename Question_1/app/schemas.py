from pydantic import BaseModel


class PostBase(BaseModel):
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(BaseModel):
    content: str
    published: bool = True

    class Config:
        from_orm = True
