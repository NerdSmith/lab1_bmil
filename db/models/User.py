from sqlalchemy import Column, String, MetaData
from sqlalchemy.orm import session

from db.db_engine import engine
from db.models.base import Base


class User(Base):
    __tablename__ = "user"
    name = Column(String, primary_key=True)
    password = Column(String)



if __name__ == '__main__':
    metadata_obj = MetaData(bind=engine)
    metadata_obj.create_all()