def parser_data(path):
    with open(path, 'r') as fp:

        next(fp)  # first line ignored (comment)
        line = fp.readline()  # line number 2 : sites information line

        tab = line.split(' ')
        number_of_sites = int(tab[0])
        safe_node_id = int(tab[1])

        # print("number of sites : "+str(number_of_sites))
        # print("safe node id : "+str(safe_node_id))

        list_sites = []  # creation of a list to put sites in

        needed_edges = []

        for i in range(number_of_sites):  # lines that describe sites on by one
            line = fp.readline()
            tab = line.split(' ')
            site = {"id": int(tab[0]), "pop": int(tab[1]), "max_rate": int(tab[2]), "number_of_nodes_in_path": int(tab[3])}
            last_node = int(tab[0])
            for k in range(site["number_of_nodes_in_path"]):
                next_node = int(tab[4+k])
                site["node"+str(k+1)] = next_node
                direct_path = [last_node, next_node]
                if direct_path not in needed_edges:
                    needed_edges.append(direct_path)
                last_node = next_node
            list_sites.append(site)

        # print(needed_edges)

        # print(list_sites)

        next(fp)  # line ignored (comment)
        line = fp.readline()

        tab = line.split(' ')
        number_of_edges = int(tab[1])

        list_edges = []

        for i in range(number_of_edges):
            line = fp.readline()
            tab = line.split(' ')
            edge = {"node_src": int(tab[0]), "node_dst": int(tab[1]), "due_date": int(tab[2]), "length": int(tab[3]),
                    "capacity": int(tab[4])}
            if ([edge["node_src"], edge["node_dst"]] in needed_edges) or ([edge["node_dst"], edge["node_src"]] in
                                                                          needed_edges):
                list_edges.append(edge)

        print(list_edges)

        return number_of_sites, list_sites, safe_node_id, number_of_edges, list_edges










