from sqlalchemy import func
from sqlalchemy.orm import Session

from db.db_engine import engine
from db.models.User import User, BioVector


class UserRepository:
    def __init__(self):
        pass

    @staticmethod
    def get_engine():
        return engine

    def add_user(self, user: User):
        with Session(self.get_engine()) as session:
            session.add(user)
            session.commit()

    def get_user_by_name(self, name):
        with Session(self.get_engine()) as session:
            return session.query(User).filter_by(name=name).first()

    def add_bio_to_user(self, username, bio):
        with Session(self.get_engine()) as session:
            user = session.query(User).filter_by(name=username).first()
            user.biovectors.append(bio)
            session.add(bio)
            session.commit()

    def get_non_unique(self):
        with Session(self.get_engine()) as session:
            non_unique_users_sub = (
                session.query(User.password)
                .group_by(User.password)
                .having(func.count(User.password) > 1)
                .all()
            )

            non_unique_users = (
                session.query(User)
                .filter(User.password.in_(*non_unique_users_sub))
                .all()
            )
            return non_unique_users

    def find_user(self, username, password):
        with Session(self.get_engine()) as session:
            return session.query(User).filter_by(name=username, password=password).first()

    def get_vectors_of_user(self, u):
        with Session(self.get_engine()) as session:
            return session.query(BioVector).filter_by(user_id=u.id).all()

    def post_prompt(self, p):
        with Session(self.get_engine()) as session:
            session.add(p)
            session.commit()
