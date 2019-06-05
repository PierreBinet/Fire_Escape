def sum_shifted_list(list_orig, l2, shift):
    if not shift == 0:
        l2 = [0]*shift + l2
    for t in range(len(l2)):
        if t >= len(list_orig):
            list_orig.append(l2[t])
        else:
            list_orig[t] += l2[t]
    return list_orig


def edge_checker(edge_index, list_edges):

    # this function creates (if it is not already created) the list_event "array" of each edge
    # by adding time-shifted "arrays" of their parent edge(s)
    # print("edge: "+str(edge_index))
    # if list_edges[edge_index]["parent"]:
    #     print("parents: "+str(list_edges[edge_index]["parent"]))
    if not list_edges[edge_index]["checked_?"]:
        if not list_edges[edge_index]["checked_site"]:
            list_edges[edge_index]["list_event"] = []
        for parent in list_edges[edge_index]["parent"]:
            parent_list_event = edge_checker(str(parent), list_edges)
            length_parent = list_edges[str(parent)]["length"]
            # print(list_edges[str(parent)]["checked_?"])
            # print(parent_list_event)
            # print(len(parent_list_event) + length_parent)
            list_edges[edge_index]["list_event"] = sum_shifted_list(list_edges[edge_index]["list_event"], parent_list_event, length_parent)

        list_edges[edge_index]["checked_?"] = True

    return list_edges[edge_index]["list_event"]


def solution_is_valid(list_sites, list_edges, last_edge_index):

    # first part of the checker:
    # for each site, create an "array" of the people evacuated/time unit until the evacuation is over
    valid = True
    valid_cap = True
    valid_due_date = True
    list_overcap = []
    list_overdue = []
    list_cap_filling = []

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
        list_edges[site]["checked_site"] = True

    # second part of the checker:
    # calls the edge checker function which creates the list_event "array" for the remaining edges
    # and check the validity of the returned "array"
    final_edge_event = edge_checker(str(last_edge_index), list_edges)

    for edge in list_edges:
        max_edge = 0
        for t in list_edges[edge]["list_event"]:
            if t > max_edge:
                max_edge = t
        if max_edge > list_edges[edge]["capacity"]:
            valid_cap &= False
            list_overcap.append(edge)
        filling = (list_edges[edge]["capacity"] - max_edge)
        list_cap_filling.append((edge, filling))

        if (len(list_edges[edge]["list_event"]) + list_edges[edge]["length"]) > list_edges[edge]["due_date"]:
            valid_due_date &= False
            list_overdue.append(edge)

    list_cap_filling.sort(key=lambda colonnes: colonnes[0])

    valid = valid_cap and valid_due_date

    # computes the the total evacuation time
    max = len(list_edges[str(last_edge_index)]["list_event"]) + list_edges[str(last_edge_index)]["length"]
    # print(last_edge_index)
    # print("final edge: "+str(list_edges[str(last_edge_index)]["list_event"]))

    return valid, valid_cap, valid_due_date, max, list_overcap, list_overdue, list_cap_filling
