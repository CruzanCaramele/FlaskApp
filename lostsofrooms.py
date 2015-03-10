from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import University, Base, Room
 
engine = create_engine('sqlite:///gotroom.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


#Rooms for MultimediaUniversity
university1 = University(name="Multimedia University", city="Cyber Jaya")
session.add(university1)
session.commit()

vacantRoom1 = Room(owner_name = "Michelle Obama", size = "320sqft", description = "Fully Furnished middle room", price = "RM500/month", address = "Block C Cyberia Condo", owner_number = "+60127672290", university=university1)
session.add(vacantRoom1)
session.commit()

#Rooms for University Putra Malaysia
university2 = University(name="Putra Malaysia", city="Serdang")
session.add(university2)
session.commit()

vacantRoom2 = Room(owner_name = "Joe Biden", size = "480sqft", description = "Fully Furnished Master room", price = "RM800/month", address = "Block A South City Condo", owner_number = "+61123472390", university=university2)
session.add(vacantRoom2)
session.commit()


#Rooms for UCSI
university3 = University(name="Sedaya College", city="Cheras")
session.add(university3)
session.commit()

vacantRoom3 = Room(owner_name = "Hilary Clinton", size = "390sqft", description = "Fully Furnished middle room with toilet", price = "RM900/month", address = "Block B Angkasa Condo", owner_number = "+60187679990", university=university3)
session.add(vacantRoom3)
session.commit()


#Rooms for Limkokwing University
university4 = University(name="Limkokwing University", city="Kuala Lumpur")
session.add(university4)
session.commit()

vacantRoom4 = Room(owner_name = "Mitt Romney", size = "220sqft", description = "Small room with air con", price = "RM350/month", address = "Block F Domain Condo", owner_number = "+60127670010", university=university4)
session.add(vacantRoom4)
session.commit()

print "added menu items!"
