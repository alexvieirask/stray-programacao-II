from services.config import *


''' Class Purchase:  desc. '''

class Purchase(db.Model):
    __tablename__ = 'Purchase'

    id = db.Column(db.Integer, primary_key = True) 
    user_id = db.Column(db.Integer,db.ForeignKey('User.id'))
    game_id = db.Column(db.Integer,db.ForeignKey('Game.id'))
    user = db.relationship('User' , backref = 'purchases')
    game = db.relationship('Game' , backref = 'purchases')
    date_realized = db.Column(db.DateTime, default = datetime.now())
    db.UniqueConstraint(user_id,game_id)
