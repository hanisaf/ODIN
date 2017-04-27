from flask import Flask, render_template
from similarity import get_updates
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/hello')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Welcome to ODIN!'

@app.route('/')
def index():
    return render_template('index.html')
    
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

@app.route('/get_updates/<word>')
def updates(word):
    u = get_updates(word)
    return u

# Will need it to test outside of App Engine
if __name__ == '__main__':
    app.run()
    

