import sys

#importing classes from sqlalchemy module
from sqlalchemy import Column, ForeignKey, Integer, String

#delcaritive_base , used in the configuration
# and class code, used when writing mapper
from sqlalchemy.ext.declarative import declarative_base

#relationship in order to create foreign key relationship
#used when writing the mapper
from sqlalchemy.orm import relationship

#create_engine to used in the configuration code at the
#end of the file
from sqlalchemy import create_engine

#this object will help set up when writing the class code
Base = declarative_base()


class User(Base):
	"""this is the users table in orer to implement
	local permission within the application preventing
	users from modifying other users data
	"""
	__tablename__ = "user"

	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)
	email = Column(String(50), nullable=False)
	picture = Column(String(250))


class University(Base):
	"""
	this class corresponds to the university table
	in the database to be created

	table representation for university which is in the
	database
	"""

	__tablename__ = "university"

	#column definitions for the university table
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	city = Column(String(80), nullable=False)
	user_id = Column(Integer, ForeignKey("user.id"))
	user = relationship(User)

	@property
	def serialize(self):
		#Returns object data in easilty serializable format
		return{
			"name": self.name,
			"city": self.city,
			"id": self.id,
		}


class Room(Base):
	"""
	this class corresponds to the table representation
	of room which is in the database
	"""

	__tablename__ = "room"

	#column definitions for the room table
	owner_name = Column(String(90), nullable=False)
	id = Column(Integer, primary_key=True)
	size = Column(String(60))
	description = Column(String(250))
	price = Column(String(10))
	address = Column(String(250))
	owner_number = Column(String(15))
	university_id = Column(Integer, ForeignKey("university.id"))
	university = relationship(University)
	user_id = Column(Integer, ForeignKey("user.id"))
	user = relationship(User)

	@property
	def serialize(self):
		#Returns object data in easilty serializable format
		return{
			"owner_name": self.owner_name,
			"size": self.size,
			"description": self.description,
			"price": self.price,
			"address": self.address,
			"owner_number": self.owner_number,
			"id": self.id
		}


#create an instance of create_engine class
#and point to the database to be used
engine = create_engine("sqlite:///gotroomwithusers.db")

#goes into the database and adds our new tables
Base.metadata.create_all(engine)

