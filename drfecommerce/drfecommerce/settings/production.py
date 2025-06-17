from .base import *

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY") 

#vohK_fjvtFyoYdeufN0cFZue4F4bjZpO4C2qjkDYPS8