''' Importação das configurações e serviços '''
from services.config import *
from services.utils import *

''' Esquema: [ Game ]
    descrição: Esquema de jogo utilizado no sistema.
'''
class Game(db.Model):
    __tablename__ = 'Game'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text, nullable = False)
    categorie = db.Column(db.Text, nullable = False)
    price = db.Column(db.Float, nullable = False)
    required_age = db.Column(db.Integer, nullable = False)
    launch_date = db.Column(db.Text, nullable = False)
    developer = db.Column(db.Text, nullable = False)
    available = db.Column(db.Boolean, default = True)
    cover = db.Column(db.Text, default = "../static/img/games/default-cover.gif" )
    screenshots = db.relationship(Screenshot, backref = 'Game')

    def json(self) -> dict:
        return { 
            "id": self.id,
            "title": self.title,
            "description": self.description, 
            "categorie": self.categorie,  
            "price":self.price,
            "required_age": self.required_age,
            "launch_date" : self.launch_date,
            "developer" : self.developer,
            "available": self.available,
            "cover": self.cover
        }