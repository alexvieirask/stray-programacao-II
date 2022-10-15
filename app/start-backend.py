
''' Schemas imports '''
from schemas import *
from schemas.game import Game

''' Services imports '''
from services.config import *
from services.database__init__ import *

''' Routes imports '''
from routes import *

''' Home Route '''
@app.route("/")
def home_route():    
    games = db.session.query(Game).all()
    return render_template('pages/home.html', games = games)

if __name__ == "__main__":
    app.run(debug=True) 