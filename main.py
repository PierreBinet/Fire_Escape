import parser
import bornes
import utilities
import os.path
import solution_checker
import time

start_time = time.time()

# Fetching the file
path = './InstancesInt/example.full'
filename = os.path.basename(path)


# Parsing the file
number_of_sites, list_sites, safe_node_id, number_of_edges, list_edges = parser.parser_data(path)

# Computing the min capacity of the path from each site
utilities.min_capacities(list_sites, list_edges, safe_node_id)
# Computing the lower and higher limits of the evacuation time
list_sites = utilities.estimate_sites_evacuation_times(list_sites, list_edges, safe_node_id)

sorted_list = utilities.sort_sites_by_evacuation_time(list_sites)

borne_inf = bornes.find_borne_inf(list_sites)
borne_sup = bornes.find_borne_sup(list_sites, list_edges, safe_node_id)


# Debug: Creating an arbitrary solution to test
# for site in list_sites:
#     list_sites[site]["evacuation_rate"] = 3
#     list_sites[site]["evacuation_start_date"] = 0
# for edge in list_edges:
#     list_edges[edge]["due_date"] = 32


# Checking the validness of a solution
valid = solution_checker.solution_is_valid(list_sites, list_edges)

end_time = time.time()

# Printing the solution
print("PRINTING THE SOLUTION")
print("Solved the problem with the following input file : \""+filename+"\"")
print("Found "+str(number_of_sites)+" site(s) to evacuate:")
for site in list_sites:
    print("Site n°"+str(site)+" = evacuation_rate: "+str(list_sites[site]["evacuation_rate"])+
          ", evacuation_start_date: "+str(list_sites[site]["evacuation_start_date"]))
if valid:
    print("Solution VALID")
else:
    print("Solution INVALID")
print("Evacuation total time : "+ str(len(list_edges[str(number_of_edges)]["list_event"]) + utilities.get_final_edge_length(list_edges, safe_node_id)))
print("Computing time : " + str((end_time - start_time)*1000) + " ms")
print("Method used : handmade\n")
print("Bastien & Pierre")


# Printing the edges
for edge in list_edges:
    print("edge n°"+edge+ str(list_edges[edge]["list_event"]))

