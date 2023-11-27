from sqlalchemy import Column, String, MetaData, Float, Integer, ForeignKey
from sqlalchemy.orm import session, declarative_base, relationship

from db.db_engine import engine
from db.models.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, nullable=False)
    password = Column(String, nullable=False)

    biovectors = relationship('BioVector', back_populates='user')
    prompts = relationship("Prompt", back_populates='user')


class BioVector(Base):
    __tablename__ = "biovector"

    id = Column(Integer, primary_key=True, autoincrement=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    input_time = Column(String, nullable=False)
    hold_time = Column(String, nullable=False)

    user = relationship('User', back_populates='biovectors')


class Prompt(Base):
    __tablename__ = "prompt"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='prompts')

    data = Column(String, nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
