from services.config import *


''' Class Screenshot:  desc. '''

class Screenshot(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.Text, nulable = False, unique = True)

    #make relationship