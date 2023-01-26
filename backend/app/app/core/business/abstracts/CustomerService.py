import sys
import os
from dotenv import load_dotenv
load_dotenv()
path = os.environ["FILE_PATH"]
sys.path.append(path)


from sqlalchemy.orm import Session
from app.app.schemas.customer import CustomerCreate
from app.app.db.get_db import get_db
from app.app.repository.customerRepository import CustomerRepository
from app.app.models.customer import Customer
from typing import Optional
from fastapi import Depends


class CustomerService:
    def __init__(self, customerRepository: CustomerRepository):
        self.customerRepository = customerRepository

    def create(self, db: Session = Depends(get_db), *, customer: CustomerCreate) -> Customer:
        self.customerRepository.save(db, customer=customer)
        return customer

    def getCustomerByName(self, db: Session = Depends(get_db), *, name: str) -> Optional[Customer]:
        customer = self.customerRepository.getByName(db, name=name)
        return customer
