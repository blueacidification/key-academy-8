from flask import Flask

app = Flask(__name__)

from bookstore import routes
_ = routes 
API_TOKEN = "abc123def456"
