from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()

class Cocktail(Base):
    __tablename__ = 'cocktails'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    ingredients = Column(String(500), nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(50))
    created_at = Column(DateTime, default=datetime.now)
    
    orders = relationship('Order', back_populates='cocktail')
    
    def __repr__(self):
        return f"<Cocktail(name='{self.name}', price={self.price})>"

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(20))
    favorite_drink = Column(String(100))
    created_at = Column(DateTime, default=datetime.now)
    
    orders = relationship('Order', back_populates='customer')
    
    def __repr__(self):
        return f"<Customer(name='{self.name}', email='{self.email}')>"

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    cocktail_id = Column(Integer, ForeignKey('cocktails.id'))
    quantity = Column(Integer, default=1)
    order_date = Column(DateTime, default=datetime.now)
    status = Column(String(20), default='pending')
    
    customer = relationship('Customer', back_populates='orders')
    cocktail = relationship('Cocktail', back_populates='orders')
    
    def __repr__(self):
        return f"<Order(customer='{self.customer.name}', cocktail='{self.cocktail.name}', quantity={self.quantity})>"

# Database configuration
engine = create_engine('sqlite:///maji_mazuri.db')
Session = sessionmaker(bind=engine)

def init_db():
    """Initialize the database"""
    Base.metadata.create_all(engine)