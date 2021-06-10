"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets, People
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object

@app.route("/people",methods=['GET'])
def get_all_people():
    people = People.get_all()
    people_dic = []
    for person in people :
        people_dic.append(person.serialize())
    return jsonify(people_dic)
    
@app.route("/people/<int:person_id>", methods=['GET'])
def person_by_id(person_id):
    people = People.get__by_id(person_id)
    people_serialized = people.serialized()
    return jsonify(people_serialized)
    
@app.route("/planets", methods=["GET"])
def get_all_planets():
    planets = Planets.get_all()
    planets_dic = []
    for planet in planets :
        planets_dic.append(planet.serialize())
    return jsonify(planets_dic)

@app.route("/planets/<int:planet_id>", methods=['GET'])
def planet_by_id(planet_id):
    planet = Planets.get_by_id(planet_id)
    planet_serialized = planet.serialized()
    return jsonify(planet_serialized) 

#GET USERS AND GET USERS FAVORITES

#Post favorire planet by id and favrotie people


@app.route("/people",methods=['POST'])
def create_person ():
    print(request.json)
    json = request.get_json()
    people = People()
    people.set_with_json(json)
    people.db_post()
    return jsonify(people.serialize())

@app.route("/planets",methods=['POST'])
def create_planet():
    planets = Planets()
    planets.set_with_json(json)
    planets.db_post()
    return jsonify(planets.serialize())

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
