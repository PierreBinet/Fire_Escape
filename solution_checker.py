def solution_is_valid(number_of_sites, list_sites, safe_node_id, number_of_edges, list_edges):

    # # first part: creation of a dictionary containing a list for each edge
    #
    # list_cap = {}
    # for edge in list_edges:
    #     people_left_to_evacuate = 0
    #     evacuation_rate = 0
    #     list_cap[str(edge["node_src"])] = (people_left_to_evacuate, edge("node_dest"), edge["capacity"],
    #                                        edge["due_date"], edge["length"], evacuation_rate)
    #
    # # second part: actualization of the dictionary's content for each time unit

    for site in list_sites:
        list_sites[site]["list_event"] = []
        quot = (list_sites[site]["pop"]//list_sites[site]["evacuation_rate"])
        rest = (list_sites[site]["pop"] % list_sites[site]["evacuation_rate"])
        if list_sites[site]["evacuation_start_date"] > 0:
            for t in range(0, list_sites[site]["evacuation_start_date"]):
                list_sites[site]["list_event"].append(0)
        else:
            for t in range(list_sites[site]["evacuation_start_date"], quot):
                list_sites[site]["list_event"].append(list_sites[site]["evacuation_rate"])
            if rest > 0:
                list_sites[site]["list_event"].append(rest)

    valid = True
    for edge in list_edges:
        last_max_range = 0
        list_edges[edge]["list_event"] = []
        # if int(edge) < number_of_sites:
        #     list_edges[edge]["list_event"] = list_sites[str(edge)]["list_event"]
        #     for t in list_edges[edge]["list_event"]:
        #         valid &= (list_edges[edge]["list_event"][t] < list_edges[edge]["capacity"])
        #     last_max_range = len(list_edges[edge]["list_event"])
        # else:
        #     for parent in list_edges[edge]["parent"]:
        #         length_parent = list_edges[str(parent)]["length"]
        #         print(parent)
        #         print(len(list_edges[str(parent)]["list_event"]))
        #         print(length_parent)
        #         for t in range(0, len(list_edges[str(parent)]["list_event"])+length_parent):
        #             if t > last_max_range:
        #                 if t >= length_parent:
        #                     print(t)
        #                     list_edges[edge]["list_event"].append(list_edges[str(parent)]["list_event"][t-length_parent])
        #                 else:
        #                     list_edges[edge]["list_event"].append(0)
        #                 last_max_range = len(list_edges[str(parent)]["list_event"])+length_parent
        #             else:
        #                 if t >= length_parent:
        #                     print(t)
        #                     list_edges[edge]["list_event"][t] += list_edges[str(parent)]["list_event"][t-length_parent]
        #                 else:
        #                     list_edges[edge]["list_event"][t] += 0
        #                 last_max_range = len(list_edges[str(parent)]["list_event"])+length_parent
        #             valid &= (list_edges[edge]["list_event"][t] < list_edges[edge]["capacity"])

        if not valid:
            print("the solution is not valid")
            return valid

    # for site in list_sites:
    #
    #     # d'abord, actualiser l'interieur du tableau,
    #     for edge in list_cap:
    #         last_of_the_tab = edge[0][-1]  # last element of the tab_edge_length
    #         for i in reversed(range(edge[0])):
    #             if i >= 1:
    #                 edge[0][i - 1] += edge[0][i]
    #             else:
    #                 edge[0][i] = walking_people[str(edge["node_src"])]
    #         # assigner last of the tab a la premiere case de
    #         # edge node _dest last_of_the_tab
    #         # ou alors creer une autre variable dans le dico (people to assign at the first case)
    #         # et au debut du for edge in list cap tu l'assigne, et du coup ça rejoint les walking people!!!!



