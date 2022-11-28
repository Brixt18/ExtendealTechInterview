import os

from dotenv import load_dotenv

# In case of troubleshooting, try sending the full path of the .env file like this:
# => load_dotenv("/var/www/my_project/my_app/config/.env")
load_dotenv()


class Config(object):
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	SESSION_COOKIE_SECURE = True
	SESSION_COOKIE_HTTPONLY = True
	SESSION_COOKIE_SAMESITE = 'Lax'

	SECRET_KEY = os.getenv("SECRET_KEY")


class Production(Config):
	DEBUG = False


class Development(Config):
	DEBUG = True
	SESSION_COOKIE_SECURE = False
