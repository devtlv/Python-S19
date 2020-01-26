#!/usr/local/bin/python3
#
# populate.py
# Marketplace

from app import db, models


my_products = [
    {
        'img': 'app/static/images/purimfood1.jpeg',
        'name': 'Purim Food',
        'ins': True,
        'price': 10,
        'category': 'Food'
    },
    {
        'img': 'app/static/images/spidermancostume.jpeg',
        'name': 'Spiderman Costume',
        'ins': True,
        'price': 50,
        'category': 'Clothes'
    },
]

for product in my_products:
    item = models.Item(
        item_name = product['name'],
        price     = product['price'],
        instock   = product['ins'],
        category  = product['category'],
    )
    db.session.add(item)

db.session.commit()

users = [
    {
        'customer_name': 'shaul-test-1',
        'customer_password': 'biltong',
        'status': 'active'
    },
    {
        'customer_name': 'rick-test-1',
        'customer_password': 'morty',
        'status': 'active'
    },
    {
        'customer_name': 'eyal-test-1',
        'customer_password': 'chocolate',
        'status': 'active'
    },
]

for user in users:
    cust = models.Customer(**user)
    db.session.add(cust)

db.session.commit()
