import time
from pprint import pprint
from zapv2 import ZAPv2
import os
import subprocess
import uuid
import json

apikey=str(uuid.uuid4())

print('Starting ZAP ...')
subprocess.Popen(['zap.sh','-daemon', '-port', '8081', '-config', 'api.key='+apikey],stdout=open(os.devnull,'w'))
print('Waiting for ZAP to load, 10 seconds ...')
time.sleep(20)

target = 'http://178.62.36.148:9090/login'
zap = ZAPv2(apikey=apikey, proxies={'http': '127.0.0.1:8081', 'https': '127.0.0.1:8081'})

# Proxy a request to the target so that ZAP has something to deal with
print('Accessing target {}'.format(target))
zap.urlopen(target)
# Give the sites tree a chance to get updated
time.sleep(2)

print('Spidering target {}'.format(target))
scanid = zap.spider.scan(target)
# Give the Spider a chance to start
time.sleep(2)
while (int(zap.spider.status(scanid)) < 100):
    # Loop until the spider has finished
    print('Spider progress %: {}'.format(zap.spider.status(scanid)))
    time.sleep(2)

print ('Spider completed')

while (int(zap.pscan.records_to_scan) > 0):
      print ('Records to passive scan : {}'.format(zap.pscan.records_to_scan))
      time.sleep(2)

print ('Passive Scan completed')

print ('Active Scanning target {}'.format(target))
scanid = zap.ascan.scan(target)
while (int(zap.ascan.status(scanid)) < 100):
    # Loop until the scanner has finished
    print ('Scan progress %: {}'.format(zap.ascan.status(scanid)))
    time.sleep(5)

print ('Active Scan completed')

# Report the results

with open('zap-report.json', 'w') as ff:
    report = zap.core.alerts()
    ff.write(json.dumps(report))
#pprint (zap.core.alerts())

zap.core.shutdown()
