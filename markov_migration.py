#!/usr/bin/python
# OpenStack virtual machine placement
# try to use aprroximated markov chain to migrate a VM
# the algorithm can be found in <Joint VM Placement and Routing for Data Center Traffic Engineering>

from physical_configuration import PhysicalConfig


def migrate_policy(num_vms, vm_consumption, vm_traffic_matrix, original_placement, physical_config):
    print '!'

    # get vms on each server
    server_user_vms = [ [] for k in range(physical_config.num_servers) ]
    for vm in range(num_vms):
        server_user_vms[original_placement[vm]].append(vm)

    # get the workload on each link(edge)
    link_workload = compute_traffic_over_link(num_vms, vm_traffic_matrix, original_placement, physical_config)
    # find the most-congested edge (currently we consider absolute most-congestion)
    edge = 0
    edge_traffic = 0
    for k in range(physical_config.num_links):
        if link_workload[k] > edge_traffic:
            edge, edge_traffic = k, link_workload[k]
    #print edge, edge_traffic

    # gather all vms that uses the edge
    candidate_vms = []
    candidate_servers = []
    candidate_racks = physical_config.link_user_racks[edge]
    for rack in candidate_racks:
        candidate_servers += physical_config.rack_user_servers[rack]
    #print candidate_servers
    for server in candidate_servers:
        candidate_vms += server_user_vms[server]

    print candidate_vms

    





def compute_traffic_over_link(num_vms, vm_traffic_matrix, original_placement, physical_config):
    link_workload = [0.0 for k in range(physical_config.num_links)]
    
    for k in range(num_vms):
        for i in range(k+1, num_vms):
            traffic_between_pair = vm_traffic_matrix[k][i]
            rack_k = physical_config.which_rack[original_placement[k]]
            rack_i = physical_config.which_rack[original_placement[i]]
            used_links = physical_config.link_occupation_matrix[rack_k][rack_i]
            #print used_links

            for link in used_links:
                link_workload[link] += traffic_between_pair

    #print link_workload
    return link_workload



