from flask import Flask

app = Flask(__name__)

from bookstore import routes
_ = routes 
API_TOKEN = os.environ.get('DATABASE_PASSWORD')