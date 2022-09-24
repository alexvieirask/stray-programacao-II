from services.config import *

''' database __init__ '''
if os.path.exists(database_file):
    print('database ja foi criada anteriormente')
else:
    db.create_all()