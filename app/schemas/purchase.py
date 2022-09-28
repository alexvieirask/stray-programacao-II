from services.config import *


'''Purchase Schema:
atrr:
    id: Integer
    user_id: Integer <ForeingKey(User.id)>
    game_id: Integer <ForeingKey(Game.id)>
    date_realized: DateTime <Default value: datetime.now()>


functions:
    create_purchase

    verify : user: User = User.query.get(1).purchases[0] 
    print(user.game.title) 


'''

class Purchase(db.Model):
    __tablename__ = 'Purchase'
    id = db.Column(db.Integer, primary_key = True)
    user_buyer_id = db.Column(db.Integer,db.ForeignKey('User.id'))
    game_buyed_id = db.Column(db.Integer,db.ForeignKey('Game.id'))
    date_realized = db.Column(db.DateTime, default = datetime.now())
    
    user = db.relationship('User' , backref = 'purchases')
    game = db.relationship('Game' , backref = 'purchases')
    db.UniqueConstraint(user_buyer_id,game_buyed_id)

    ''' this function return datas in JSON format '''
    def json(self) -> dict:
        return {
            'purchase_id': self.id,
            'user_buyer_id': self.user_buyer_id,
            'game_buyed_id': self.game_buyed_id,
            'date_realized': self.date_realized
        }

    ''' this func '''
    def create_purchase(user_buyer_id: int, game_buyed_id: int) -> tuple:
        try:
            PURCHASE = Purchase(user_buyer_id = user_buyer_id, game_buyed_id = game_buyed_id ) 
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
    