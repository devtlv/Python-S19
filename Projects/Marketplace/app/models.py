from app import db, login_mgr
import flask_login


@login_mgr.user_loader
def load_customer(customer_id):
    customer_id = int(customer_id)
    return Customer.query.get(customer_id)

basket_table = db.Table(
    'basket',
    db.Column('customer_id', db.Integer(), db.ForeignKey('customer.customer_id')),
    db.Column('product_id', db.Integer(), db.ForeignKey('item.item_id')),
)

class Customer(flask_login.UserMixin, db.Model):

    customer_id       = db.Column(db.Integer, primary_key=True)
    customer_name     = db.Column(db.String(64))
    customer_password = db.Column(db.String(12))
    status            = db.Column(db.String(64))

    basket            = db.relationship("Item",
                                        secondary=basket_table,
                                        back_populates="buyers"
                                       )

    def get_id(self):
        return self.customer_id

    def __repr__(self):
        return '<Customer {}>'.format(self.customer_name)

class Item(db.Model):
    item_id    = db.Column(db.Integer,primary_key=True)
    item_name  = db.Column(db.String(64))
    price      = db.Column(db.Integer)
    instock    = db.Column(db.Boolean)
    category   = db.Column(db.String(64))

    buyers     = db.relationship('Customer',
                                 secondary=basket_table,
                                 back_populates="basket"
                                )

    def get_id(self):
        return (self.item_id)

    def __repr__(self):
        return '<Item {}>'.format(self.item_name)

    @classmethod
    def get_by_id(cls, item_id):
        return cls.query.get(item_id)




