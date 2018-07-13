'''
instance_test_3nodes.lp

node(1).
node(2).
node(3).
link(1,2).
link(1,3).
link(2,3).
link(2,1).
'''

def read_ham_graph(infile):
	with open(infile,"r") as fread:
		adj_dict={}
		for line in fread:
			#print "line:",line
			if line[0]=="n":
				node=line.split("(")[1].split(")")[0]
				if not node in adj_dict.keys():
					adj_dict[node]=[]
					#print node,adj_dict
			if line[0]=="l":
				node1,node2=line.split("(")[1].split(")")[0].split(",")
				if not node1 in adj_dict.keys():
					adj_dict[node1]=[]
					print node1,adj_dict
				if not node2 in adj_dict.keys():
					adj_dict[node2]=[]
					#print node2,adj_dict
				adj_dict[node1].append(node2)
				#print node1,node2,adj_dict
		return adj_dict

def test():				
	print read_ham_graph("instance_test_3nodes.lp")
