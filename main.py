import parser
import os.path


def find_edge(last_node, next_node, list_edges):
    for edge in list_edges:
        if ([edge["node_src"], edge["node_dst"]] == [last_node, next_node]) or \
          ([edge["node_dst"], edge["node_src"]] == [last_node, next_node]):
            return edge


path = './InstancesInt/example.full'
number_of_sites, list_sites, safe_node_id, number_of_edges, list_edges = parser.parser_data\
                                                                    (path)

filename = os.path.basename(path)

# create a file with the following functions

print("filename : "+filename)
print("number of sites : "+str(number_of_sites))
for site in list_sites:
    print(str(site["id"])+" "+"evacuation_rate"+" "+str("evacuation_start_date"))
print("solution is valid :")
print("evacuation total time :")
print("computing time :")
print("method used :")

