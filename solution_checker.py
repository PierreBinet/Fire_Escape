def edge_checker(edge_index, list_edges):

    # this function creates (if it is not already created) the list_event "array" of each edge
    # by adding time-shifted "arrays" of their parent edge(s)
    if not list_edges[edge_index]["checked_?"]:
        list_edges[edge_index]["list_event"] = []

        for parent in list_edges[edge_index]["parent"]:
            length_parent = list_edges[str(parent)]["length"]
            parent_list_event = edge_checker(str(parent), list_edges)
            for t in range(0, len(parent_list_event)+length_parent):
                if t >= len(list_edges[edge_index]["list_event"]):
                    if (t-length_parent) >= 0:
                        list_edges[edge_index]["list_event"].append(parent_list_event[t-length_parent])
                    else:
                        list_edges[edge_index]["list_event"].append(0)
                else:
                    if (t-length_parent) >= 0:
                        list_edges[edge_index]["list_event"][t] += parent_list_event[t-length_parent]
                    # else:
                    #     list_edges[edge_index]["list_event"][t] += 0

            list_edges[edge_index]["checked_?"] = True

    return list_edges[edge_index]["list_event"]


def solution_is_valid(list_sites, list_edges):

    # first part of the checker:
    # for each site, create an "array" of the people evacuated/time unit until the evacuation is over
    valid = True

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
    # for each edge, call the edge checker function which return the list_event "array" of the edge
    for edge in list_edges:
        final_edge_event = edge_checker(edge, list_edges)

        # and check the validity of the returned "array"
        for t in final_edge_event:
            valid &= (t <= list_edges[edge]["capacity"])
        valid &= ((len(final_edge_event)-1) <= list_edges[edge]["due_date"])

        # print((len(final_edge_event)-1))

    return valid
