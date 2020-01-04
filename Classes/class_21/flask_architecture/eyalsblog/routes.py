from eyalsblog import app

@app.route('/')
def homepage():
    return "Welcome to my blog !"
