import requests
import re

def get_asn(company_name):
    url = f'https://rest.db.ripe.net/search.json?query-string=AS-{company_name}'
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    list_asn = response.json()["objects"]["object"][0]["attributes"]["attribute"]
    as_name = []
    for asn in list_asn:
        if asn.get("referenced-type")=="aut-num":
            as_name.append(re.sub('[^0-9]','', asn.get("value")))
    print("="*100)
    print(company_name.upper() + f" registered ASN list:\n{', '.join(as_name)}")
    print("="*100)
    return as_name

