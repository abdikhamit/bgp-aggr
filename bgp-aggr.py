from get_asn import get_asn
from calc_aggr_net import get_subnet_list
from calc_aggr_net import get_subnet_aggr
from get_rib_info import get_rib_info
from sqldb_update import SQL_CONNECT
from sqldb_update import SQL_UPDATE 

def main():
    print("\n")
    print("~~ RIPE Database Query ~~\n".center(100))
    company_name = input("\nEnter Company name to get list of registered BGP Autonomous System Numbers from RIPE Database: ")

    list_asn = get_asn(company_name)

    file_unzip = get_rib_info()

    SQL_CONNECT()
    print("\nCalculating aggregated list of subnets of each AS\nPlease wait....  it might take a while to process....\n")

    for asn in list_asn:
        subnet_list = get_subnet_list(asn, file_unzip)
        subnet_aggregated = get_subnet_aggr(subnet_list)
        print(f"List of aggregated subnets from AS{asn} to be written in BGP_ASN DB:\n{subnet_aggregated}")
        for i in subnet_aggregated:
            entities=(company_name,asn,i)
            SQL_UPDATE(entities)
        print('Data has been saved in BGP_ASN DB\n') 

if __name__=="__main__":
    main()
