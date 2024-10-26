from flask import Flask
from config import Config
from models import db, User, Goal, Challenge, Team, Event

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return "Welcome to the Corporate Challenge Platform!"

if __name__ == '__main__':
    app.run(debug=True)
