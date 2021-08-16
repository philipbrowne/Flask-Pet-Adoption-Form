from models import Pet, db
from app import app
db.drop_all()
db.create_all()

Pet.query.delete()

p1 = Pet(name='Jimmy', species='dog', photo_url='https://images.unsplash.com/photo-1603272743626-df5c7f34c0e9?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1082&q=80',
         age='8', notes='Very good boy!', available=True)
p2 = Pet(name='Steve', species='cat', photo_url='https://images.unsplash.com/photo-1570461121477-846eadb013b6?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1069&q=80',
              age='4', notes='Sweet cat! Very nice!', available=True)
p3 = Pet(name='Charles', species='dog', photo_url='https://images.unsplash.com/photo-1516108282925-3c3c19bc72b2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1100&q=80',
              age='6', notes='Wonderful animal!', available=False)
p4 = Pet(name='Stacy', species='cat', photo_url='https://images.unsplash.com/photo-1564539279948-9931a76c05be?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1100&q=80',
              age='7', notes='Sweetest girl', available=True)
p5 = Pet(name='Marcie', species='dog', photo_url='https://images.unsplash.com/photo-1605358638400-1c6ffa76632d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1100&q=80',
              age='4', notes='Adorable', available=False)

db.session.add_all([p1, p2, p3, p4, p5])
db.session.commit()
