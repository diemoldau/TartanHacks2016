from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, FileField, SelectField
from wtforms.validators import DataRequired, Length
from .models import User

class LoginForm(Form):
	nickname = StringField('nickname',validators= [DataRequired()])
	password = StringField('password',validators =[DataRequired()])
	remember_me = BooleanField('remember_me',default = False)

class RegisterForm(Form):
	nickname = StringField('openid',validators= [DataRequired()])
	password = StringField('password',validators =[DataRequired()])
	email = StringField('email',validators= [DataRequired()])

	def validate(self):
		if not Form.validate(self):
			return False
		user = User.query.filter_by(nickname = self.nickname.data).first()
		if not user is None:
			self.nickname.errors.append('Nickname taken. Choose another one')
			return False
		return True

class ProfileForm(Form):
	description = StringField('desc')

class RatingForm(Form):
	rating = SelectField('rating', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])

class Listingform(Form):
	description = StringField('desc')
	location = StringField('loc')
	timeAvail = StringField('time')