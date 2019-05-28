import utilities

def find_borne_inf(list_sites, list_edges):
    borne_inf = 0

    for site in list_sites:
        if list_sites[site]["estimated_evacuation_time"] > borne_inf:
            borne_inf = list_sites[site]["estimated_evacuation_time"]

    print("Borne inf = " + str(borne_inf) + " time steps")

    return borne_inf


def find_borne_sup(list_sites, list_edges):
    # Pour la borne sup, on propose de renverser le problème : on réunit tout le monde sur le noeud safe
    # puis on les fait partir vers leur site. Pour améliorer notre borne sup, on commence par remplir les
    # sommets les plus "éloignés" (sens large du terme). Pour estimer un bon ordre des sommets à remplir, on réutilise
    # l'heuristique utilisée pour la borne inf : POPULATION/MIN_CAPACITY + TOTAL_LENGTH
    borne_sup = 0
    sorted_list_sites = utilities.sort_sites_by_evacuation_time(list_sites)
    list_following_sites = sorted_list_sites.copy()
    list_following_sites.pop(0)

    for site in sorted_list_sites:
        sum_following_evac_times = 0
        path_min_capacity = utilities.find_min_capacity(site, list_edges)
        length_to_safe_node = utilities.find_length_to_safe_node(site, list_edges)

        for following_site in list_following_sites:
            sum_following_evac_times += following_site["estimated_evacuation_time"]
        overtime = max(0, length_to_safe_node - sum_following_evac_times)   # l'overtime est le nombre de pas de temps pendant lequel des personnes seront
                                                                            # encore sur le chemin vers ce sommet lorsque le noeud de départ aura été
                                                                            # entièrement vidé (rappel : noeud de départ = noeud safe ici
        if list_following_sites:
            list_following_sites.pop(0)

        borne_sup += round(site["pop"]/path_min_capacity) + overtime

    print("Borne sup = " + str(borne_sup) + " time steps")
    return borne_sup
