from flask_app import app

from flask_app.controllers import forms, routes

if __name__=="__main__":
    app.run(debug=True)
