from model import Base, Rating

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(picture_path,name,price):
	product_object = Product(
		picture_path=picture_path,
		name = name,
		price = price)
	session.add(product_object)
	session.commit()