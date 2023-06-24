# main.py
from flask import Flask
from strawberry.flask.views import GraphQLView
from schema import schema
from database import init_db

app = Flask(__name__)
app.debug = True

# Initialize the database
init_db()

# Define the GraphQL endpoint
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql_view", schema=schema),
    methods=["GET", "POST"],
)

if __name__ == "__main__":
    app.run()
