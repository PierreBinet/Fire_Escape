import solution_checker


def find_solution(number_of_sites, list_sites, list_edges, last_edge_index, list_original):
    # the finder takes a solution that is a valid (capacity speaking) upper limit
    # the first part of the finder shrinks tha start dates so it
    date_blocked_sites = []
    rate_blocked_sites = []

    valid, valid_cap, _, best_solution_so_far, list_overcap, list_overdue, list_cap_filling\
        = solution_checker.solution_is_valid(list_sites, list_edges, last_edge_index)
    # print("VALID BEGIN : " + str(valid_cap))

    best_solution_so_far = compress_dates(date_blocked_sites, number_of_sites, list_sites, list_edges, last_edge_index, best_solution_so_far)
    decrease_rate_to_start_earlier(list_sites, list_edges, last_edge_index)
    # best_solution_so_far = adjust_rates(rate_blocked_sites, number_of_sites, list_sites, list_edges, last_edge_index, list_original, best_solution_so_far)


def compress_dates(date_blocked_sites, number_of_sites, list_sites, list_edges, last_edge_index, best_solution_so_far):
    we_continue = True
    while we_continue:
        we_continue = False
        for site in list_sites:
            list_sites[site]["evacuation_start_date"] -= 1
            valid, valid_cap, _, tmp_solution, list_overcap, list_overdue, list_cap_filling\
                = solution_checker.solution_is_valid(list_sites, list_edges, last_edge_index)

            if valid_cap and tmp_solution < best_solution_so_far:
                best_solution_so_far = tmp_solution
                we_continue = True
                print("START DATE COMPRESSED")
            elif list_sites[site]["evacuation_start_date"] < 0:
                list_sites[site]["evacuation_start_date"] += 1

    return best_solution_so_far


def find_parent_site(edge_index, list_edges):
    current_id = edge_index
    return_list = []
    parent_left_to_check = []
    parent_left_to_check.append(current_id)
    while parent_left_to_check:
        current_id = parent_left_to_check.pop()
        if list_edges[str(current_id)]["is_a_site"]:
            return_list.append(current_id)
        for parent in list_edges[str(current_id)]["parent"]:
            parent_left_to_check.append(parent)

    return return_list


def decrease_rate_parent_site(edge_index, list_edges, list_sites):
    list_parent_sites = find_parent_site(edge_index, list_edges)
    for site in list_parent_sites:
        if list_sites[str(site)]["evacuation_rate"] > 0:
            list_sites[str(site)]["evacuation_rate"] -= 1


def decrease_start_one_site(site_index, list_sites, list_edges, last_edge_index):
    if list_sites[site_index]["evacuation_start_date"] > 0:
        list_sites[site_index]["evacuation_start_date"] -= 1
    valid, valid_cap, valid_due_date, _, list_overcap, _, list_cap_filling\
        = solution_checker.solution_is_valid(list_sites, list_edges, last_edge_index)
    while not valid_cap:
        for edge in list_overcap:
            decrease_rate_parent_site(edge, list_edges, list_sites)
            valid, valid_cap, valid_due_date, _, _, _, list_cap_filling \
                = solution_checker.solution_is_valid(list_sites, list_edges, last_edge_index)


def decrease_rate_to_start_earlier(list_sites, list_edges, last_edge_index):
    # valid, valid_cap, valid_due_date, evacuation_total_time, list_overcap, list_overdue, list_cap_filling = \
    #     solution_checker.solution_is_valid(list_sites, list_edges, last_edge_index)
    # if valid_cap:
    #     for t in range(0, 5):
    #
    for site in list_sites:
        decrease_start_one_site(site, list_sites, list_edges, last_edge_index)


def debug(list_sites, best_solution_so_far, valid_cap):
    for site in list_sites:
        print("Site nb " + str(list_sites[site]["id"]) + " rate = " + str(list_sites[site]["evacuation_rate"]))
    print("BEST SOLUTION SO FAR : " + str(best_solution_so_far))
    print("SOLUTION IS VALID : " + str(valid_cap))


# def adjust_rates(rate_blocked_sites, number_of_sites, list_sites, list_edges, last_edge_index, list_original, best_solution_so_far):
#     for site in list_sites:
#         it_was_useful = False
#         list_sites[site]["evacuation_rate"] -= 1
#         for other_site in list_sites:
#             it_was_useful = False
#             if other_site != site and list_sites[other_site]["evacuation_rate"] > 1:
#                 list_sites[other_site]["evacuation_rate"] -= 1
#                 valid, valid_cap, _, tmp_solution, list_overcap, list_overdue, list_cap_filling =\
#                     solution_checker.solution_is_valid(list_sites, list_edges, last_edge_index)
#
#                 debug(list_sites, best_solution_so_far, valid_cap)
#
#                 if valid_cap and tmp_solution <= best_solution_so_far:
#                     best_solution_so_far = tmp_solution
#                     print("RATE DECREMENTED")
#                     it_was_useful = True
#                     break
#                 elif not valid_cap:
#                     list_sites[other_site]["evacuation_rate"] -= 1
#             elif list_sites[other_site]["evacuation_rate"] <= 1:
#                 list_sites[site]["evacuation_rate"] = list_original[site][0]
#
#         if it_was_useful:
#             find_solution(number_of_sites, list_sites, list_edges, last_edge_index, list_original)
#         if not it_was_useful:
#             list_sites[site]["evacuation_rate"] += 1
#
#     print(best_solution_so_far)
#     return best_solution_so_far


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


# def compress_start_dates(date_blocked_sites, number_of_sites, list_sites, list_edges, last_edge_index, best_solution_so_far):
#     tmp_solution = sys.maxsize
#     while len(date_blocked_sites) < number_of_sites:
#         for site in list_sites:
#             if site not in date_blocked_sites:
#                 if list_sites[site]["evacuation_start_date"] > 0:
#                     list_sites[site]["evacuation_start_date"] -= 1
#                     valid, valid_cap, _, tmp_solution = \
#                         solution_checker.solution_is_valid(list_sites, list_edges, last_edge_index)
#                     if not valid_cap:
#                         list_sites[site]["evacuation_start_date"] += 1
#                         date_blocked_sites.append(site)
#                 else:
#                     date_blocked_sites.append(site)
#     return best_solution_so_far


# def adjust_rate(rate_blocked_sites, number_of_sites, list_sites, list_edges, last_edge_index, list_original, best_solution_so_far):
#     tmp_solution = sys.maxsize
#     while len(rate_blocked_sites) < number_of_sites:
#         for site in list_sites:
#             if site not in rate_blocked_sites:
#                 if list_sites[site]["evacuation_start_date"] > 0:
#                     list_sites[site]["evacuation_start_date"] -= 1
#                     valid, valid_cap, _, _ = solution_checker.solution_is_valid(list_sites, list_edges, last_edge_index)
#                     while not valid_cap:
#                         for sites in list_sites:
#                             if list_sites[sites]["evacuation_rate"] > 1:
#                                 list_sites[sites]["evacuation_rate"] -= 1
#                             else:
#                                 list_sites[site]["evacuation_rate"] = list_original[site][0]
#                                 list_sites[site]["evacuation_start_date"] = list_original[site][1]
#                                 rate_blocked_sites.append(site)
#                         valid, valid_cap, _, _ = solution_checker.solution_is_valid(list_sites, list_edges, last_edge_index)
#                 rate_blocked_sites.append(site)
#                 # ICI rajouter condition pour diminuer rate pour secteur en conflits
#
#             if tmp_solution < best_solution_so_far:
#                 best_solution_so_far = tmp_solution
#
#     return best_solution_so_far