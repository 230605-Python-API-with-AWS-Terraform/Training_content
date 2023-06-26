from flask import Flask
from schemas import schema
from database import db
from strawberry.flask.views import GraphQLView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Sreealee%402609@localhost/day1_demo?port=5432'

# Initialize the database
db.init_app(app)

@app.route('/')
def index():
    return 'Student Management System'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema))

if __name__ == '__main__':
    app.run()
