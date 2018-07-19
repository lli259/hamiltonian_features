import sys
import random
import graph_parse
import node_edge
import height_1stDFS
import height_avgDFS

def write_to_file(*m):
	'''
	m :  1st bit
		0: append, 1 new line
	     2nd bit
		0: no end, 1 end of line.
	     3rd to end: infomation to write
	'''
	if m[0]==1:
		#append to the line	
		with open("feature.csv","a") as f:
			for i in m[2:]:
				f.write(",")
				f.write(str(i))
			if m[1]==1:
				f.write("\n")
	else:
		#new line
		with open("feature.csv","a") as f:
			for i in m[2:-1]:
				f.write(str(i))
				f.write(",")
			f.write(str(m[-1]))
			if m[1]==1:
				f.write("\n")

graph=graph_parse.read_ham_graph(sys.argv[1])
reverse_graph=node_edge.reverse(graph)


#num_of_nodes,num_of_edges,ratio_node_edge,bi_edge,ratio_bi_edge,min_out_degree,max_out_degree,avg_out_degree,min_in_degree,max_in_degree,avg_in_degree,num_of_odd_out_degree,ratio_of_odd_out_degree,num_of_even_out_degree,ratio_of_even_out_degree,num_of_odd_in_degree,ratio_of_odd_in_degree,num_of_even_in_degree,ratio_of_even_in_degree,num_of_odd_degree,ratio_of_odd_degree,num_of_even_degree,ratio_of_even_degree,out_degree_less_than_3,ratio_out_degree_less_than_3,in_degree_less_than_3,ratio_in_degree_less_than_3,degree_less_than_3,ratio_degree_less_than_3

#features:
#num_of_nodes,num_of_edges,ratio_node_edge
num_of_nodes=node_edge.get_num_of_nodes(graph)
num_of_edges=node_edge.get_num_of_edges(graph)
ratio_node_edge=node_edge.get_ratio_node_edge(graph)

write_to_file(0,0,num_of_nodes,num_of_edges,ratio_node_edge)

#bi_edge,ratio_bi_edge
bi_edge=node_edge.get_num_of_edges(node_edge.get_bi_edge(graph))
ratio_bi_edge=bi_edge/float(num_of_edges)

write_to_file(1,0,bi_edge,ratio_bi_edge)


#min_out_degree,max_out_degree,avg_out_degree
min_out_degree=node_edge.get_min_out_degree(graph)
max_out_degree=node_edge.get_max_out_degree(graph)
avg_out_degree=node_edge.get_avg_out_degree(graph)

write_to_file(1,0,min_out_degree,max_out_degree,avg_out_degree)

#min_in_degree,max_in_degree,avg_in_degree
min_in_degree=node_edge.get_min_out_degree(reverse_graph)
max_in_degree=node_edge.get_max_out_degree(reverse_graph)
avg_in_degree=node_edge.get_avg_out_degree(reverse_graph)

write_to_file(1,0,min_in_degree,max_in_degree,avg_in_degree)

#num_of_odd_out_degree,ratio_of_odd_out_degree,num_of_even_out_degree,ratio_of_even_out_degree
num_of_odd_out_degree=node_edge.get_odd_out_degree(graph)
num_of_even_out_degree=node_edge.get_even_out_degree(graph)
ratio_of_odd_out_degree=num_of_odd_out_degree/float(len(graph.keys()))
ratio_of_even_out_degree=num_of_even_out_degree/float(len(graph.keys()))

write_to_file(1,0,num_of_odd_out_degree,ratio_of_odd_out_degree,num_of_even_out_degree,ratio_of_even_out_degree)

#num_of_odd_in_degree,ratio_of_odd_in_degree,num_of_even_in_degree,ratio_of_even_in_degree
num_of_odd_in_degree=node_edge.get_odd_out_degree(reverse_graph)
num_of_even_in_degree=node_edge.get_even_out_degree(reverse_graph)
ratio_of_odd_in_degree=num_of_odd_in_degree/float(len(reverse_graph.keys()))
ratio_of_even_in_degree=num_of_even_in_degree/float(len(reverse_graph.keys()))
write_to_file(1,0,num_of_odd_in_degree,ratio_of_odd_in_degree,num_of_even_in_degree,ratio_of_even_in_degree)


#num_of_odd_degree,ratio_of_odd_degree,num_of_even_degree,ratio_of_even_degree
num_of_odd_degree=node_edge.get_odd_degree(graph)
ratio_of_odd_degree=num_of_odd_degree/float(len(graph.keys()))
num_of_even_degree=node_edge.get_even_degree(graph)
ratio_of_even_degree=num_of_even_degree/float(len(graph.keys()))
write_to_file(1,0,num_of_odd_degree,ratio_of_odd_degree,num_of_even_degree,ratio_of_even_degree)


#out_degree_less_than_3,ratio_out_degree_less_than_3
out_degree_less_than_3=node_edge.get_out_degree_less_than_3(graph)
ratio_out_degree_less_than_3=out_degree_less_than_3/float(len(graph.keys()))

write_to_file(1,0,out_degree_less_than_3,ratio_out_degree_less_than_3)

#in_degree_less_than_3,ratio_in_degree_less_than_3
in_degree_less_than_3=node_edge.get_out_degree_less_than_3(reverse_graph)
ratio_in_degree_less_than_3=in_degree_less_than_3/float(len(reverse_graph.keys()))
write_to_file(1,0,in_degree_less_than_3,ratio_in_degree_less_than_3)


#degree_less_than_3,ratio_degree_less_than_3
degree_less_than_3=node_edge.get_degree_less_than_3(graph)
ratio_degree_less_than_3=degree_less_than_3/float(len(graph.keys()))
write_to_file(1,0,degree_less_than_3,ratio_degree_less_than_3)


#height_1st_DFS_backjump,height_avg_DFS_backjump
start_node="1"
height_1st_DFS_backjump=height_1stDFS.dfs(graph,start_node)
write_to_file(1,0,height_1st_DFS_backjump)

height_avg_DFS_backjump=height_1stDFS.dfs(graph,start_node)
write_to_file(1,0,height_avg_DFS_backjump)











