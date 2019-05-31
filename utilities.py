import copy


def find_edge(last_node, next_node, list_edges):
    for edge in list_edges:
        if ([edge["node_src"], edge["node_dst"]] == [last_node, next_node]) or \
          ([edge["node_dst"], edge["node_src"]] == [last_node, next_node]):
            return edge


def estimate_sites_evacuation_times(list_sites, list_edges, safe_node_id):
    for site_index in list_sites:
        min_capacity = list_sites[site_index]["path_min_capacity"]
        total_length = find_length_to_safe_node(site_index, list_edges, safe_node_id)
        total_evacuation_time = list_sites[site_index]["pop"]/min_capacity + total_length
        list_sites[site_index]["estimated_evacuation_time"] = int(total_evacuation_time)
    return list_sites


def min_capacities(list_sites, list_edges, safe_node_id):
    for site_index in list_sites:
        first_edge = list_edges[site_index]
        min_capacity = first_edge["capacity"]

        current_edge = list_edges[str(first_edge["node_dst"])]
        while current_edge["node_dst"] != safe_node_id:
            if current_edge["capacity"] < min_capacity:
                min_capacity = current_edge["capacity"]
            current_edge = list_edges[str(current_edge["node_dst"])]

        if current_edge["capacity"] < min_capacity:  # on traite la dernière arête
            min_capacity = current_edge["capacity"]

        list_sites[site_index]["path_min_capacity"] = min_capacity

    return list_sites


def find_length_to_safe_node(site_index, list_edges, safe_node_id):
    length = 0
    first_edge = list_edges[site_index]
    length += first_edge["length"]

    current_edge = list_edges[str(first_edge["node_dst"])]

    while current_edge["node_dst"] != safe_node_id:
        length += current_edge["length"]
        current_edge = list_edges[str(current_edge["node_dst"])]

    length += current_edge["length"]  # on traite la dernière arête

    return length


def sort_sites_by_evacuation_time(list_sites):
    sorted_list = []
    sites_index_left_to_sort = []

    for site_index in list_sites:
        sites_index_left_to_sort.append(site_index)

    for _ in list_sites:
        max_time = list_sites[sites_index_left_to_sort[0]]["estimated_evacuation_time"]
        max_site_index = sites_index_left_to_sort[0]

        for site_index in sites_index_left_to_sort:
            if list_sites[site_index]["estimated_evacuation_time"] > max_time and site_index in sites_index_left_to_sort:
                max_site_index = site_index
                max_time = list_sites[site_index]["estimated_evacuation_time"]

        sorted_list.append(max_site_index)
        sites_index_left_to_sort.pop(sites_index_left_to_sort.index(max_site_index))

    return sorted_list
