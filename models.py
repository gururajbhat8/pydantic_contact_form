from pydantic import BaseModel, EmailStr, Field, validator

class Contact(BaseModel):
    name: str = Field(min_length=10)
    email: EmailStr
    age : int = Field(gt=0, lt=80)
    phone_number: str

    @validator('phone_number')
    def valid_phone_number(cls, v):
        if len(v) != 10 or not v.isdigit():
            raise ValueError("Phone Number must be a 10 digit number")
        return v