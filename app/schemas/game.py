from services.config import *


''' Class Game:  desc.  '''
class Game(db.Model):
    __tablename__ = 'Game'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text, nullable = False)
    categorie = db.Column(db.Text, nullable = False)
    price = db.Column(db.Numeric, nullable = False)
    required_age = db.Column(db.Integer, nullable = False)
    pc_requirements = db.Column(db.Text, nullable = False)
    launch_date = db.Column(db.DateTime, nullable = False)
    screenshot = db.Column(db.Text, nullable = False)

    ''' this function return datas in JSON '''
    def json(self):
        return { 
            "id": self.id,
            "name": self.name,
            "description": self.description, 
            "categorie": self.categorie,  
            "price":self.price,
            "required_age": self.required_age,
            "pc_requirements": self.pc_requirements,
            "launch_date" : self.launch_date,
            "screenshot" : self.screenshot
        }