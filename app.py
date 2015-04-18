from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

#import module for ORM
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, University, Room

#New Imports to help create anti-forgery state token
#login_session works like a dictionary
from flask import session as login_session
import random, string


#create connection to database
engine = create_engine("sqlite:///gotroom.db")
Base.metadata.bind=engine
DBSession = sessionmaker(bind=engine)
session=DBSession()


#create an instance of Flask class with the name
#of the runnung application as the argument
app = Flask(__name__)


@app.route("/login")
def showLogin():
	state = "".join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
	login_session["state"] = state
	return "The current session state is %s" % login_session["state"]

@app.route("/")
@app.route("/university/")
def showUniversities():
	#get all universities from university table
	universities = session.query(University).all()
	return render_template("universities.html", universities=universities)


#add a new university
@app.route("/university/new/", methods=["GET", "POST"] )
def newUniversity():
	if request.method == "POST" and request.form["newCity"] != "":
		newUniversity = University(name=request.form["newUni"], city=request.form["newCity"])
		session.add(newUniversity)
		session.commit()

		#feedback to user
		flash("new university added")
		return redirect(url_for("showUniversities"))
	elif request.method == "POST" and request.form["newCity"] == "":
		flash("City Must Be Added")
		return redirect(url_for("newUniversity"))


	else:
		return render_template("newuni.html")
		

#edit an existing university
@app.route("/university/<int:university_id>/edit/", methods=["GET", "POST"])
def editUniversity(university_id):
	editedUni = session.query(University).filter_by(id=university_id).one()
	if request.method == "POST":
		if request.form["newEditedName"]:
			editedUni.name = request.form["newEditedName"]
		if request.form["newEditedCity"]:
			editedUni.city = request.form["newEditedCity"]
		session.add(editedUni)
		session.commit()

		#feedback to user
		flash("University Successfully Edited")

		return redirect(url_for("showUniversities"))
	else:
		return render_template("edituni.html", university=editedUni)


#delete an existing university
@app.route("/university/<int:university_id>/delete/", methods=["GET", "POST"])
def deleteUniversity(university_id):
	uniToDelete = session.query(University).filter_by(id=university_id).one()
	if request.method == "POST":
		session.delete(uniToDelete)
		session.commit()

		#feedback to user
		flash("University Successfully Deleted")

		return redirect(url_for("showUniversities"))
	else:
		return render_template("deleteuni.html", university=uniToDelete)



#show rooms for a university
@app.route("/university/<int:university_id>/")
@app.route("/university/<int:university_id>/rooms/")
def showRooms(university_id):
	university = session.query(University).filter_by(id=university_id).one()
	rooms = session.query(Room).filter_by(university_id=university_id).all()
	return render_template("rooms.html", rooms=rooms, university=university)


#create a new room for a particular university
@app.route("/university/<int:university_id>/rooms/new/", methods=["GET", "POST"])
def newRoom(university_id):
	if request.method == "POST":
		aNewRoom = Room(owner_name=request.form["ownerName"], size=request.form["roomSize"]\
				       , description=request.form["roomDescription"], price=request.form["roomPrice"]\
				        , address=request.form["adress"], owner_number=request.form["phoneNum"], \
				        university_id=university_id)

		session.add(aNewRoom)
		session.commit()

		#feedback to user
		flash("New Room Created")		

		return redirect(url_for("showRooms", university_id=university_id))
	else:
		return render_template("newroom.html", university_id=university_id)

	


#edit a room in apartuclar university
@app.route("/university/<int:university_id>/<int:room_id>/edit/", methods=["GET", "POST"])
def editRoom(university_id, room_id):
	roomToEdit = session.query(Room).filter_by(id=room_id).one()
	if request.method == "POST":
		if request.form["ownerName"]:
			roomToEdit.owner_name = request.form["ownerName"]
		if request.form["roomSize"]:
			roomToEdit.size = request.form["roomSize"]
		if request.form["roomDescription"]:
			roomToEdit.description = request.fom["roomDescription"]
		if request.form["roomPrice"]:
			roomToEdit.price = request.form["roomPrice"]
		if request.form["adress"]:
			roomToEdit.address = request.form["adress"]
		if request.form["phoneNum"]:
			roomToEdit.owner_number = request.form["phoneNum"]
		session.add(roomToEdit)
		session.commit()

		#feedback to user
		flash("Room Successfully Edited")	

		return redirect(url_for("showRooms", university_id=university_id))
	else:
		return render_template("editroom.html", university_id=university_id, room_id=room_id, room=roomToEdit)

		

	return render_template("editroom.html", university_id=university_id, room_id=room_id, room=roomToEdit)


#delete a room 
@app.route("/university/<int:university_id>/<int:room_id>/delete/", methods=["GET", "POST"])
def deleteRoom(university_id, room_id):
	roomToDelete = session.query(Room).filter_by(id=room_id).one()
	if request.method == "POST":
		session.delete(roomToDelete)
		session.commit()

		#feedback to user
		flash("Room Successfully Deleted")	

		return redirect(url_for("showRooms", university_id=university_id))
	else:
		return render_template("deleteroom.html", university_id=university_id, room_id=room_id, room=roomToDelete)
	

#API Endpoints for GET Requests

#JSON data for list of all universitites
@app.route("/university/JSON/")
def showUniversitiesJSON():
	universities = session.query(University).all()
	return jsonify(universitites=[university.serialize for university in universities])


#JSON data for rooms in a university
@app.route("/university/<int:university_id>/rooms/JSON")
def showRoomsJSON(university_id):
	university = session.query(University).filter_by(id=university_id).one()
	rooms = session.query(Room).filter_by(university_id=university_id).all()
	return jsonify(rooms=[room.serialize for room in rooms])

#JSON data for a single room
@app.route("/university/<int:university_id>/rooms/<int:room_id>/JSON/")
def singleRoomJSON(university_id, room_id):
	university = session.query(University).filter_by(id=university_id).one()
	singleRoom = session.query(Room).filter_by(id=room_id).one()
	return jsonify(room=[singleRoom.serialize])



if __name__ == '__main__':
	app.secret_key = "super_secret_key"
	app.debug = True
	app.run("0.0.0.0", port=5000)