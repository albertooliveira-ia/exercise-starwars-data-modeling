from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    subscription_date = db.Column(db.DateTime)
    username = db.Column(db.String(50), unique=True, nullable=False)
    favorites = db.relationship('Favorite', backref='user', lazy=True)

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_year = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    height = db.Column(db.String(20))
    skin_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    favorites = db.relationship('Favorite', backref='character', lazy=True)

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    climate = db.Column(db.String(50))
    diameter = db.Column(db.String(50))
    orbital_period = db.Column(db.String(50))
    population = db.Column(db.String(50))
    terrain = db.Column(db.String(50))
    favorites = db.relationship('Favorite', backref='planet', lazy=True)

class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))

    def __repr__(self):
        return f'<Favorite {self.id}>'