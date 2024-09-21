from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Passenger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    PassengerId = db.Column(db.String(80), unique=True, nullable=False)
    HomePlanet = db.Column(db.String(80), nullable=False)
    CryoSleep = db.Column(db.Boolean, nullable=False)
    Cabin = db.Column(db.String(80), nullable=False)
    Destination = db.Column(db.String(80), nullable=False)
    Age = db.Column(db.Float, nullable=False)
    VIP = db.Column(db.Boolean, nullable=False)
    RoomService = db.Column(db.Float, nullable=False)
    FoodCourt = db.Column(db.Float, nullable=False)
    ShoppingMall = db.Column(db.Float, nullable=False)
    Spa = db.Column(db.Float, nullable=False)
    VRDeck = db.Column(db.Float, nullable=False)
    Name = db.Column(db.String(80), nullable=False)
    hash = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(80), nullable=False)