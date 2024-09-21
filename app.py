from flask import Flask

app = None # initially app is none

def init_app():
    kanban_app = Flask(__name__) #object of flask
    kanban_app.debug = True
    kanban_app.app_context().push() #direct access app and other modules db
    print("kanban application started")
    return kanban_app


app = init_app()
from backend.controllers import *

if __name__ == "__main__":
    app.run()