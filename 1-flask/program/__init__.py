from flask import Flask

app = Flask(__name__)

#has to happen after creation of app
from program import routes