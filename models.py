from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#setup the base (parent) class
Base = declarative_base()



#setup the donors table
class Donor(Base):

    __tablename__='donors'

    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name',String, nullable=True)
    last_name = Column('last_name', String)
    age = Column('age', Integer, default=18)
    email = Column('email', String, nullable=False, unique=True)

    def __repr__(self):
        return f"Name: {self.first_name} {self.last_name} - [{self.age} years] | Email: {self.email}\n"



#create database
engine = create_engine('sqlite:///example.db')


#create a metadata
Base.metadata.create_all(bind=engine)

#create a session
Session = sessionmaker(bind=engine)
session = Session()
