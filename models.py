from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = "sqlite:///blood_donation.db"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    Base.metadata.create_all(engine)

class Donor(Base):
    __tablename__ = 'donors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    contact_info = Column(String, nullable=False)
    blood_type = Column(String, nullable=False)
    last_donation_date = Column(Date, nullable=True)

    donations = relationship('Donation', back_populates='donor')

class Donation(Base):
    __tablename__ = 'donations'

    id = Column(Integer, primary_key=True)
    donor_id = Column(Integer, ForeignKey('donors.id'))
    donation_date = Column(Date, nullable=False)
    quantity_ml = Column(Integer, nullable=False)

    donor = relationship('Donor', back_populates='donations')

class BloodStock(Base):
    __tablename__ = 'blood_stock'

    blood_type = Column(String, primary_key=True)
    quantity_ml = Column(Integer, nullable=False)
    last_updated = Column(Date, nullable=False)
