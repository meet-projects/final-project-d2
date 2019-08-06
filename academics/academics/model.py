from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Product(Base):
	__tablename__ = 'rating'
	product_id = Column(Integer, primary_key=True)
	picture_path = Column(String)
	name = Column(String)
	price = Column(Integer)

class Picture(Base):
	__tablename__ = 'picture'
	picture_id = Column(Integer, primary_key=True)
	path = Column(String)