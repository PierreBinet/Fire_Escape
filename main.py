import parser
import os.path

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

#def solution_is_valid(number_of_sites, list_sites, safe_node_id, number_of_edges, list_edges):
