import utilities


def find_borne_inf(list_sites):
    borne_inf = 0

    for site in list_sites:
        if list_sites[site]["estimated_evacuation_time"] > borne_inf:
            borne_inf = list_sites[site]["estimated_evacuation_time"]

    print("Borne inf = " + str(borne_inf) + " time steps")

    return borne_inf


def find_borne_sup(list_sites, list_edges, safe_node_id):
    borne_sup = 0
    sorted_list = utilities.sort_sites_by_evacuation_time(list_sites)

    list_following_sites = []
    for site_index in sorted_list:
        list_following_sites.append(site_index[0])
    list_following_sites.pop(0)

    for site_index in sorted_list:
        sum_following_evac_times = 0

        path_min_capacity = utilities.find_min_capacity(site_index, list_edges, safe_node_id) # FAIRE UNE FONCTION QUI MET CA DANS UNE CLE DES SITES + APPELER DANS LE MAIN

        for following_site in list_following_sites:
            sum_following_evac_times += list_sites[following_site]["estimated_evacuation_time"]
        overtime = max(0, list_sites[site_index]["estimated_evacuation_time"] - sum_following_evac_times)

        if list_following_sites:
            list_following_sites.pop(0)

        borne_sup += round(list_sites[site_index]["pop"]/path_min_capacity) + overtime

    print("Borne sup = " + str(borne_sup) + " time steps")
    return borne_sup
