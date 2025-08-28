from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    
    contacts = relationship("Contact", back_populates="group")
    
    def __repr__(self):
        return f"<Group(name='{self.name}')>"

class Contact(Base):
    __tablename__ = 'contacts'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String)
    email = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    
    group = relationship("Group", back_populates="contacts")
    address = relationship("Address", back_populates="contact", uselist=False)
    
    def __repr__(self):
        return f"<Contact(name='{self.name}', phone='{self.phone}', email='{self.email}')>"

class Address(Base):
    __tablename__ = 'addresses'
    
    id = Column(Integer, primary_key=True)
    street = Column(String)
    city = Column(String)
    zip_code = Column(String)
    contact_id = Column(Integer, ForeignKey('contacts.id'))
    
    contact = relationship("Contact", back_populates="address")
    
    def __repr__(self):
        return f"<Address(street='{self.street}', city='{self.city}', zip='{self.zip_code}')>"

# Database setup
engine = create_engine('sqlite:///contacts.db')
Session = sessionmaker(bind=engine)