import sys


def find_edge(last_node, next_node, list_edges):
    for edge in list_edges:
        if ([edge["node_src"], edge["node_dst"]] == [last_node, next_node]) or \
          ([edge["node_dst"], edge["node_src"]] == [last_node, next_node]):
            return edge


def estimate_sites_evacuation_times(list_sites, list_edges):
    for site in list_sites:
        total_length = 0
        min_capacity = sys.maxsize

        first_edge = find_edge(site["id"], site["node1"], list_edges)
        total_length += first_edge["length"]
        if first_edge["capacity"] < min_capacity:
            min_capacity = first_edge["capacity"]

        for k in range(site["number_of_nodes_in_path"]-1):
            current_edge = find_edge(site["node"+str(k+1)], site["node"+str(k+2)], list_edges)
            total_length += current_edge["length"]
            if current_edge["capacity"] < min_capacity:
                min_capacity = current_edge["capacity"]

        total_evacuation_time = site["pop"]/min_capacity + total_length
        site["estimated_evacuation_time"] = total_evacuation_time
    return list_sites
