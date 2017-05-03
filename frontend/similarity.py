
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

class JsonGraph(nx.Graph):
    #def add_node(self, n, attr_dict=None, **attr):
    #    nx.DiGraph.add_node(self, n, attr_dict, x=randint(0,100), y=randint(0,100), size=3, **attr)
        
    def jsonify(self):
        G = self
        H = nx.Graph()
        node_dict = dict(zip(G.nodes(), range(len(G.nodes()))))
        for i in node_dict.keys():
            H.add_node(node_dict[i], label=i, x=randint(0,100), y=randint(0,100), size=3)
        i = 0
        for e in G.edges():
            H.add_edge(node_dict[e[0]], node_dict[e[1]], id="e%d"%i)
            i = i + 1
        rgraph=node_link_data(H, dict(id='id', source='source', target='target', key='key'))
        nodes = rgraph['nodes']
        edges = rgraph['links']
        return {"nodes":nodes, "edges":edges}


# In[4]:

def gen_concepts(words, topn=10):
    G = JsonGraph()
    for word in words:
        G = nx.compose(G,gen_concept(word))
    return G  


# In[5]:

def gen_concept(word, topn=10):
    G = JsonGraph()
    if word is not None:
        results = model.most_similar(word,topn=topn)
        G.add_node(word)
        for e in results:
            G.add_node(e[0])
            G.add_edge(word, e[0])
    return G

