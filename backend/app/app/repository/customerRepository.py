import sys
import os
from dotenv import load_dotenv
load_dotenv()
path = os.environ["FILE_PATH"]
sys.path.append(path)

from app.app.schemas.customer import CustomerCreate
from app.app.db.base import Customer
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from app.app.db.get_db import get_db
from fastapi import Depends
from typing import Optional, List

class CustomerRepository:
    def save(self, db: Session = Depends(get_db), *, customer: CustomerCreate) -> Customer:
        customer_db = Customer(name=customer.name, phonenumber=customer.phonenumber)
        # print(customer_db)
        db.add(customer_db)
        db.commit()
        db.refresh(customer_db)
        return customer_db

    def getByName(self, db: Session, *, name: str) -> Optional[Customer]:
        customer = db.query(Customer).filter(Customer.name == name).first()
        return customer
