#!/usr/bin/python

class PhysicalConfig(object):
    def __init__(self, num_servers = 0, num_racks = 0, which_rack = [], traffic_cost_matrix = [], constraint_cpu = [], constraint_memory = [], num_links = 0, link_capacity = [], link_occupation_matrix = [], link_user_racks = []):
        self.num_servers = num_servers
        self.num_racks = num_racks
        self.which_rack = which_rack
        self.traffic_cost_matrix = traffic_cost_matrix
        self.constraint_cpu = constraint_cpu
        self.constraint_memory = constraint_memory
        self.num_links = num_links
        self.link_capacity = link_capacity
        self.link_occupation_matrix = link_occupation_matrix
        self.link_user_racks = link_user_racks

        # compute rack users using which_rack
        self.rack_user_servers = [ [] for k in range(num_racks) ]
        for k in range(num_servers):
            self.rack_user_servers[which_rack[k]].append(k)

        #print self.rack_user_servers
        #print self.link_user_racks
