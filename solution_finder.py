import solution_checker

def find_solution(number_of_sites, list_sites, list_edges):
    list_blocked_sites = []
    while len(list_blocked_sites) < number_of_sites:
        for site in list_sites:
            if site not in list_blocked_sites:
                if list_sites[site]["evacuation_start_date"] > 0:
                    list_sites[site]["evacuation_start_date"] -= 1
                    valid = solution_checker.solution_is_valid(list_sites, list_edges)
                    if not valid:
                        list_sites[site]["evacuation_start_date"] += 1
                        list_blocked_sites.append(site)
                else:
                    list_blocked_sites.append(site)
