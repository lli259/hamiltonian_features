import sys
import random
import graph_parse
import node_edge #node,edge,bi_edge,out_degree,in_degree,even_out,even_in,odd_out,odd_in,ratio.
import depth_1st_backjump_DFS #the depth of 1st backjump, and all the breadths over the path.
import depth_avgDFS # average depth of full DFS 
import depth_back_edge #the depth when DFS finds a back edge to root.
import depth_back_cycle #the depth when DFS finds a any back edge.
import depth_one_path_found #the depth when DFS finds a node with only one propagation direction.

import bfs # min, max, average depth of breadth first search
import beam # set limititation in BFS: 2 items in each layer, min, max, average depth of BFS


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
				f.write(str(round(i,4)))
			if m[1]==1:
				f.write("\n")
	else:
		#new line
		with open("feature.csv","a") as f:
			for i in m[2:-1]:
				f.write(str(round(i,4)))
				f.write(",")
			f.write(str(round(m[-1],4)))
			if m[1]==1:
				f.write("\n")

graph=graph_parse.read_ham_graph(sys.argv[1])
reverse_graph=node_edge.reverse(graph)


#num_of_nodes,num_of_edges,ratio_node_edge,bi_edge,ratio_bi_edge,min_out_degree,max_out_degree,avg_out_degree,min_in_degree,max_in_degree,avg_in_degree,num_of_odd_out_degree,ratio_of_odd_out_degree,num_of_even_out_degree,ratio_of_even_out_degree,num_of_odd_in_degree,ratio_of_odd_in_degree,num_of_even_in_degree,ratio_of_even_in_degree,num_of_odd_degree,ratio_of_odd_degree,num_of_even_degree,ratio_of_even_degree,out_degree_less_than_3,ratio_out_degree_less_than_3,in_degree_less_than_3,ratio_in_degree_less_than_3,degree_less_than_3,ratio_degree_less_than_3

with open("feature.csv","a") as f:
	a=sys.argv[1]
	if "/" in a:
		f.write(a.split("/")[-1])
	else:
		f.write(a)

#features:
#num_of_nodes,num_of_edges,ratio_node_edge
num_of_nodes=node_edge.get_num_of_nodes(graph)
num_of_edges=node_edge.get_num_of_edges(graph)
ratio_node_edge=node_edge.get_ratio_node_edge(graph)

write_to_file(1,0,num_of_nodes,num_of_edges,ratio_node_edge)

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


#dfs_1st_back_depth,sum_of_choices_along_path,depth_avg_DFS_backjump
start_node="1"
#start_node=sorted(G.keys())[0]
dfs_1st_back_depth,sum_of_choices_along_path=depth_1st_backjump_DFS.dfs(graph,start_node)
write_to_file(1,0,dfs_1st_back_depth,sum_of_choices_along_path)

depth_avg_DFS_backjump=depth_avgDFS.dfs(graph,start_node)
write_to_file(1,0,depth_avg_DFS_backjump)


#depth_back_to_root,depth_back_to_any,depth_one_path
depth_back_to_root=depth_back_edge.dfs(graph,start_node)
write_to_file(1,0,depth_back_to_root)

depth_back_to_any=depth_back_cycle.dfs(graph,start_node)
write_to_file(1,0,depth_back_to_any)

depth_one_path=depth_one_path_found.dfs(graph,start_node)
write_to_file(1,0,depth_one_path)


#bfs
#min_depth_bfs,max_depth_bfs,avg_depth_bfs
min_depth_bfs,max_depth_bfs,avg_depth_bfs=bfs.bfs_edges(graph,start_node)
write_to_file(1,0,min_depth_bfs,max_depth_bfs,avg_depth_bfs)

#beam
#min_depth_beam,max_depth_beam,avg_depth_beam
min_depth_beam,max_depth_beam,avg_depth_beam=beam.bfs_edges(graph,start_node)
write_to_file(1,1,min_depth_beam,max_depth_beam,avg_depth_beam)

#print "features generated for 1 instance"






