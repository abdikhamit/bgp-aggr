# bgp-aggr
usage: ./bgp-aggr.py


The task is to write a python script that will receive as input
a full BGP table and pull out from it only networks belonging to AS
of company REG.RU(or any other). Next, these networks need to be aggregated to the maximum
possible prefix and written to mysql database. 
- The full BGP table is retrieved from http://routeviews.org/
- The list of AS is retrieved from ripe.net 

Requirements:
- Linux (must be linux, as full bgp table file is extracted by the OS)
- Python3
- pip install netaddr
