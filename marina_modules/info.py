import requests
import json

def get_info(host):

    headers = {
        'User-Agent': 'MARINA 2.0'
    }

    shodan_data = requests.get("https://andrax.thecrackertechnology.com/api/marina-info.php?ip={}".format(host), headers=headers)

    return json.loads(shodan_data.text)

    