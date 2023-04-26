from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///tempp.db', echo=True)
Base = declarative_base()

class MyTable(Base):
    __tablename__ = 'Complaint'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    complaint = Column(String)

Base.metadata.create_all(engine)
