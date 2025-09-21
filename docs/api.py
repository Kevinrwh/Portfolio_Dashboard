import requests as rq
import json
import os

# Define a custom exception class
class KeyNotFoundError(Exception):
    pass

PRO_URL = "https://pro-api.coingecko.com/api/v3/"

# Get API key from environment variable only (secure best practice)
def get_key():
    key = os.getenv('CG_PRO_KEY')
    if key is not None:
        return key
    
    raise KeyNotFoundError(
        "API key is not available! Please set the CG_PRO_KEY environment variable.\n"
        "Example: export CG_PRO_KEY='your_api_key_here'\n"
        "Or create a .env file with: CG_PRO_KEY=your_api_key_here"
    )

# Switch between demo and pro accounts
#use_demo={"accept": "application/json"}

use_pro = {
    "accept": "application/json",
    "x-cg-pro-api-key": get_key()
}