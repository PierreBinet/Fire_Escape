import solution_checker


def find_solution(number_of_sites, list_sites, list_edges):
    date_blocked_sites = []
    while len(date_blocked_sites) < number_of_sites:
        for site in list_sites:
            if site not in date_blocked_sites:
                if list_sites[site]["evacuation_start_date"] > 0:
                    list_sites[site]["evacuation_start_date"] -= 1
                    valid = solution_checker.solution_is_valid(list_sites, list_edges)
                    if not valid:
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
                    original_rate= list_sites[site]["evacuation_rate"]
                    while not valid:
                        if list_sites[site]["evacuation_rate"] > 1:
                            list_sites[site]["evacuation_rate"] -= 1
                        else:
                            list_sites[site]["evacuation_rate"] = original_rate
                            list_sites[site]["evacuation_start_date"] += 1
                            rate_blocked_sites.append(site)
                            break
                        valid = solution_checker.solution_is_valid(list_sites, list_edges)
                    rate_blocked_sites.append(site)
                else:
                    rate_blocked_sites.append(site)
                    #ICI rajouter condition pour diminuer rate pour secteur en conflits

    date_blocked_sites = []
    while len(date_blocked_sites) < number_of_sites:
        for site in list_sites:
            if site not in date_blocked_sites:
                if list_sites[site]["evacuation_start_date"] > 0:
                    list_sites[site]["evacuation_start_date"] -= 1
                    valid = solution_checker.solution_is_valid(list_sites, list_edges)
                    if not valid:
                        list_sites[site]["evacuation_start_date"] += 1
                        date_blocked_sites.append(site)
                else:
                    date_blocked_sites.append(site)
