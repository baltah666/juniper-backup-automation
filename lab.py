from jnpr.junos import Device
from pprint import pprint
import json

inventory = [
        "172.17.0.2"
    ]

list_of_device_output = []
for each_hostname in inventory:
    with Device(host=each_hostname, user='root', password='juniper123') as network_device:
        try:
            show_version = network_device.rpc.get_software_information({'format':'json'})
            payload = {'hostname': each_hostname, 'payload': show_version}
            list_of_device_output.append(payload)
            pprint('Completed request on device ' + str(each_hostname))
        except:
            pass

pprint(list_of_device_output)
