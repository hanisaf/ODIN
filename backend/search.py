
# coding: utf-8

# In[6]:

import whoosh.index
from whoosh.qparser import QueryParser


# In[3]:

ix=whoosh.index.open_dir("index")


# In[10]:

def search(term):
    query = QueryParser("content", ix.schema).parse(term)
    results = ix.searcher().search(query)
    high = []
    for r in results:
        high.append(r.highlights(fieldname='content', minscore=0))    
    return high


# In[ ]:



