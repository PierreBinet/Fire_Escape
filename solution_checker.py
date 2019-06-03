def sum_shifted_list(list_orig, l2, shift):
    l2 = [0]*shift + l2
    for t in range(len(l2)):
        if t > len(list_orig):
            list_orig.append(l2[t])
        else:
            list_orig[t] += l2[t]
    return list_orig


def edge_checker(edge_index, list_edges):

    # this function creates (if it is not already created) the list_event "array" of each edge
    # by adding time-shifted "arrays" of their parent edge(s)
    if not list_edges[edge_index]["checked_?"]:
        list_edges[edge_index]["list_event"] = []
        for parent in list_edges[edge_index]["parent"]:
            parent_list_event = edge_checker(str(parent), list_edges)
            if not list_edges[str(parent)]["checked_?"]:
                print("ERREUR")
            length_parent = list_edges[str(parent)]["length"]
            # print(list_edges[str(parent)]["checked_?"])
            # print(parent_list_event)
            # print(len(parent_list_event) + length_parent)
            list_edges[edge_index]["list_event"] = sum_shifted_list(list_edges[edge_index]["list_event"], parent_list_event, length_parent)

        # print(str(len(list_edges[edge_index]["list_event"]))+"new")
        # if len(list_edges[edge_index]["list_event"]) == 243:
        #     print(list_edges[edge_index])
        list_edges[edge_index]["checked_?"] = True

    return list_edges[edge_index]["list_event"]


def solution_is_valid(list_sites, list_edges, last_edge_index):

    # first part of the checker:
    # for each site, create an "array" of the people evacuated/time unit until the evacuation is over
    valid = True
    valid_cap = True
    valid_due_date = True

    for site in list_sites:
        list_sites[site]["list_event"] = []
        quot = (list_sites[site]["pop"]//list_sites[site]["evacuation_rate"])
        rest = (list_sites[site]["pop"] % list_sites[site]["evacuation_rate"])

        if list_sites[site]["evacuation_start_date"] > 0:
            for t in range(0, list_sites[site]["evacuation_start_date"]):
                list_sites[site]["list_event"].append(0)

        for t in range(0, quot):
            list_sites[site]["list_event"].append(list_sites[site]["evacuation_rate"])
        if rest > 0:
            list_sites[site]["list_event"].append(rest)
        # copy of each site's array into the corresponding edge
        list_edges[site]["list_event"] = []
        list_edges[site]["list_event"] = list_sites[site]["list_event"]
        list_edges[site]["checked_?"] = True

    # second part of the checker:
    # calls the edge checker function which creates the list_event "array" for the remaining edges
    # and check the validity of the returned "array"
    for edge in list_edges:
        final_edge_event = edge_checker(edge, list_edges)

        for t in final_edge_event:
            valid_cap &= (t <= list_edges[edge]["capacity"])
        valid_due_date &= ((len(final_edge_event)-1) <= list_edges[edge]["due_date"])

        # print((len(final_edge_event)-1))
    valid = valid_cap and valid_due_date

    # computes the the total evacuation time
    max = len(list_edges[str(last_edge_index)]["list_event"]) + list_edges[str(last_edge_index)]["length"]
    # print(last_edge_index)
    # print("final edge: "+str(list_edges[str(last_edge_index)]["list_event"]))

    return valid, valid_cap, valid_due_date, max
