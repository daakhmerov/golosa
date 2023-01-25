from flask import Flask

app = Flask(__name__)

from app import views
from app import menu
from app import db
from app import interview