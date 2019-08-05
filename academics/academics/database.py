from model import Base, Product

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///products.db?check_same_thread=False')
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

def query_by_id(product_id):
    product = session.query(Product).filter_by(
        product_id=product_id).first()
    return product
