from services.config import *
from schemas import *
from services.database__init__ import *
from routes.users import *
from tests.user import *

@app.route("/")
def initial_route():
    return render_template('main/index.html')

if __name__ == "__main__":
    app.run(debug=True) 