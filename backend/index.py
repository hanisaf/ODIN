
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

df=pd.read_csv('corpus/EC2000.csv.gz', encoding='utf-8')


# In[3]:

from whoosh.index import create_in
from whoosh.fields import *


# In[4]:

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True))


# In[5]:

ix = create_in("index", schema)


# In[6]:

writer = ix.writer()


# In[7]:

for i in df.index:
    row = df.ix[i]
    writer.add_document(title=unicode(row['fName']), path=unicode(row['id']), content=unicode(row['text']))


# In[8]:

writer.commit()


# In[9]:

get_ipython().system(u'ls index')


# In[10]:

#!rm -rf index/*


# In[11]:

from whoosh.qparser import QueryParser


# In[12]:


query = QueryParser("content", ix.schema).parse("zoe")
results = ix.searcher().search(query)


# In[15]:

for r in results:
    print(r.highlights(fieldname='content', minscore=0))


# In[14]:

r.highlights(fieldname='content', minscore=0)


# In[ ]:



