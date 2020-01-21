from pyblog import app as pyblog_app
from pyblog import models, db, forms
import flask

@pyblog_app.shell_context_processor
def make_shell_context():
    return {
        'app': pyblog_app,
        'models': models,
        'db': db,
        'forms': forms,
        'flask': flask
    }

if __name__ == "__main__":
    pyblog_app.run(debug=True, port=5000)
