import sys
from pprint import pprint
from pycentral.base import ArubaCentralBase

def siteSettingsFromDict(conn, site_list, customer_id: str, command_body):
    path = "/caasapi/v1/exec/cmd"
    for site_data in site_list:
        group = site_data['group']
        mac_address = site_data['mac_address']

        params = {
            "cid": customer_id,
            "group_name": f"{group}/{mac_address}"
        }

        conn.command(apiMethod="POST", apiPath=path, apiParams=params, apiData=command_body)
        print("Pushed the following Config to Central:")
        print(command_body)




central = ArubaCentralBase(central_info=central_info,
                           ssl_verify=True)
apiPath = "/configuration/v2/groups"
apiMethod = "GET"
apiParams = {
    "limit": 20,
    "offset": 0
}
base_resp = central.command(apiMethod=apiMethod,
                            apiPath=apiPath,
                            apiParams=apiParams)
pprint(base_resp)
customer_id = central_info['customer_id']




siteSettingsFromDict(
    conn=central,
    site_list=input_dict,
    customer_id=customer_id,
    command_body=command_body
)




