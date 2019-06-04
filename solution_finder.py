import solution_checker


def find_solution(number_of_sites, list_sites, list_edges, last_edge_index, list_original):
    # the finder takes a solution that is a valid (capacity speaking) upper limit
    # the first part of the finder shrinks tha start dates so it
    date_blocked_sites = []
    while len(date_blocked_sites) < number_of_sites:
        for site in list_sites:
            if site not in date_blocked_sites:
                if list_sites[site]["evacuation_start_date"] > 0:
                    list_sites[site]["evacuation_start_date"] -= 1
                    valid, valid_cap, valid_due_date, evacuation_total_time = \
                        solution_checker.solution_is_valid(list_sites, list_edges, last_edge_index)
                    if not valid_cap:
                        list_sites[site]["evacuation_start_date"] += 1
                        date_blocked_sites.append(site)
                else:
                    date_blocked_sites.append(site)

    rate_blocked_sites = []
    while len(rate_blocked_sites) < number_of_sites:
        for site in list_sites:
            if site not in rate_blocked_sites:
                if list_sites[site]["evacuation_start_date"] > 0:
                    list_sites[site]["evacuation_start_date"] -= 1
                    valid = solution_checker.solution_is_valid(list_sites, list_edges)
                    while not valid:
                        for sites in list_sites:
                            if list_sites[sites]["evacuation_rate"] > 1:
                                list_sites[sites]["evacuation_rate"] -= 1
                            else:
                                list_sites[site]["evacuation_rate"] = list_original[site][1]
                                list_sites[site]["evacuation_start_date"] = list_original[site][2]
                                rate_blocked_sites.append(site)
                        valid = solution_checker.solution_is_valid(list_sites, list_edges)
                rate_blocked_sites.append(site)
                    #ICI rajouter condition pour diminuer rate pour secteur en conflits

    # date_blocked_sites = []
    # while len(date_blocked_sites) < number_of_sites:
    #     for site in list_sites:
    #         if site not in date_blocked_sites:
    #             if list_sites[site]["evacuation_start_date"] > 0:
    #                 list_sites[site]["evacuation_start_date"] -= 1
    #                 valid = solution_checker.solution_is_valid(list_sites, list_edges)
    #                 if not valid:
    #                     list_sites[site]["evacuation_start_date"] += 1
    #                     date_blocked_sites.append(site)
    #             else:
    #                 date_blocked_sites.append(site)
