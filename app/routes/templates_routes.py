from services.config import *
from services.utils import *

''' Rota: [ home_route ]
    descrição: Retorna o template da tela inicial da aplicação.
'''
@app.route("/")
def home_route():
    return render_template("pages/home.html")

''' Rota: [ join_route ]
    descrição: Retorna o template da tela de registro.
'''
@app.route("/join")
def join_route():
    return render_template("pages/register.html")

''' Rota: [ login_route ]
    descrição: Retorna o template da tela de login.
'''
@app.route("/login")
def login_route():
    return render_template("pages/login.html")

@app.route("/myprofile")
def my_profile_route():
    return render_template("pages/my-profile.html")

@app.route("/myprofile/edit")
def my_profile_route_edit():
    return render_template("pages/my-profile-edit.html")

@app.route("/giftcard")
def giftcard_route():
    return render_template("pages/giftcard.html")

@app.route("/game/<int:id>/<string:title>")
def game_route(id,title):
    current_game = db_query_by_id(Game,id)
    if not current_game:
        abort(404)
    return render_template("pages/game.html")

@app.route("/game/add")
def game_add_route():
    return render_template("pages/game-add.html")

@app.route("/admin")
def admin_route():
    return render_template("pages/admin.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("utils/_error.html", code=404, message = "PAGE NOT FOUND" )

@app.errorhandler(401)
def page_not_found(error):
    return render_template("utils/_error.html", code=401, message = "UNAUTHORIZED USER")