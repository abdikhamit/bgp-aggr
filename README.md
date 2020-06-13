# bgp-aggr
usage: ./bgp-aggr.py


The task is to write a perl or python script that will receive input
full BGP table and pull out from it only networks belonging to AS
company REG.RU(or any other). Next, these networks need to be aggregated to the maximum
possible prefix and written to mysql database. Full BGP table is possible
take from the site http://routeviews.org/

Requirements:
- Linux (must be linux, as bgp table is extracted by the OS)
- Python3
- pip install netaddr
