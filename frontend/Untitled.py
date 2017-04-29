
# coding: utf-8

# In[5]:

from flask import Flask
#from werkzeuk.utils import find_modules, import_str


# In[ ]:




# In[2]:

def create_app(config=None):
    app = Flask(__name__)
    app.config.update(config or {})
    #register_blueprints(app)
    return app


# In[ ]:



