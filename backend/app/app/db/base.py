import sys
import os
from dotenv import load_dotenv
load_dotenv()
path = os.environ["FILE_PATH"]
sys.path.append(path)

from app.app.db.base_class import Base
from app.app.models.address import Address
from app.app.models.booking import Booking
from app.app.models.customer import Customer
from app.app.db.session import engine


