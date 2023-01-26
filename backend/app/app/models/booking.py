import sys
import os
from dotenv import load_dotenv
load_dotenv()
path = os.environ["FILE_PATH"]
sys.path.append(path)

from app.app.db.base_class import Base
from sqlalchemy import Column, String, Integer, Sequence


class Booking(Base):
    id = Column(Integer, Sequence("booking_seq_id"), primary_key=True)
