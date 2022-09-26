from schemas.game import Game
from services.config import *
from services.games import GAMES

''' Game Schema:
atrr:
    id: Integer
    title: Text
    description: Text
    categorie: Text
    price: Text
    required_age: Integer
    pc_requirements: Text
    launch_date: Text
    screenshot: Text
    developer: Text
    available: Boolean <Default value: true>

functions:
    create_game
    set_unavailable_game
    return_all_games
    return_game_by_id
    default_games_add

'''

''' this func '''
def create_game(title:str, description:str, categorie:str,price:str,required_age:int, 
                launch_date:str, screenshot:str,developer:str, available:bool):
    try:
        GAME = Game ( title = title, description = description, 
                    categorie = categorie, price = price, 
                    required_age = required_age, launch_date = launch_date,
                    screenshot = screenshot, developer = developer, 
                    available = available
                    )
        db.session.add(GAME)
        db.session.commit()
        return 200
    
    except Exception as error:
        return str(error)
            
''' this func '''
def default_games_add():
    try:
        for game in GAMES:
            db.session.add(game)
        db.session.commit()
        return 200
    
    except Exception as error:
        return str(error)