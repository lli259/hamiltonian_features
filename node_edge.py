import graph_parse
import sys

def reverse(G):
	reverse_graph={}
	for node in G.keys():
		reverse_graph[node]=[]
	for node in G.keys():
		for edge in G[node]:
			reverse_graph[edge].append(node)
	return reverse_graph
		
def get_num_of_nodes(G):
	nodes=G.keys()
	return len(nodes)


def get_num_of_edges(G):
	return sum([len(G[n]) for n in G.keys()])

def get_ratio_node_edge(G):
	num_of_nodes=get_num_of_nodes(G)
	num_of_edges=get_num_of_edges(G)
	return float(num_of_nodes)/num_of_edges

#graph=graph_parse.read_ham_graph("instance_test_3nodes.lp")
graph=graph_parse.read_ham_graph(sys.argv[1])
#print graph

print get_num_of_nodes(graph),get_num_of_edges(graph),get_ratio_node_edge(graph)

#------------------------
reverse_graph=reverse(graph)
#print reverse_graph

print get_num_of_nodes(reverse_graph),get_num_of_edges(reverse_graph),get_ratio_node_edge(reverse_graph)

def get_bi_edge(G):
	bi_graph={}
	for node in G.keys():
		bi_graph[node]=[]
		for edge in G[node]:
			if node in G[edge]:
				bi_graph[node].append(edge)
	return  get_num_of_edges(bi_graph)/2
print "bi_edge:",get_bi_edge(graph)
