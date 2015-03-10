from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

#import module for ORM
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, University, Room


#create connection to database
engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind=engine
DBSession = sessionmaker(bind=engine)
session=DBSession()


#create an instance of Flask class with the name
#of the runnung application as the argument
app = Flask(__name__)


@app.route("/")
@app.route("/university/")
def showUniversities():
	return "This page shows all the universities and their cities"


@app.route("/university/new/")
def newUniversity():
	return "This page will be for adding new Universities"


@app.route("/university/<int:university_id>/edit/")
def editUniversity(university_id):
	return "This page will be for editing a university %s" % university_id


@app.route("/university/<int:university_id>/delete/")
def deleteUniversity(university_id):
	return "This page will be for deleting a university %s" % university_id


@app.route("/university/<int:university_id>/")
@app.route("/university/<int:university_id>/rooms/")
def showRooms(university_id):
	return "This page will be for showing rooms for  a university %s" % university_id


@app.route("/university/<int:university_id>/rooms/new/")
def newRoom(university_id):
	return "This page will be for adding a new room for a university %s" % university_id


@app.route("/university/<int:university_id>/<int:room_id>/edit/")
def editRoom(university_id, room_id):
	return "This page will be for editing a particular room in a university %s" % room_id


@app.route("/university/<int:university_id>/<int:room_id>/delete/")
def deleteRoom(university_id, room_id):
	return "This page will be for deleting a room %s" %s room_id







if __name__ == '__main__':
	app.debug = True
	app.run("0.0.0.0", port=5000)