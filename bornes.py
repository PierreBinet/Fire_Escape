import utilities


def borne_inf(list_sites, list_edges):
    max_evacuation_time = 0
    list_sites_with_estimated_times = utilities.estimate_sites_evacuation_times(list_sites, list_edges)
    for site in list_sites_with_estimated_times:

        if site["estimated_evacuation_time"] > max_evacuation_time:
            max_evacuation_time = site["estimated_evacuation_time"]

    print("Borne inf = " + str(max_evacuation_time) + " time steps")

    return max_evacuation_time

#def borne_sup(list_sites, list_edges):
# Pour la borne sup, on propose de renverser le problème : on réunit tout le monde sur le noeud safe
# puis on les fait partir vers leur site. Pour avoir améliorer notre borne sup, on commence par remplir les
# sommets les plus "éloignés" (sens large du terme). Pour estimer un bon ordre des sommets à remplir, on réutilise
# l'heuristique utilisée pour la borne inf : POPULATION/MIN_CAPACITY + TOTAL_LENGTH

