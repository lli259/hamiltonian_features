from collections import deque

import graph_parse
import sys

#G={1:[2,4],2:[1,3],3:[1,2],4:[1]}
graph=graph_parse.read_ham_graph(sys.argv[1])

def bfs_edges(G, source, reverse=False):
    """Produce edges in a breadth-first-search starting at source.

    Parameters
    ----------
    G : NetworkX graph

    source : node
       Specify starting node for breadth-first search and return edges in
       the component reachable from source.

    reverse : bool, optional
       If True traverse a directed graph in the reverse direction

    Returns
    -------
    edges: generator
       A generator of edges in the breadth-first-search.

    Examples
    --------
    >>> G = nx.Graph()
    >>> G.add_path([0,1,2])
    >>> print(list(nx.bfs_edges(G,0)))
    [(0, 1), (1, 2)]

    Notes
    -----
    Based on http://www.ics.uci.edu/~eppstein/PADS/BFS.py
    by D. Eppstein, July 2004.
    """
    if reverse:
        neighbors = iter(G[source])
    else:
        neighbors = iter(G[source])
    
    leave_nodes=[]
    all_depth=[]
    bfs_edges=[]
    visited = set([source])
    queue = deque([(source, 0, neighbors)])

    old_node=''

    while queue:
        parent,height, children = queue[0]

        
        #check if all children are visited or empty.
	#before the node is first visited as a parent
	#it is only done once for a node
        #can't check this at other step as other nodes may become visited because of this node.

	if old_node!= parent:
		#if the node has no child
		#Or if the node has no new child
		#print G[parent],bfs_edges
		if (len(G[parent])==0) or (sum([0 if nd in visited else 1 for nd in G[parent]])==0) :
			leave_nodes.append(parent)
			all_depth.append(height)
			#print "leaf",parent

			#this must be check after all line done , 
			#(1,2),(1,3),(2,3).
			#or it will not treat 2 as leaves because 3 is not reached yet when judge 2.
		old_node=parent


        try:
            child = next(children)
            if child not in visited:
                bfs_edges.append((parent, child))
                visited.add(child)
                queue.append((child,height+1, iter(G[child])))


	    
        except StopIteration:
            queue.popleft()
    return bfs_edges,max(all_depth),float(sum(all_depth))/len(all_depth)
#print graph
bfs_edges,max_depth,avg_depth=bfs_edges(graph, "1", reverse=False)
print max_depth,avg_depth
