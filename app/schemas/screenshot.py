from services.config import *


''' Screenshot Schema:

atributes:
    id: Integer
    url: Text
    alt: Text
    game_id: Integer <ForeingKey(Game.id)>
'''
class Screenshot(db.Model):
    __tablename__ = "Screenshot"
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.Text, nullable = False)
    alt = db.Column(db.Text, nullable = False)
    game_id = db.Column(db.Integer,db.ForeignKey('Game.id'))
    
    def json(self):
        return{
            "id": self.id,
            "url": self.url,
            "alt": self.alt,
            "game_id": self.game_id
        }

    def screenshot_add(url:str, alt:str, game_id: int) -> tuple:
        try:
            screenshot = Screenshot(url = url, alt = alt, game_id = game_id) 
            db.session.add(screenshot)
            db.session.commit()
            return 200, screenshot.json()

        except Exception as error:
            return str(error)        
    
    def screenshot_delete(id: int) -> tuple:
        try:
            screenshot = Screenshot.query.get(id)
            db.session.delete(screenshot)
            db.session.commit()
            return 200,screenshot
        
        except Exception as error:
            return str(error)
    
    def return_all_screenshots() -> tuple:
        try:
            screenshots = Screenshot.query.all()
            json_screenshots = [ screenshot.json() for screenshot in screenshots ]
            return 200, json_screenshots

        except Exception as error:
            return str(error) 
