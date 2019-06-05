import parser
import bornes
import utilities
import os.path
import solution_checker
import solution_finder
import time
import total_time


# Starting the "computing time" timer
start_time = time.time()

# Fetching the file
path = 'InstancesInt/example.full'
filename = os.path.basename(path)


# Parsing the file
number_of_sites, list_sites, safe_node_id, number_of_edges, list_edges, last_edge_index = parser.parser_data(path)


# Computing the min capacity of the path from each site
utilities.min_capacities(list_sites, list_edges, safe_node_id)


# Computing the lower and higher limits of the evacuation time
list_sites = utilities.estimate_sites_evacuation_times(list_sites, list_edges, safe_node_id)

sorted_list = utilities.sort_sites_by_evacuation_time(list_sites)

borne_inf = bornes.find_borne_inf(list_sites)
borne_sup = bornes.find_borne_sup(list_sites, list_edges, safe_node_id)


list_original = {}
# Debug: Creating an arbitrary solution to test
for site in list_sites:
    # list_sites[site]["evacuation_rate"] = 3
    # list_sites[site]["evacuation_start_date"] = 52
    list_original[site] = []
    list_original[site].append(list_sites[site]["evacuation_rate"])
    list_original[site].append(list_sites[site]["evacuation_start_date"])

# for edge in list_edges:
#     list_edges[edge]["due_date"] = 358




# Finding a solution based on the bornes sup/inf found
solution_finder.find_solution(number_of_sites, list_sites, list_edges, last_edge_index, list_original)


# Checking the validness of a solution
valid, valid_cap, valid_due_date, evacuation_total_time = \
    solution_checker.solution_is_valid(list_sites, list_edges, last_edge_index)


# Ending the "computing time" timer
end_time = time.time()


# Printing the solution
print("PRINTING THE SOLUTION")
print("Solved the problem with the following input file : \""+filename+"\"")
print("Found "+str(number_of_sites)+" site(s) to evacuate:")
for site in list_sites:
    print("Site n°%3s" % site, "= rate: %3s" % list_sites[site]["evacuation_rate"],
          ", start_date: %3s" % list_sites[site]["evacuation_start_date"],
          ", estimated_evacuation_time: %3s" % list_sites[site]["estimated_evacuation_time"])
if valid:
    print("Solution VALID")
else:
    if not valid_cap:
        print("Solution INVALID because edge capacities were violated")
    else:
        print("Edges capacities respected")
    if not valid_due_date:
        print("Solution INVALID because edges were used beyond their due dates")
print("Solution lower limit: "+str(borne_inf)+" upper limit: "+str(borne_sup))
print("Evacuation total time : " + str(evacuation_total_time))
print("Computing time : " + str((end_time - start_time)*1000) + " ms")
print("Method used : handmade")
print("Bastien & Pierre\n")


# Printing the edges
for edge in list_edges:
    print("edge n°%3s: " % edge, "capacity: %3s" % list_edges[edge]["capacity"], str(list_edges[edge]["list_event"]))

total_time = total_time.compute_total_time(list_sites)

print("TOTAL TIME : ")
print(total_time)
# list_edges["13"]["checked_?"] = False
# list_edges["97"]["checked_?"] = False
# print(solution_checker.edge_checker("13", list_edges))
# print(solution_checker.edge_checker("97", list_edges))

