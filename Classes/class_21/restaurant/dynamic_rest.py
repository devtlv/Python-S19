import jinja2
import os

filename = 'restaurant.jin'
outfile  = 'restaurant.html'

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

comments = [
    Comment(author_name="Eyal", title="I love monkeys", content="Monkeys are so good at python"),
    Comment(author_name="Eyal", title="I hate monkeys", content="Monkeys are so bad at javascript"),
    Comment(author_name="Eyal", title="I love empanadas", content="It's so tasty"),
    Comment(author_name="Eyal", title="I love CHOCOLATE", content="But not too much."),
    Comment(author_name="Eyal", title="I lied", content="Hi it's the chocolate guy, i lied in my previous comment..."),
]

restaurant_name = "China class"
food_type       = "Traditional chinese"

menu = {
    # TITLE: LIST_OF_CONTENT
    'Starters': ['Seviche', 'Focaccia'],
    'Main': ['Beef', 'Vegan beef'],
    'Desserts': ['Chocolate', 'Muffins'],
    'Wine': ['Pepsi', 'Nestle']
}


# Render it as html
template = jinja2.Template(content)
rendered = template.render(
                restaurant_name=restaurant_name,
                food_type=food_type,
                menu=menu
)

print("Rendered", outfile)


# Store output into a file
open(outfile, 'w').write(rendered)
