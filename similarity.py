#import site
#site.addsitedir("/home/hanisaf/ODIN/lib")

from gensim.models.Word2Vec import load
import json

model = load('data/model3.model')


def get_updates(word):
    result_json = """
    {
	  "nodes": [
	    {
	      "id": "n0",
	      "label": "A node",
	      "x": 0,
	      "y": 0,
	      "size": 3
	    },
	    {
	      "id": "n1",
	      "label": "Another node",
	      "x": 3,
	      "y": 1,
	      "size": 2
	    },
	    {
	      "id": "n2",
	      "label": "And a last one",
	      "x": 1,
	      "y": 3,
	      "size": 1
	    }
	  ],
	  "edges": [
	    {
	      "id": "e0",
	      "source": "n0",
	      "target": "n1"
	    },
	    {
	      "id": "e1",
	      "source": "n1",
	      "target": "n2"
	    },
	    {
	      "id": "e2",
	      "source": "n2",
	      "target": "n0"
	    }
	  ]
	}
	"""
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