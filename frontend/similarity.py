
# coding: utf-8

# In[1]:

from gensim.models import Word2Vec
import json
import networkx as nx
from  networkx.readwrite.json_graph import node_link_data
from random import randint


# In[2]:

model = Word2Vec.load('data/model3.model')


# In[3]:

class JsonGraph(nx.DiGraph):
    def add_node(self, n, attr_dict=None, **attr):
        nx.DiGraph.add_node(self, n, attr_dict, x=randint(0,100), y=randint(0,100), size=3, **attr)
        
    def jsonify(self):
        rgraph=node_link_data(self, dict(id='id', source='source', target='target', key='key'))
        nodes = rgraph['nodes']
        edges = rgraph['links']
        return {"nodes":nodes, "edges":edges}


# In[ ]:




# In[4]:

def gen_concept(word, topn=10):
    G = JsonGraph()
    if word is not None:
        results = model.most_similar(word,topn=topn)
        G.add_node(0, label=word)
        i = 0
        en = 0
        for e in results:
            i = i + 1
            G.add_node(i, label=e[0])
            G.add_edge(0, i, id=en)
            en = en + 1                
    return G


# In[37]:

def gen_concepts(words, topn=10):
    results = []
    for word in words:
        results.append((word, 1))
        results = results + model.most_similar(word,topn=topn)
    G = JsonGraph()
    
    i=-1
    for e in results:
        i = i + 1
        G.add_node(i, label=e[0])
        #G.add_edge(0, i, id=en)
        #en = en + 1                
    return G    

def gen_concepts(words, topn=10):

    nodes=[]
    edges=[]
    for word in words:
        print(word)
        H = gen_concept(word, topn=topn)
        #nodes.append(H.nodes(data=True))
        #edges.append(H.edges(data=True))
        nodes = nodes + H.nodes(data=True)
        edges = edges + H.edges(data=True)

    G = JsonGraph()
    #G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    print(nodes)
    return nodes,edges
# In[ ]:



