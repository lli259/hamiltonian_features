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

    choiceseachlayer=[]
    dfs_1st_back_depth=0

    dfspath=[]
    visited = set()

    for start in nodes:
        if start in visited:
            continue
        visited.add(start)
   	stack = [(start, 0, iter(G[start]))]
        while stack:

            parent, depth_now, children = stack[-1]
            try:
                #0.child = next(children)
	
		#1.random choice
		childrens_list=list(children)
		#print "#",len(childrens_list)
		choiceseachlayer.append(len(childrens_list))
		child=random.choice(childrens_list)

                if child not in visited:
			dfspath.append((parent, child))
                  	visited.add(child)
                        stack.append((child, depth_now + 1, iter(G[child])))

            #0.next(children) error: 
	    #except StopIteration:

	    #1.random choice error
	    except IndexError:
		parent, depth_now, children = stack[-1]
		#print "The maximum depth this DFS is: ",depth_now
		dfs_1st_back_depth=depth_now
		#0. If we want to continue the search 
		#stack.pop()
		#1. If we want to terminate search after the first run:
		stack=[]
	#print dfspath
        return dfs_1st_back_depth,sum(choiceseachlayer)	 
              
def __main__():

	'''
	graph = {'A': ["C"],
		  'B': ['C','A'],
		  'C':[]}
	'''

	#graph=graph_parse.read_ham_graph("instance_test_3nodes.lp")
	graph=graph_parse.read_ham_graph(sys.argv[1])

	#print graph
	dfs_1st_back_depth,sum_of_choices_along_path=dfs(graph,"1")
	#print dfs_1st_back_depth,sum_of_choices_along_path
