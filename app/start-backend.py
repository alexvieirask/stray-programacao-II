
from schemas import *
from services.config import *
from services.database__init__ import *
from routes import *

@app.route("/")
def initial_route():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True) 