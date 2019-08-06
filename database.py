from model import Base, Product,Picture

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

def delete_by_id(product_id):
	session.query(Product).filter_by(product_id=product_id).delete()
	session.commit()
	
engine = create_engine('sqlite:///pictures.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_pic(path):
	picture = Picture(
		path=path)
	session.add(picture)
	session.commit()

def delete_pic_by_id(picture_id):
	session.query(Picture).filter_by(picture_id=picture_id).delete()
	session.commit()

def query_pic_by_id(picture_id):
    picture = session.query(Picture).filter_by(
        picture_id=picture_id).first()
    return picture

