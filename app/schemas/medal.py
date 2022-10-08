from services.config import *


''' Medal Schema:

atributes:
    id: Integer
    title: Text
    description: Text
    icon: Text
    received_date: DateTime <Default value: datetime.now()>
    user_id: Integer <ForeingKey(User.id)>
'''

class Medal(db.Model):
    __tablename__ = 'Medal'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text, nullable = False)
    icon = db.Column(db.Text, nullable = False)
    received_date = db.Column(db.DateTime, default= datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    
    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description" : self.description,
            "received_date" :  self.received_date
        }

    def register_medal(title: str, description: str, icon: str , user_id: int):
        try:
            medal = Medal(title  = title, description = description, icon = icon, user_id = user_id)
            db.session.add(medal)
            db.session.commit()
            return 200, medal.json()
            
        except Exception as error:
            return str(error)