import graph_parse
import random
import sys


def dfs(G,source=None):
    if source is None:
        # edges for all components
        nodes = G.keys()
    else:
        # edges for components with source
        nodes = [source]

    allpath=[]
    visited = set()
    all_depth=[]
    leave_nodes=[]
    for start in nodes:

        if start in visited:
            continue
        visited.add(start)
   	stack = [(start, 0, iter(G[start]))]
        while stack:
            parent, depth_now, children = stack[-1]
            try:
                child = next(children)
	
                if child not in visited:
			allpath.append((parent, child))
                  	visited.add(child)

	                #if the node has no child
			#Or if the node has no new child
			if (len(G[child])==0) or (sum([0 if nd in visited else 1 for nd in G[child]])==0) :
				#print child,"The maximum depth this DFS is: ",depth_now+1
				leave_nodes.append(child)
				all_depth.append(depth_now+1)

                        stack.append((child, depth_now + 1, iter(G[child])))

	    except StopIteration:

		#0. If we want to continue the search 
		stack.pop()
    #print allpath,max(all_depth)
    return float(sum(all_depth))/len(all_depth)
               
def __main_():
	'''
	graph = {'A': ["C"],
		  'B': ['C','A'],
		  'C':[]}
	'''

	#graph=graph_parse.read_ham_graph("instance_test_3nodes.lp")
	graph=graph_parse.read_ham_graph(sys.argv[1])
	#print graph
	avedepth=dfs(graph,"1")
	#print maxdepth,avedepth
