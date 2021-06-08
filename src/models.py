from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text, Boolean, Column

db = SQLAlchemy()

class BaseModel():
    @classmethod
    def get_all(cls):
        return cls.query.all()
        
    @classmethod
    def get_one(cls,id):
        return cls.query.get(id)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
    email= db.Column(db.String(250), nullable=False)
    password= db.Column(db.String(250), nullable=False)
    is_logged= db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,  
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
            "is_logged": self.is_logged
            # do not serialize the password, its a security breach
        }
    
class Planets(db.Model):
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
        
class People(db.Model):
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

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             do not serialize the password, its a security breach
#         }