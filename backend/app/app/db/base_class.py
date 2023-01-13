from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative
class Base:
    id: Any
    __tablename__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__lower__()
