import jinja2
import os
import wikipedia

filename = 'cv.jin'
outfile  = 'cv.html'

# Read content from the html file
content  = open(filename, 'r').read()

# Program

class Comment:

    def __init__(self, title, content, author_name):
        self.title = title.title()
        self.content = content
        self.author_name = author_name
        self.replies = []

    def add_reply(self, comment):
        self.replies.append(comment)


### Adding a reply for example
# Create a comment
comment = Comment(author_name="Eyal", title="I love monkeys", content="Monkeys are so good at python")

# Create a reply
reply   = Comment(author_name="Marev", title="I don't", content="Monkeys aren't good as me..")

# Add this reply to the comment replies list
comment.add_reply(reply)

###

animal_name = "chicken"

# Retrieve the image
path_to_pic_dir = "downloads/"+animal_name.lower()
path_to_pic = list(os.scandir(path_to_pic_dir))[0].path

# Retrieve description
description = wikipedia.summary(animal_name, sentences=1)

hobbies = [
    'Bamboos',
    'Sleeping',
    'Climbing on trees',
    'Steal things'
]

dislikes = [
    'Sport',
    'Fighting',
    'Running away because of deforestation',
]

comments = [
    Comment(author_name="Eyal", title="I love monkeys", content="Monkeys are so good at python"),
    Comment(author_name="Eyal", title="I hate monkeys", content="Monkeys are so bad at javascript"),
    Comment(author_name="Eyal", title="I love empanadas", content="It's so tasty"),
    Comment(author_name="Eyal", title="I love CHOCOLATE", content="But not too much."),
    Comment(author_name="Eyal", title="I lied", content="Hi it's the chocolate guy, i lied in my previous comment..."),
]

# Render it as html
template = jinja2.Template(content)
rendered = template.render(animal_name=animal_name,
                           animal_pic=path_to_pic,
                           description=description,
                           hobbies=hobbies,
                           dislikes=dislikes,
                           comments=comments,
                          )

# Store output into a file
open(outfile, 'w').write(rendered)

