import main


def solution_is_valid(number_of_sites, list_sites, safe_node_id, number_of_edges, list_edges):

    # first part: creation of a dictionnary containing

    nb_edge = 0
    list_cap = {}
    for edge in list_edges:
        tab_edge_capacity = []
        for i in range(edge["length"]):
            tab_edge_capacity.append(0)
        list_cap[str(edge["node_src"])] = (tab_edge_capacity, edge["capacity"], edge["due_date"], edge("node_dest"))
        nb_edge += 1



    t=0
    while False: # ici prochainement une condition
        pass

    for site in list_sites:
        last_node = site["id"]

        for k in range(site["number_of_nodes_in_path"]):
            next_node = site["node" + str(k + 1)]
            edge = main.find_edge(last_node, next_node, list_edges)

            last_node = next_node



