import sys


def find_edge(last_node, next_node, list_edges):
    for edge in list_edges:
        if ([edge["node_src"], edge["node_dst"]] == [last_node, next_node]) or \
          ([edge["node_dst"], edge["node_src"]] == [last_node, next_node]):
            return edge


def estimate_sites_evacuation_times(list_sites, list_edges):
    for site in list_sites:
        min_capacity = find_min_capacity(site, list_edges)
        total_length = find_length_to_safe_node(site, list_edges)
        total_evacuation_time = site["pop"]/min_capacity + total_length
        site["estimated_evacuation_time"] = total_evacuation_time
    return list_sites


def find_min_capacity(site, list_edges):
    min_capacity = sys.maxsize
    first_edge = find_edge(site["id"], site["node1"], list_edges)

    if first_edge["capacity"] < min_capacity:
        min_capacity = first_edge["capacity"]

    for k in range(site["number_of_nodes_in_path"] - 1):
        current_edge = find_edge(site["node" + str(k + 1)], site["node" + str(k + 2)], list_edges)
        if current_edge["capacity"] < min_capacity:
            min_capacity = current_edge["capacity"]
    return min_capacity


def find_length_to_safe_node(site, list_edges):
    length = 0
    first_edge = find_edge(site["id"], site["node1"], list_edges)
    length += first_edge["length"]
    for k in range(site["number_of_nodes_in_path"] - 1):
        current_edge = find_edge(site["node" + str(k + 1)], site["node" + str(k + 2)], list_edges)
        length += current_edge["length"]
    return length


def sort_sites_by_evacuation_time(list_sites):
    try:
        list_copy = list_sites.copy()
        sorted_list = []
        for i in range(len(list_copy)):
            site_max = list_copy[0]
            for site in list_copy:
                if site["estimated_evacuation_time"] > site_max["estimated_evacuation_time"]:
                    site_max = site
            sorted_list.append(site_max)
            list_copy.pop(list_copy.index(site_max))
        return sorted_list
    except KeyError:
        print("Erreur : Le temps d'evacuation n'a pas été estimé")