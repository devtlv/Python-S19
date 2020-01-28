#!/usr/local/bin/python3

# Populate users
import faker
from faker.providers import internet, lorem
import random

from python_landing import db, models

fake = faker.Faker()
fake.add_provider(internet)
fake.add_provider(lorem)

# populate users
for n in range(100):
    user = {
        'username': fake.name(),
        'pwd': 'chocolate',
        'email': fake.ascii_company_email()
    }
    model = models.User(**user)
    db.session.add(model)

db.session.commit()

print("Added 100 random users")

# Populate Tags
tags = ["python", "hacking", "web", "flask", "chocolate", "little robot", "dev", "linux", "mac OSX",
       "windows"]

for tag in tags:
    tag_model = models.Tag(name=tag)
    db.session.add(tag_model)

db.session.commit()
print("Added tags:", tags)

# Populate Topics
users = models.User.query.all()
tags  = models.Tag.query.all()

for n in range(10):
    topic = {
        'subject': fake.paragraph(nb_sentences=1),
        'body': fake.paragraph(nb_sentences=4, variable_nb_sentences=True)
    }

    author = random.choice(users)
    tag    = random.choice(tags)

    model = models.Topic(**topic)
    author.topics.append(model)
    model.tags.append(tag)

    if random.randint(0, 2) == 1:
        newtag    = random.choice(tags)
        model.tags.append(newtag)

        if random.randint(0, 2) == 1:
            newtag    = random.choice(tags)
            model.tags.append(newtag)


    db.session.add(model)

print("Added 10 random topics")
db.session.commit()

# Populate messages
topics = models.Topic.query.all()

for n in range(50):
    message = {
        'body': fake.paragraph(nb_sentences=3, variable_nb_sentences=True)
    }

    author = random.choice(users)
    topic  = random.choice(topics)

    message = models.Message(**message)
    message.topic = topic
    message.author = author

    db.session.add(message)

print("Added 50 random messages")
db.session.commit()

