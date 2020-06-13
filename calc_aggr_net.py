import re
import netaddr
from itertools import groupby

def get_subnet_list(as_number, file):
 
    with open(file) as file_data:
        subnet_list = []
        regex = as_number + "\s(i|e|\?)"
        for line in file_data:
            if re.search(regex, line):
                subnet = line.split()[1]
                subnet_list.append(subnet) if subnet not in subnet_list else subnet_list
        return subnet_list


def get_subnet_aggr(subnet_list):
 
    subnet_group = []
    subnet_aggr = []
    for key, group in groupby(subnet_list, lambda x: x.split('.')[0] + '.' + x.split('.')[1]):
        subnet_group.append(list(group))
 
    for subnets in subnet_group:
        if len(subnets) > 1:
            cidr = str(netaddr.spanning_cidr(subnets))
            subnet_aggr.append(cidr)
        else:
            subnet_aggr.append(subnets[0])
 
    return subnet_aggr
 
