from flask import Flask
from backend.models import *

app = None # initially app is none

def init_app():
    kanban_app = Flask(__name__) #object of flask
    kanban_app.debug = True
    
    kanban_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///kanban.sqlite3"
    kanban_app.app_context().push() #direct access app and other modules db
    db.init_app(kanban_app)
    print("kanban application started")
    return kanban_app


app = init_app()
from backend.controllers import *

if __name__ == "__main__":
    app.run(debug=True)