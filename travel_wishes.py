
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table


Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    username = Column(String, primary_key=True)
    password = Column(String(80))
    fullname = Column(String(50))
    email = Column(String(100))


class Locations(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    state = Column(String)
    city = Column(String)
    website = Column(String)


class Wishes(Base):
    __tablename__ = 'wishes'

    user = Column(String, ForeignKey('users.username'), primary_key=True)
    location = Column(Integer, ForeignKey('locations.id'), primary_key=True)
    location_name = relationship("Locations", backref=backref('wishes'))
    username = relationship("Users", backref=backref('wishes'))


engine = create_engine('sqlite:///travel_wishes.db')

Base.metadata.create_all(engine)