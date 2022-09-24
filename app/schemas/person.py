from services.config import db

''' Class Person:  desc. '''
class Person(db.Model):
    __tablename__ = 'Person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    country = db.Column(db.Text)
    age = db.Column(db.DateTime, nullable = False)
    description = db.Column(db.Text)
    profile_picture = db.Column(db.Text)
    
    ''' this function return datas in JSON '''
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "age": self.age,
            "description": self.description,
            "profile_picture": self.profile_picture
        }