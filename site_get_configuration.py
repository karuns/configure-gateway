import sys
from pprint import pprint
import logging

#now we will Create and configure logger
logging.basicConfig(filename="data/log.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

#Let us Create an object
logger=logging.getLogger()
logger.setLevel(logging.INFO)

csv_filename = "data/input_file.csv"
central_filename = "data/auth/input_token_only.json"

# Get instance of ArubaCentralBase from the central_filename
from pycentral.workflows.workflows_utils import get_conn_from_file, get_file_contents
input_args = get_file_contents(filename=central_filename)

# Get customer id from the central_filename
if "central_info" not in input_args:
    sys.exit("exiting... Provide central_info in the file %s" % central_filename)
customer_id = input_args["central_info"]['customer_id']
central = get_conn_from_file(filename=central_filename)


# Testing
# GET groups from Aruba Central
# apiPath = "/configuration/v2/groups"
# apiMethod = "GET"
# apiParams = {
#     "limit": 20,
#     "offset": 0
# }
# base_resp = central.command(apiMethod=apiMethod,
#                             apiPath=apiPath,
#                             apiParams=apiParams)
# pprint(base_resp)


# Setup sites
from config_helper import siteSettingsFromCsv, siteGetSettingsFromCsv
siteGetSettingsFromCsv(
    conn=central,
    csv_filename=csv_filename,
    customer_id=customer_id,
    logger=logger
)




