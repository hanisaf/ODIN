
# coding: utf-8

# In[9]:

from flask import Flask, json, Response, request
#from werkzeuk.utils import find_modules, import_str


# In[24]:

class ApiResult(object):
    def __init__(self, value, status=200):
        self.value = value
        self.status = status
        
    def to_response(self):
        return Response(json.dumps(self.value), status=self.status, mimetype='application/json')


# In[ ]:

class ApiException(object):
    def __init__(self, message, status=400):
        self.message = message
        self.status = status
    
    def to_result(self):
        return ApiResult({'message':self.message}, status=self.status)


# In[10]:

class ApiFlask(Flask):
    def make_response(self, rv):
        if isinstance(rv, ApiResult):
            return rv.to_response()
        return Flask.make_response(self, rv)
    def register_error_handlers(app):
        app.register_error_handler(ApiException, lambda err: err.to_result())
    


# In[11]:




# In[12]:




# In[13]:

def create_app(config=None):
    app = ApiFlask(__name__)
    app.config.update(config or {})
    #register_error_handlers(app)
    #register_blueprints(app)
    return app


# In[28]:

e=ApiException('err')


# In[29]:

type(e)


# In[31]:

e.to_result().to_response()


# In[ ]:



