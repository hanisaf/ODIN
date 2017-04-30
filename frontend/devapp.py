
# coding: utf-8

# In[1]:

from myapp import *
from flask import request


# In[2]:

app = create_app()


# In[3]:

@app.route("/")
def hello():
    return ApiResult("Hello World!")


# In[4]:

@app.route('/add')
def add_numbers():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is None or b is None:
        raise ApiException('Numbers must be integers')
    return ApiResult({'sum': a + b})


# In[6]:

#app.run(host="0.0.0.0")


# In[ ]:



