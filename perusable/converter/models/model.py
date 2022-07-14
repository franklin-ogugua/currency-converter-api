from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    """
    Schema for handling user registration
    """

    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Franklin Ogugua",
                "email": "franklin@x.com",
                "password": "weakpassword",
            }
        }


class UserLoginSchema(BaseModel):
    """
    Schema for handling user login
    """

    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {"email": "franklin@x.com", "password": "weakpassword"}
        }


class ConversionSchema(BaseModel):
    """
    Schema for handling currency conversion
    """

    base_code: str = Field(...)
    target_code: str = Field(...)
    amount: int = Field(...)

    class Config:
        schema_extra = {
            "example": {"base_code": "EUR", "target_code": "GBP", "amount": 500}
        }


class HistorySchema(BaseModel):
    """
    Schema for handling currency conversion based on historical data
    """

    year: int = Field(...)
    month: int = Field(...)
    day: int = Field(...)
    base_code: str = Field(...)
    target_code: str = Field(...)
    amount: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "year": 2015,
                "month": 2,
                "day": 22,
                "base_code": "EUR",
                "target_code": "GBP",
                "amount": 500,
            }
        }
