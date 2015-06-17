from flask.ext.wtf import Form
from wtforms import Form ,StringField, BooleanField ,IntegerField, validators
from wtforms.validators import DataRequired

class UserForm(Form):
    id = StringField('id')
    name = StringField('Name', [validators.Length(min=4, max=25)])
    location = StringField('Location', validators=[DataRequired()])
    degree = StringField('Degree', validators=[DataRequired()])
    experience = StringField('Experience', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    email = StringField('Email Address', [validators.Email(message='Enter a valid email id')])
    imagePath = StringField('Address', validators=[DataRequired()])

class SearchForm(Form):
	locality = StringField('locality', validators=[DataRequired()])
	speciality = StringField('speciality', validators=[DataRequired()])

class InputForm(Form):
	name = StringField('name', validators=[DataRequired()])
	location = StringField('locality', validators=[DataRequired()])
	degree = StringField('degree')
	speciality = StringField('speciality', validators=[DataRequired()])
	experience = StringField('experience')
	address = StringField('address', validators=[DataRequired()])
	email = StringField('email', validators=[DataRequired()])
	imagePath = StringField('imagepath')

class UpdateDataForm(Form):
	name = StringField('name', validators=[DataRequired()])
	location = StringField('locality', validators=[DataRequired()])
	degree = StringField('degree')
	speciality = StringField('speciality', validators=[DataRequired()])
	experience = StringField('experience')
	address = StringField('address', validators=[DataRequired()])
	email = StringField('email', validators=[DataRequired()])
	imagePath = StringField('imagepath')

class ReadForm(Form):
	email = StringField('email', validators=[DataRequired()])

class EmailForm(Form):
	email = StringField('email', validators=[DataRequired()])

class UpdateForm(Form):
	email = StringField('email', validators=[DataRequired()])