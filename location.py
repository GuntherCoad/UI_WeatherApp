import requests
from config import GEO_SERVICE

# Not paying for an API so state is indeterminant.
def get_current_location():
    """Returns current location as a list[latitude,longitude]"""
    r = requests.get(GEO_SERVICE)
    cur_loc = r.text.split(',')
    return cur_loc
