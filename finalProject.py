from flask import Flask

app = Flask(__name__)

def showUniversities():
	return "This page shows all the universities and their cities"


def newUniversity():
	return "This page will be for adding new Universities"


def editUniversity():
	return "This page will be for editing a university %s" % university_id


def deleteUniversity():
	return "This page will be for deleting a university %s" % university_id


def showRoom():
	return "This page will be for showing rooms for  a university %s" % university_id


def newRoom():
	return "This page will be for adding a new room for a university %s" % university_id


def editRoom():
	return "This page will be for editing a particular room in a university %s" % room_id


def deleteRoom():
	return "This page will be for deleting a room %s" %s room_id


if __name__ == '__main__':
	app.debug = True
	app.run("0.0.0.0", port=5000)