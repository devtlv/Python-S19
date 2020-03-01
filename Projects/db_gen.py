#!/usr/local/bin/python3
import faker
from faker.providers import geo, person, address
import random
import json

NB_TO_GEN = 1000

fake = faker.Faker()
fake.add_provider(geo)
fake.add_provider(person)
fake.add_provider(address)

fake_date = lambda: fake.date_this_month(before_today=True, after_today=True)

fields = {
    'location':lambda: fake.local_latlng(country_code='US', coords_only=False),
    'renter': lambda: {k:v() for k,v in {'first_name': lambda: fake.first_name(), 'last_name': lambda:fake.last_name(),
               'phone':lambda:fake.phone_number()}.items() },
    'price':lambda: random.randint(500,2000),
    'surface':lambda: random.randint(100,500),
    'dates':lambda: [str(x) for x in set(sorted([fake_date() for _ in range(15)], key=lambda d:
                                                d.day))],
}

d = [{k:v() for k,v in fields.items()} for _ in range(NB_TO_GEN)]
json.dump(d, open('db.json','w')) 
