import utilities
import math


def find_borne_inf(list_sites):
    borne_inf = 0

    for site in list_sites:
        if list_sites[site]["estimated_evacuation_time"] > borne_inf:
            borne_inf = list_sites[site]["estimated_evacuation_time"]

    # print("Borne inf = " + str(borne_inf) + " time steps")

    return borne_inf


# def find_borne_sup(list_sites, list_edges, safe_node_id):
#     borne_sup = 0
#     start_date = 0
#     sorted_list = utilities.sort_sites_by_evacuation_time(list_sites)
#
#     list_following_sites = []
#     for site_index in sorted_list:
#         list_following_sites.append(site_index[0])
#     list_following_sites.pop(0)
#
#     for site_index in sorted_list:
#         max_following_evac_time = 0
#
#         path_min_capacity = list_sites[site_index]["path_min_capacity"]
#
#         for following_site in list_following_sites:
#             if list_sites[following_site]["estimated_evacuation_time"] > max_following_evac_time:
#                 max_following_evac_time = list_sites[following_site]["estimated_evacuation_time"]
#         overtime = max(0, list_sites[site_index]["estimated_evacuation_time"] - max_following_evac_time)
#
#         if list_following_sites:
#             list_following_sites.pop(0)
#
#         borne_sup += overtime
#
#         list_sites[site_index]["evacuation_rate"] = path_min_capacity
#         list_sites[site_index]["evacuation_start_date"] = start_date
#         print("Sommet " + str(site_index) + " : start date = " + str(start_date) + " , est_evacuation_time = " + str(list_sites[site_index]["estimated_evacuation_time"]))
#         start_date += math.ceil(list_sites[site_index]["pop"]/path_min_capacity)
#
#         # on prend le temps et on le retourne
#     for site_index in list_sites:
#         list_sites[site_index]["evacuation_start_date"] = \
#             borne_sup - list_sites[site_index]["evacuation_start_date"]
#
#     print("Borne sup = " + str(borne_sup) + " time steps")
#     return borne_sup

def find_borne_sup(list_sites, list_edges, safe_node_id):
    borne_sup = 0
    start_date = 0
    sorted_list = utilities.sort_sites_by_evacuation_time(list_sites)
    current_evacuation_time_left = 0

    for site_index in sorted_list:
        path_min_capacity = list_sites[site_index]["path_min_capacity"]
        population = list_sites[site_index]["pop"]
        list_sites[site_index]["evacuation_start_date"] = start_date
        list_sites[site_index]["evacuation_rate"] = path_min_capacity

        if current_evacuation_time_left < list_sites[site_index]["estimated_evacuation_time"]:
            borne_sup += list_sites[site_index]["estimated_evacuation_time"] - current_evacuation_time_left
            current_evacuation_time_left = list_sites[site_index]["estimated_evacuation_time"]

        current_evacuation_time_left -= math.ceil(population/path_min_capacity)
        start_date += math.ceil(population/path_min_capacity)

    # print("Borne sup = " + str(borne_sup))

    for site_index in sorted_list:
        list_sites[site_index]["evacuation_start_date"] = borne_sup - list_sites[site_index]["evacuation_start_date"] - \
                                                          list_sites[site_index]["estimated_evacuation_time"]

    return borne_sup























