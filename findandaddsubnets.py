import requests
import json
from requests.auth import HTTPBasicAuth

serverIP = '10.55.17.20'
port = '8080'
container = 'default'
user = 'admin'
password = 'admin'

def find_subnet(subnets, subnetName):
    allSubnets = '/controller/nb/v2/subnet/' + container + '/subnet/all'
    url = 'http://' + serverIP + ':' + port + allSubnets
    for subnet in subnets:
        if subnet['subnet'] == subnetName:
            return subnet
    return None

def add_subnet(name, subnet):
    url = 'http://10.55.17.20:8080/controller/nb/v2/subnet/' + container + '/subnet/' + name
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    payload = {
        "name" : name,
        "subnet" : subnet
            }
    try:
        r = requests.post(url, data=json.dumps(payload), headers = headers, auth=(user, password))
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print e
        return None
    else:
        print "subnet added"
        return json.dumps(payload)

allSubnets = '/controller/nb/v2/subnet/' + container + '/subnet/all'
url = 'http://' + serverIP + ':' + port + allSubnets
subnetquery = '10.2.2.254/24'
r = requests.get(url, auth=(user, password))
r.raise_for_status()
result = find_subnet(r.json()['subnetConfig'], subnetquery)
print result
print "Adding Subnet"
add_subnet('test3', '172.17.0.0/24')