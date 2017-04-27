
# coding: utf-8

# In[1]:

from gensim.models import Word2Vec
import json


# In[2]:

model = Word2Vec.load('data/model3.model')


# In[4]:

def get_updates(word):
    if word is not None:
    try:
    results = model.most_similar(word)
        nodes=[{"id":"n%d"%i, "label":results[i][0]}  for i in range(len(results))]
        edges=[]
    except:
        nodes=edges=[]
        graph = {"nodes":nodes, "edges":edges}
        result_json = json.dumps(graph)
    return result_json


# In[ ]:




# In[ ]:




# In[ ]:



