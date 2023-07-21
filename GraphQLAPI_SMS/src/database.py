from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Rest of the code...

db = SQLAlchemy()
db_session=db.session

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
