from sqlalchemy import Column, Integer, String, Text, Boolean, Numeric, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    points = Column(Integer, default=0)
    created_at = Column(TIMESTAMP)

    addresses = relationship("Address", back_populates="user")

class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    address = Column(Text, nullable=False)
    is_default = Column(Boolean, default=False)
    
    user = relationship("User", back_populates="addresses")

class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)

class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)
    image_url = Column(Text)
    category = Column(String)

class MenuAvailability(Base):
    __tablename__ = "menu_availability"
    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"))
    is_available = Column(Boolean, default=True)