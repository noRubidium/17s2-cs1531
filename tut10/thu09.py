"""
- Sequence diagram for next iteration
- ORM
"""

# import sqlite3
# conn = sqlite3.connect('data.db')
#
# c = conn.cursor()
# c.execute(''' CREATE TABLE person (
#     id INTEGER PRIMARY KEY ASC,
#     name varchar(500) NOT NULL
#     )''')
#
# c.execute(''' CREATE TABLE address (
#     id INTEGER PRIMARY KEY ASC,
#     full_address varchar(500) NOT NULL,
#     person_id INTEGER NOT NULL,
#     FOREIGN KEY(person_id) REFERENCES person(id)
#     )''')
#
# c.execute('''INSERT INTO person VALUES(1, 'Minjie')''')
# c.execute('''INSERT INTO address VALUES(1, 'UNSW', 1)''')
# conn.commit()
# conn.close()

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///alchemy.db')
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=False)


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    full_address = Column(String(500), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)


try:
    Base.metadata.create_all(engine)
except:
    print('Table already there.')

# insert record
DBSession = sessionmaker(bind=engine)
session = DBSession()

new_person = Person(name='Minjie')
session.add(new_person)

new_address = Address(full_address='UNSW', person=new_person)
session.add(new_address)
session.commit()

new_person = Person(name='Aarthi')
session.add(new_person)

new_address = Address(full_address='1001 UNSW', person=new_person)
session.add(new_address)
session.commit()

## Query

person = session.query(Person).first()
print(person.name)
addrs = session.query(Address).filter(Address.person == person).all()

for addr in addrs:
    print(addr.full_address)
