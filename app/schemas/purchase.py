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

    ''' this function return datas in JSON format '''
    def json(self) -> dict:
        return {
            'purchase_id': self.id,
            'user_buyer_id': self.user_buyer_id,
            'game_buyed_id': self.game_buyed_id,
            'realized_date': self.realized_date
        }

    ''' this func '''
    def create_purchase(user_buyer_id: int, game_buyed_id: int) -> tuple:
        try:
            PURCHASE = Purchase(
                user_buyer_id = user_buyer_id, 
                game_buyed_id = game_buyed_id 
            ) 
            db.session.add(PURCHASE)
            db.session.commit()
            return 200, PURCHASE.json()

        except Exception as error:
            return str(error)
    
    ''' this func '''
    def return_all_purchases() -> tuple:
        try:
            PURCHASES = Purchase.query.all()
            json_purchases =[ purchase.json() for purchase in PURCHASES]
            return 200, json_purchases
        
        except Exception as error:
            return error
    