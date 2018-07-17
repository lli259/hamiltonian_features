def kruskal_spanning_tree(G):

    #initialize differernt set for each node
    nodeset={}
    for index,node in enumerate(G.adj.keys()):
	nodeset[node]=index

    #no need to sort, they are all 1
    #edges = sorted(G.edges)
    edges = G.edges()
    for u, v in edges:
        if nodeset[u] != nodeset[v]:
            yield (u, v)
	
	    # assign set to a smaller index
	    if nodeset[u]<nodeset[v]:
		nodeset[v]=nodeset[u]
	    else:
		nodeset[u]=nodeset[v]


'''
class G():
	def __init__(self,dc):
		self.adj=dc
	def edges(self):
		edges=[]
		for i in self.adj.keys():
			for j in self.adj[i]:
				edges+=[(i,j)]
		return edges
	
a={
1:[2,3],
2:[1],
3:[1]
}	
graph=G(a)
print list(kruskal_spanning_tree(graph))
'''
