import os
from flask import Flask
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from charity_box.organizations.views import organizations

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
cred_file = os.path.join(os.path.dirname(__file__), "serviceAccountKey.json")
cred = credentials.Certificate("charity_box/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

app.register_blueprint(organizations, url_prefix='/organizations')
