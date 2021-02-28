from app import app
from db import db

db.init_app(app)

@app.before_first_request    # It creates the database and all the necessary tables if does not exist
def create_tables():
    db.create_all()