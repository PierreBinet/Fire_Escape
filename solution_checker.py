def solution_is_valid(number_of_sites, list_sites, safe_node_id, number_of_edges, list_edges):

    for site in list_sites:
        last_node = site["id"]
        for k in range(site["number_of_nodes_in_path"]):
            next_node = site["node" + str(k + 1)]
            edge = find_edge(last_node, next_node, list_edges)

            last_node = next_node


def find_edge(last_node, next_node, list_edges):
    for edge in list_edges:
        if ([edge["node_src"], edge["node_dst"]] == [last_node, next_node]) or \
          ([edge["node_dst"], edge["node_src"]] == [last_node, next_node]):
            return edge
