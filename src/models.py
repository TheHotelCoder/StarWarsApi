from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text, Boolean, Column

db = SQLAlchemy()

class BaseModel():
    @classmethod
    def get_all(cls):
        return cls.query.all()
        
    @classmethod
    def get_by_id(cls,id):
        return cls.query.get(id)
    
    @classmethod 
    def delete_all(cls):
        return cls.query.delete()

class User(db.Model, BaseModel):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
    email= db.Column(db.String(250), nullable=False)
    password= db.Column(db.String(250), nullable=False)
    is_logged= db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,  
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
            "is_logged": self.is_logged
            # do not serialize the password, its a security breach
        }
    
class Planets(db.Model, BaseModel):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    population= db.Column(db.Integer,primary_key=False)
    orbital_period= db.Column(db.Integer,primary_key=False)
    rotation_period= db.Column(db.Integer,primary_key=False)
    diameter = db.Column(db.Integer,primary_key=False)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "name" : self.name,
            "population": self.population,
            "orbital_period" :self.orbital_period,
            "rotation_period" : self.rotation,
            "diameter": self.diammeter 
            # do not serialize the password, its a security breach
        }
        
class People(db.Model, BaseModel):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    eye_color= db.Column(db.String(250))
    skin_color= db.Column(db.String(250))
    gender= db.Column(db.String(250))
    height = db.Column(db.String(250))
    description= db.Column(db.String(250))
    
    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color":self.eye_color,
            "skin_color":self.skin_color,
            "gender":self.gender,
            "height":self.height,
            "description":self.description
        }

    def db_post(self):        
        db.session.add(self)
        db.session.commit()
    
    def set_with_json(self,json):
        self.name = json["name"]
        self.eye_color = json["eye_color"]
        self.skin_color = json["skin_color"]
        self.gender = json["gender"]
        self.height = json["height"]
        self.description = json["description"]

# class Favorites(db.Model):
#     __tablename__ = 'favorite_character'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     user= db.relationship(User)
#     people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
#     people = db.relationship(People)
#     planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
#     planet = db.relationship(Planets)

#     def __repr__(self):
#         return '<Favorites %r>' % self.name

#     def serialize(self):
#         return {
#             "id": self.id,
#             "user_id": self.user_id,
#             "people_id":self.people_id,
#             "people":self.people,
#             "planet_id":self.planet,
#             "user_id":self.user_id,
#             "user":self.user   
  
        # }

