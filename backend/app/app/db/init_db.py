import sys
import os
from dotenv import load_dotenv
load_dotenv()
path = os.environ["FILE_PATH"]
sys.path.append(path)

from app.app.db.session import SessionLocal
from sqlalchemy.orm import Session
from app.app.repository.customerRepository import CustomerRepository
from app.app.core.business.abstracts.customerService import CustomerService
from app.app.config.settings import Settings
from app.app.schemas.customer import CustomerCreate


customerService = CustomerService(CustomerRepository())

def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)
    customer = customerService.getCustomerByName(db, name=Settings.FIRST_CUSTOMER)
    if not customer:
        customer_in = CustomerCreate(
            name=Settings.FIRST_CUSTOMER,
            phonenumber=Settings.FIRST_CUSTOMER_PHONENUMBER,
        )
        customer = customerService.create(db, customer=customer_in)  # noqa: F841
        print(customer)
