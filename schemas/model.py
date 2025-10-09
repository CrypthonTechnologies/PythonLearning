from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

    class Config:
        from_attributes = True


class CreateUser(BaseModel):
    username: str
    password: str


class User(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        from_attributes = True

class Post(BaseModel):
    post_id: int 
    title: str
    description: str

class Token(BaseModel):
    access_token: str
    token_type: str
