import parser
import bornes
import utilities
import os.path
import solution_checker


# Fetching the file
path = './InstancesInt/example.full'
filename = os.path.basename(path)


# Parsing the file
number_of_sites, list_sites, safe_node_id, number_of_edges, list_edges = parser.parser_data(path)


# Computing the lower and higher limits of the evacuation time
# list_sites = utilities.estimate_sites_evacuation_times(list_sites, list_edges)
#
# sorted_list = utilities.sort_sites_by_evacuation_time(list_sites)
# print()
# print(sorted_list)
# print()
#
# borne_inf = bornes.find_borne_inf(list_sites, list_edges)
# borne_sup = bornes.find_borne_sup(list_sites, list_edges)


# Debug: Creating an arbitrary solution to test
for site in list_sites:
    list_sites[site]["evacuation_rate"] = 1
    list_sites[site]["evacuation_start_date"] = 0

# Checking the validness of a solution
valid = solution_checker.solution_is_valid(list_sites, list_edges)


# Printing the solution
print("PRINTING THE SOLUTION")
print("File : \""+filename+"\"")
print("Is the solution found valid? "+str(valid))
print("Evacuation total time : "+str(len(list_edges[str(number_of_edges)]["list_event"])))
print("Computing time : ")
print("Method used : personal method\n")

for edge in list_edges:
    print("edge n°"+edge+": "+str(list_edges[edge]["list_event"]))


# Useless for now, since we do not find our own solutions (yet)
# print("Number of sites found: "+str(number_of_sites))
# for site in list_sites:
#     print("Site "+str(list_sites[site]["id"])+": rate: start date: ")
# print("Number of edges found: "+str(number_of_edges))

