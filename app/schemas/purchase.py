from services.config import *


'''Purchase Schema:

atributes:
    id: Integer
    user_buyer_id: Integer <ForeingKey(User.id)>
    game_buyed_id: Integer <ForeingKey(Game.id)>
    realized_date: DateTime <Default value: datetime.now()>
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
            'purchase_id': self.id,
            'user_buyer_id': self.user_buyer_id,
            'game_buyed_id': self.game_buyed_id,
            'realized_date': self.realized_date
        }

    def create_purchase(user_buyer_id: int, game_buyed_id: int) -> tuple:
        try:
            purchase = Purchase(
                user_buyer_id = user_buyer_id, 
                game_buyed_id = game_buyed_id 
            ) 
            db.session.add(purchase)
            db.session.commit()
            return 200, purchase.json()

        except Exception as error:
            return str(error)