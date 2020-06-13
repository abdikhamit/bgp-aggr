import os.path
import urllib.request
import re

def get_subnet_list(as_number,file):
    with open(file) as file_data:
        subnet_list = []
        regex = as_number + "\s(i|e|\?)"
        for line in file_data:
            if re.search(regex, line):
                subnet = line.split()[1]
                subnet_list.append(subnet) if subnet not in subnet_list else subnet_list
        return subnet_list


