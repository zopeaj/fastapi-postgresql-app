from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class CustomerBase(BaseModel):
    name: Optional[str] = None
    phonenumber: Optional[str] = None


# Properties to receive via API on creation
class CustomerCreate(CustomerBase):
    name: str = None
    phonenumber: str = None



# Properties to receive via API on update
class CustomerUpdate(CustomerBase):
    phonenumber: Optional[str] = None


class CustomerInDBBase(CustomerBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Customer(CustomerInDBBase):
    pass


# Additional properties stored in DB
class CustomerInDB(CustomerInDBBase):
    phonenumber: str
