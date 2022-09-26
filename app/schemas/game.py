from services.config import *

''' Class Game:  desc.  '''
class Game(db.Model):
    __tablename__ = 'Game'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text, nullable = False)
    categorie = db.Column(db.Text, nullable = False)
    price = db.Column(db.Text, nullable = False)
    required_age = db.Column(db.Integer, nullable = False)
    launch_date = db.Column(db.Text, nullable = False)
    screenshot = db.Column(db.Text, nullable = False)
    developer = db.Column(db.Text, nullable = False)
    available = db.Column(db.Boolean, default = True)


    ''' this function return datas in JSON format '''
    def json(self):
        return { 
            "id": self.id,
            "title": self.title,
            "description": self.description, 
            "categorie": self.categorie,  
            "price":self.price,
            "required_age": self.required_age,
            "launch_date" : self.launch_date,
            "screenshot" : self.screenshot,
            "developer" : self.developer
        }