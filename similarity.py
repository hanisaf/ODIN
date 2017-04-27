
# coding: utf-8

# In[1]:

from gensim.models import Word2Vec
import json
import networkx as nx
from  networkx.readwrite.json_graph import node_link_data


# In[2]:

model = Word2Vec.load('data/model3.model')


# In[16]:

def get_updates(word):
    if word is not None:
        try:
            results = model.most_similar(word)
            G = nx.DiGraph()
            G.add_node(0, label=word)
            i = 0
            en = 0
            for e in results:
                i = i + 1
                G.add_node(i, label=e[0])
                G.add_edge(1, i, id=en)
                en = en + 1
            rgraph=node_link_data(G, dict(id='id', source='source', target='target', key='key'))
            nodes = rgraph['nodes']
            edges = rgraph['links']
            #nodes=[{"id":"n%d"%i, "label":results[i][0]}  for i in range(len(results))]
            #edges=[]
        except Exception as e:
            nodes=edges=[]
            print(e)
        graph = {"nodes":nodes, "edges":edges}
        result_json = json.dumps(graph)
    return result_json


# In[ ]:




# In[17]:

#get_updates("US")


# In[ ]:



