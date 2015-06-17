from app import db

class Practo_doctors(db.Model):
	__tablename__ = 'doctors'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=False)
	degree = db.Column(db.String(64), unique=False) 
	experience =db.Column(db.Integer)
	email = db.Column(db.String(120), unique=True)
	imagePath =db.Column(db.String(64),  unique=True) 
	def __init__(self, name ,email , degree =None , experience =None  , imagePath = None):
		self.name = name
		self.degree = degree 
		self.experience = experience
		self.email = email
		self.imagePath = imagePath
	def __repr__(self):
		return '<User %r>' % (self.name)	

class Location(db.Model):
	__tablename__ = 'location'
	id = db.Column(db.Integer, primary_key=True)
	location = db.Column(db.String(64), index=True, unique=True)
	def __init__(self,location):
		self.location=location

	def __repr__(self):
		return '<User %r>' % (self.location)

class Doctor_location(db.Model):
	__tablename__ = 'doctorlocation'
	id = db.Column(db.Integer, primary_key=True)
	doctorId = db.Column(db.Integer,db.ForeignKey('doctors.id'))
	locationId = db.Column(db.Integer,db.ForeignKey('location.id'))
	address = db.Column(db.String(64), index=True, unique=True)
	def __init__(self,doctorId,locationId,address):
		self.doctorId = doctorId
		self.locationId=locationId
		self.address = address
	def __repr__(self):
		return '%r' % (self.doctorId)

class Speciality(db.Model):
	__tablename__ = 'speciality'
	id = db.Column(db.Integer, primary_key=True)
	speciality =db.Column(db.String(64), index=True, unique=True)
	def __init__(self,speciality):
		self.speciality=speciality
	def __repr__(self):
		return '<User %r>' % (self.speciality)

class Doctor_speciality(db.Model):
	__tablename__ = 'doctorspeciality'
	id = db.Column(db.Integer, primary_key=True)
	doctorId = db.Column(db.Integer,db.ForeignKey('doctors.id'))
	specialityId = db.Column(db.Integer,db.ForeignKey('speciality.id'))
	def __init__(self,doctorId,specialityId):
		self.doctorId=doctorId
		self.specialityId=specialityId
	def __repr__(self):
		return '%r' % (self.doctorId)
