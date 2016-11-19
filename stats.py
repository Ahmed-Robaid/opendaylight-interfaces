import httplib2
import json
#The docs are staright forward - https://wiki.opendaylight.org/view/OpenDaylight_Controller:REST_Reference_and_Authentication

req = httplib2.Http(".cache")
req.add_credentials('admin', 'admin')

response, content = req.request('http://10.55.17.20:8080/controller/nb/v2/statistics/default/flow', "GET")
allFlowStats = json.loads(content)
flowStats = allFlowStats['flowStatistics']
for fs in flowStats:
	print "\nSwitch ID : " + fs['node']['id']
	print '{0:8} {1:8} {2:5} {3:15}'.format('Count', 'Action', 'Port', 'DestIP')
	for aFlow in fs['flowStat']:
		count = aFlow['packetCount']
		actions = aFlow['flow']['actions'] 
		actionType = ''
		actionPort = ''
		if(type(actions) == type(list())):
			actionType = actions[1]['type']
			actionPort = actions[1]['port']['id']
		else:
			actionType = actions['type']
			actionPort = actions['port']['id']
		dst = aFlow['flow']['match']['matchField'][0]['value']
		print '{0:8} {1:8} {2:5} {3:15}'.format(count, actionType, actionPort, dst)