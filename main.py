from flask import Flask, render_template
import json
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

@app.route('/get_updates')
def updates():
    u = get_updates()
    return u
    #return None

# Will need it to test outside of App Engine
if __name__ == '__main__':
    app.run()
    

def get_updates():
    result_json = """
    {
	  "nodes": [
	    {
	      "id": "n0",
	      "label": "A node",
	      "x": 0,
	      "y": 0,
	      "size": 3
	    },
	    {
	      "id": "n1",
	      "label": "Another node",
	      "x": 3,
	      "y": 1,
	      "size": 2
	    },
	    {
	      "id": "n2",
	      "label": "And a last one",
	      "x": 1,
	      "y": 3,
	      "size": 1
	    }
	  ],
	  "edges": [
	    {
	      "id": "e0",
	      "source": "n0",
	      "target": "n1"
	    },
	    {
	      "id": "e1",
	      "source": "n1",
	      "target": "n2"
	    },
	    {
	      "id": "e2",
	      "source": "n2",
	      "target": "n0"
	    }
	  ]
	}
	"""
    #return json.dumps(result_json)
    return result_json