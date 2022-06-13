import os

class Config:
	# SECRET_KEY = '922140b28f699a317c4cfd5b61fd5239'
	# SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 465
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True
	MAIL_USERNAME = 'deep.inexture@gmail.com'
	MAIL_PASSWORD = 'deep!p@9016782401'
	# MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	# MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')