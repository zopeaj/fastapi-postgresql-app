import sys
import os
from dotenv import load_dotenv
load_dotenv()
path = os.environ["FILE_PATH"]
sys.path.append(path)

from app.app.db.base_class import Base
from sqlalchemy import Integer, Sequence, Column, String


class Customer(Base):
    id = Column(Integer, Sequence('address_seq_id'), primary_key=True)
    name = Column(String(50), nullable=False)
    phonenumber = Column(String(15), nullable=False)

    def __repr__(self):
        return "<User(name='%s', phonenumber='%s')>"  % (self.name, self.phonenumber)

print(Customer(name="Hello", phonenumber="080223901852"))

