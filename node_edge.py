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


def get_min_out_degree(G):
	return min([len(G[n]) for n in G.keys()])

def get_max_out_degree(G):
	return max([len(G[n]) for n in G.keys()])

def get_avg_out_degree(G):
	return sum([len(G[n]) for n in G.keys()])/float(len(G.keys()))

#graph=graph_parse.read_ham_graph("instance_test_3nodes.lp")
graph=graph_parse.read_ham_graph(sys.argv[1])
#print graph
print "get_num_of_nodes(graph),get_num_of_edges(graph),get_ratio_node_edge(graph)"
print get_num_of_nodes(graph),get_num_of_edges(graph),get_ratio_node_edge(graph)

#------------------------
reverse_graph=reverse(graph)
#print reverse_graph
print "get_num_of_nodes(reverse_graph),get_num_of_edges(reverse_graph),get_ratio_node_edge(reverse_graph)"
print get_num_of_nodes(reverse_graph),get_num_of_edges(reverse_graph),get_ratio_node_edge(reverse_graph)






def get_bi_edge(G):
	bi_graph={}
	for node in G.keys():
		bi_graph[node]=[]
		for edge in G[node]:
			if node in G[edge]:
				bi_graph[node].append(edge)
	return  bi_graph

print "bi_edge:",get_num_of_edges(get_bi_edge(graph))

print "min_out_degree:",get_min_out_degree(graph),"max_out_degree:",get_max_out_degree(graph),"avg_out_degree:",get_avg_out_degree(graph)
print "min_in_degree:",get_min_out_degree(reverse_graph),"max_in_degree:",get_max_out_degree(reverse_graph),"avg_out_degree:",get_avg_out_degree(reverse_graph)

