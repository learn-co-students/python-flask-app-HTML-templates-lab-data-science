# import flask here
from flask import Flask, render_template

# create new Flask App here
app = Flask(__name__)

# define routes for your new flask app
@app.route('/')
def index():
    return "<h1>Welcome to my flask app</h1><p>be careful, it's still under construction...</p>"

@app.route('/profile/<username>')
def user_profile(username):
    return '<h1>{}</h1>'.format(username)

@app.route('/hello-world-template')
def hello_world_template():
    return render_template('hello_world.html')

@app.route('/profile/<name>/<age>/<favorite_hobby>/<hometown>')
def profile_page(name, age, favorite_hobby, hometown):
    hometown, state = hometown.split(",")
    if "_" in hometown:
        name_of_town = " ".join([name.title() for name in hometown.split("_")])
    else:
        name_of_town = hometown.title()
    return render_template('profile.html', name=name, age=age, favorite_hobby=favorite_hobby, name_of_town=name_of_town, state=state.upper())


# tell your flask app to run with debug mode on
app.run(debug=True)
