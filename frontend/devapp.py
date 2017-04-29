
# coding: utf-8

# In[17]:

from myapp import *
from flask import request


# In[13]:

app = create_app()


# In[9]:

@app.route("/")
def hello():
    return ApiResult("Hello World!")


# In[10]:

@app.route('/add')
def add_numbers():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is None or b is None:
        raise ApiException('Numbers must be integers')
    return ApiResult({'sum': a + b})


# In[ ]:



