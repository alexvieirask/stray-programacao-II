''' Importação das configurações e serviços '''
from services.config import *
from services.utils import *

''' Esquema: [ Purchase ]
    descrição: Esquema de Purchase utilizado no sistema.
'''
class Purchase(db.Model):
    __tablename__ = 'Purchase'
    id = db.Column(db.Integer, primary_key = True)
    user_buyer_id = db.Column(db.Integer,db.ForeignKey('User.id'))
    game_buyed_id = db.Column(db.Integer,db.ForeignKey('Game.id'))
    realized_date = db.Column(db.DateTime, default = datetime.now())
    
    ''' Com isso é possível acessar os atributos do jogo que o usuário comprou '''
    game = db.relationship('Game', backref = 'purchases')
    
    ''' Usuário não pode comprar o mesmo jogo duas vezes '''
    db.UniqueConstraint(user_buyer_id,game_buyed_id)

    def json(self) -> dict:
        return {
            "id": self.id,
            "user_buyer_id": self.user_buyer_id,
            "game_buyed_id": self.game_buyed_id,
            "realized_date": self.realized_date
        }

    def __lt__(self, object2):
        return self.id < object2.id
    
    def __gt__(self, object2):
        return self.id > object2.id