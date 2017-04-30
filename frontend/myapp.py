
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

class ApiException(BaseException):
    def __init__(self, message, status=400):
        self.message = message
        self.status = status
    
    def to_response(self):
        return ApiResult({'message':self.message}, status=self.status)
    
    def to_result(self):
        return self.to_response()


# In[10]:

class ApiFlask(Flask):
    def make_response(self, rv):
        if isinstance(rv, ApiResult):
            return rv.to_response()
        return Flask.make_response(self, rv)
    def register_error_handlers(app):
        app.register_error_handler(ApiException, lambda err: err.to_result())
    


# In[13]:

def create_app(config=None):
    app = ApiFlask(__name__)
    app.config.update(config or {})
    #register_error_handlers(app)
    #register_blueprints(app)
    return app


# In[ ]:



