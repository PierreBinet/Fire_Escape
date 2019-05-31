import utilities


def find_borne_inf(list_sites):
    borne_inf = 0

    for site in list_sites:
        if list_sites[site]["estimated_evacuation_time"] > borne_inf:
            borne_inf = list_sites[site]["estimated_evacuation_time"]

    # print("Borne inf = " + str(borne_inf) + " time steps")

    return borne_inf


def find_borne_sup(list_sites, list_edges, safe_node_id):
    borne_sup = 0
    start_date = 0
    sorted_list = utilities.sort_sites_by_evacuation_time(list_sites)

    list_following_sites = []
    for site_index in sorted_list:
        list_following_sites.append(site_index[0])
    list_following_sites.pop(0)

    for site_index in sorted_list:
        sum_following_evac_times = 0

        path_min_capacity = list_sites[site_index]["path_min_capacity"]

        for following_site in list_following_sites:
            sum_following_evac_times += list_sites[following_site]["estimated_evacuation_time"]
        overtime = max(0, list_sites[site_index]["estimated_evacuation_time"] - sum_following_evac_times)
        # print(overtime)

        if list_following_sites:
            list_following_sites.pop(0)

        borne_sup += round(list_sites[site_index]["pop"]/path_min_capacity) + overtime
        #print(borne_sup)

        list_sites[site_index]["evacuation_rate"] = path_min_capacity
        list_sites[site_index]["evacuation_start_date"] = start_date
        start_date += round(list_sites[site_index]["pop"]/path_min_capacity)

    print("Borne sup = " + str(borne_sup) + " time steps")
    return borne_sup
