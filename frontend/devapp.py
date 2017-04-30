
# coding: utf-8

# In[5]:

from myapp import *
from similarity import gen_concept
from flask import request, render_template


# In[6]:

app = create_app()


# In[ ]:

@app.route('/search')
def index():
    return render_template('index.html')


# In[15]:

@app.route("/hello")
def hello():
    """Return a friendly HTTP greeting."""
    return ApiResult('Welcome to ODIN!')


# In[ ]:

@app.route('/concept/<word>')
def concept(word):
    u = gen_concept(word)
    return ApiResult(u)


# In[4]:

@app.route('/add')
def add_numbers():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is None or b is None:
        raise ApiException('Numbers must be integers')
    return ApiResult({'sum': a + b})


# In[3]:

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.\nCheck /help for more info', 404


# In[ ]:

@app.route('/help')
def help():
    return ApiResult(map(lambda x: x.__repr__(),list(app.url_map.iter_rules())))


# In[ ]:

# Will need it to test outside of App Engine
if __name__ == '__main__':
    app.run()


# In[ ]:



