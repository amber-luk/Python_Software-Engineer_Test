from flask import Flask


app = Flask(__name__)

SECRET_KEY = 'w450p9nmtpb4brnpei'
app.config['SECRET_KEY'] = SECRET_KEY

from app import routes