''' Importação das configurações  '''
from services.config import *

''' Esquema Game:

atributos:
    id: Integer
    title: Text
    description: Text
    categorie: Text
    price: Text
    required_age: Integer
    launch_date: Text
    developer: Text
    available: Boolean <Default value: true>
    cover: Text <Default value:../static/img/default-cover.gif>
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
    cover = db.Column(db.Text, default = "../static/img/default-cover.gif" )
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
    
    def create_game(title:str, description:str, categorie:str,price:str,required_age:int, 
                    launch_date:str, developer:str, available:bool) -> tuple:
        try:
            game = Game (
                title = title, 
                description = description, 
                categorie = categorie, 
                price = price, 
                required_age = required_age,
                launch_date = launch_date,
                developer = developer, 
                available = available
            )

            db.session.add(game)
            db.session.commit()
            return 200, game.json()
        
        except Exception as error:
            return str(error)
    
    def set_unavailable_game(id) -> tuple:
        try:
            game = Game.query.get(id)
            game.available = False
            db.session.commit()
            return 200, game.json()

        except Exception as error:
            return str(error)