def solution_is_valid(number_of_sites, list_sites, safe_node_id, number_of_edges, list_edges):

    # first part: creation of a dictionary containing a list for each edge

    nb_edge = 0
    list_cap = {}
    for edge in list_edges:
        tab_edge_length = []
        for i in range(edge["length"]):
            tab_edge_length.append(0)
        people_left_to_evacuate = 0
        list_cap[str(edge["node_src"])] = (tab_edge_length, edge["capacity"], edge["due_date"], edge("node_dest"),
                                           edge["node_src"])
        nb_edge += 1

    # sec ond part: actualization of the dictionary's content for each time unit
    t = 0

    while False: # ici prochainement une condition
        # d'abord, actualizer l'interieur du tableau,
        for edge in list_cap:
            last_of_the_tab = edge[0][-1] # last element of the tab edge length
            for i in reversed(range(edge[0])):
                if i >= 1:
                    edge[0][i-1] += edge[0][i]
                else:
                    edge[0][i] = walking_people[str(edge["node_src"])]
            # assigner last of the tab a la premiere case de
            # edge node _dest last_of_the_tab
            # ou alors creer une autre variable dans le dico (people to assign at the first case)
            # et au debut du for edge in list cap tu l'assigne, et du coup ça rejoint les walking people!!!!

        # puis ajouter des nouveaux gens
        walking_people = {}
        for site in list_sites:
            if t >= site("evacuation_start_date"): # and if il reste des gens a evacuer
                walking_people[site["id"]] = site["evacuation_rate"]
                site["pop"] -= walking_people[site["id"]]

        # du coup ici rajouter un truc pour assigner le walking people dans le "people to assign"




