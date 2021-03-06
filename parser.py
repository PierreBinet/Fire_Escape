def is_a_site(list_edges, list_sites):
    for site in list_sites:
        list_edges[site]["is_a_site"] = True


def subject_parser(path):
    with open(path, 'r') as fp:

        next(fp)  # first line ignored (comment)
        line = fp.readline()  # line number 2 : sites information line

        tab = line.split(' ')
        number_of_sites = int(tab[0])
        safe_node_id = int(tab[1])

        list_sites = {}  # creation of a list to put sites in

        needed_edges = []

        for i in range(number_of_sites):  # lines that describe sites on by one
            line = fp.readline()
            tab = line.split(' ')
            site = {"id": int(tab[0]), "pop": int(tab[1]), "max_rate": int(tab[2]), "number_of_nodes_in_path":
                    int(tab[3])}
            last_node = int(tab[0])
            for k in range(site["number_of_nodes_in_path"]):
                next_node = int(tab[4+k])
                site["node"+str(k+1)] = next_node
                direct_path = [last_node, next_node]
                if direct_path not in needed_edges:
                    needed_edges.append(direct_path)
                last_node = next_node
            list_sites[str(site["id"])] = site

        next(fp)  # line ignored (comment)
        line = fp.readline()

        tab = line.split(' ')
        number_of_edges = int(tab[1])
        useful_edges = 0

        list_edges = {}

        last_edge_index = []

        for i in range(number_of_edges):
            line = fp.readline()
            tab = line.split(' ')
            parent = []

            if [int(tab[0]), int(tab[1])] in needed_edges:
                edge = {"node_src": int(tab[0]), "node_dst": int(tab[1]), "due_date": int(tab[2]),
                        "length": int(tab[3]), "capacity": int(tab[4]), "parent": parent, "checked_?": False,
                        "is_a_site": False}
                list_edges[str(edge["node_src"])] = edge
                useful_edges += 1

            elif [int(tab[1]), int(tab[0])] in needed_edges:
                edge = {"node_src": int(tab[1]), "node_dst": int(tab[0]), "due_date": int(tab[2]),
                        "length": int(tab[3]), "capacity": int(tab[4]), "parent": parent, "checked_?": False,
                        "is_a_site": False}
                list_edges[str(edge["node_src"])] = edge
                useful_edges += 1

        for edge in list_edges:  # parent assignments
            if list_edges[edge]["node_dst"] != safe_node_id:
                list_edges[str(list_edges[edge]["node_dst"])]["parent"].append(list_edges[edge]["node_src"])
            else:
                last_edge_index.append(list_edges[edge]["node_src"])

        is_a_site(list_edges, list_sites)

    return number_of_sites, list_sites, safe_node_id, useful_edges, list_edges, last_edge_index


def solution_parser(path):
    with open(path, 'r') as fp:

        # next(fp)  # first line ignored (comment)
        line = fp.readline()
        tab = line.split('\n')
        subject_filename = "InstancesInt/"+tab[0]+".full"

        number_of_sites, list_sites, safe_node_id, number_of_edges, list_edges, last_edge_index = subject_parser(subject_filename)

        line = fp.readline()
        tab = line.split(' ')
        number_of_sites_found = int(tab[0])

        for index in range(number_of_sites_found):
            line = fp.readline()
            tab = line.split(' ')
            site_index = str(tab[0])
            list_sites[site_index]["evacuation_start_date"] = int(tab[2])
            list_sites[site_index]["evacuation_rate"] = int(tab[1])

        line = fp.readline()
        tab = line.split(' ')
        valid_found = False
        if str(tab[0]) == "valid":
            valid_found = True

        line = fp.readline()
        tab = line.split('\n')
        evacuation_total_time = str(tab[0])

        return number_of_sites, list_sites, safe_node_id, number_of_edges, list_edges, last_edge_index, valid_found, evacuation_total_time
