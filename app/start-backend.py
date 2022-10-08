
''' Schemas imports '''
from schemas import *

''' Services imports '''
from services.config import *
from services.database__init__ import *

''' Routes imports '''
from routes import *

''' Home Route '''
@app.route("/")
def home_route():
    return render_template('pages/home.html')

if __name__ == "__main__":
    app.run(debug=True) 