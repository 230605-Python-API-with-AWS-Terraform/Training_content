from flask import Flask
from strawberry.flask.views import GraphQLView
from schemas import schema
from database import init_db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Sreealee%402609@localhost/Stud_Project_?port=5432"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app)

@app.route("/")
def hello():
    return "Hello, World!"

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == "__main__":
    app.run()
