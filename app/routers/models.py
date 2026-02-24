from pydantic import BaseModel

class LoginSchema(BaseModel):
    username: str
    password: str


class SignupSchema(BaseModel):
    username: str
    password: str
    confirm_password: str