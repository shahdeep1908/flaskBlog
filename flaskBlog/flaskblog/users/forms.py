from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])

	submit = SubmitField('Sign Up')

	# wt-forms Custom Validators will automatically check that username or Email Already Exists or not.
	def validate_username(self, username):
		user = User.query.filter_by(username = username.data).first()
		if user:
			raise ValidationError('Username Already Exists. Please Choose Another')

	def validate_email(self, email):
		user = User.query.filter_by(email= email.data).first()
		if user:
			raise ValidationError('Email Already Exists. Please Choose Another')

class LoginForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	remember = BooleanField('Remember Me')

	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators = [DataRequired(), Email()])
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
	submit = SubmitField('Update')

	# wt-forms Custom Validators will automatically check that username or Email Already Exists or not.
	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username = username.data).first()
			if user:
				raise ValidationError('Username Already Exists. Please Choose Another')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email= email.data).first()
			if user:
				raise ValidationError('Email Already Exists. Please Choose Another')

class RequestResetForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired(), Email()])
	submit = SubmitField('Request Password Reset')

	def validate_email(self, email):
		user = User.query.filter_by(email= email.data).first()
		if user is None:
			raise ValidationError('No Account Exists with this Email. Please Register Yourself First!')

class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password', validators = [DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('Reset Password')