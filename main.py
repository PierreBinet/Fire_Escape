import parser
import bornes
import utilities
import os.path

path = './InstancesInt/example.full'
number_of_sites, list_sites, safe_node_id, number_of_edges, list_edges = parser.parser_data\
                                                                    (path)
list_sites = utilities.estimate_sites_evacuation_times(list_sites, list_edges)

sorted_list = utilities.sort_sites_by_evacuation_time(list_sites)
print()
print(sorted_list)
print()

filename = os.path.basename(path)

borne_inf = bornes.find_borne_inf(list_sites, list_edges)
borne_sup = bornes.find_borne_sup(list_sites, list_edges)

# create a file with the following functions

print("filename : "+filename)
print("number of sites : "+str(number_of_sites))
for site in list_sites:
    print(str(site["id"])+" "+"evacuation_rate"+" "+str("evacuation_start_date"))
print("solution is valid :")
print("evacuation total time :")
print("computing time :")
print("method used :")

