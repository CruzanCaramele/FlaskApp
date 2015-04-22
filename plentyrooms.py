from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Base, University, Room, User
 
engine = create_engine("sqlite:///gotroomwithusers.db")
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


#Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com", picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

#Menu for UrbanBurger
university1 = University(user_id=1, name = "Multimedia University", city = "Cyberjaya")

session.add(university1)
session.commit()

room2 = Room(user_id=1, owner_name = "Michelle Obama", description = "Master Room with attached bathroom and aircon", price = "$750.50", address = "Domain Villa , Jalan Technocrat", owner_number = "+60123445234", university = university1, \
	picture="")

session.add(room2)
session.commit()


room1 = Room(user_id=1, owner_name = "Mitt Romney", description = "Master Room with attached bathroom and bath-tub and aircon", price = "$850.50", address = "Cyberria Condo , Jalan Technocrat", owner_number = "+60103805234", university = university1, \
	picture="")

session.add(room1)
session.commit()


#Menu for Super Stir Fry
university2 = University(user_id=1, name = "Segi College", city = "Petaling Jaya")

session.add(university2)
session.commit()


room1 = Room(user_id=1, owner_name = "Hilary Clinton", description = "Middle Room with attached bathroom and bath-tub and aircon", price = "$450.50", address = "Cyberria Condo , Jalan Persiaran MMU", owner_number = "+60103805333", university = university2, \
	picture="")

session.add(room1)
session.commit()

room2 = Room(user_id=1, owner_name = "Dick Chaney", description = "Small Room with  aircon", price = "$250.50", address = "Cyberria Condo , Jalan Technocrat2", owner_number = "+60189765234", university = university2, picture="")

session.add(room2)
session.commit()

