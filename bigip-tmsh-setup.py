#!/usr/bin/env python

import requests

#Create partition
url = "https://10.1.20.10/mgmt/tm/auth/partition"

payload = "{\n\t\"name\": \"kubernetes\",\n    \"defaultRouteDomain\": 0\n\t\n}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic YWRtaW46YWRtaW4=",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

print(response.text)

#Create vxlan profile
url = "https://10.1.20.10/mgmt/tm/net/tunnels/vxlan"

payload = "{\n    \"name\": \"fl-vxlan\",\n    \"partition\": \"Common\",\n    \"defaultsFrom\": \"/Common/vxlan\",\n    \"encapsulationType\": \"vxlan\",\n    \"floodingType\": \"none\",\n    \"port\": 8472\n}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic YWRtaW46YWRtaW4=",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

print(response.text)

#Create vxlan tunnel
url = "https://10.1.20.10/mgmt/tm/net/tunnels/tunnel/"

payload = "{\n    \"name\": \"fl-vxlan\",\n    \"partition\": \"Common\",    \n    \"description\": \"Flannel vxlan tunnel for kubernetes cluster deployment\",\n    \"autoLasthop\": \"default\",\n    \"idleTimeout\": 300,\n    \"key\": 1,\n    \"localAddress\": \"10.1.20.10\",\n    \"mtu\": 0,\n    \"profile\": \"/Common/fl-vxlan\",\n    \"usePmtu\": \"enabled\"\n}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic YWRtaW46YWRtaW4=",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

print(response.text)

#Create Flannel self-IP
import requests

url = "https://10.1.20.10/mgmt/tm/net/self"

payload = "{\n    \"name\": \"10.244.20.10\",\n    \"description\": \"IP address to communicate on the Flannel kubernetes network\",\n    \"partition\": \"Common\",\n    \"address\": \"10.244.20.10/16\",\n    \"floating\": \"disabled\",\n    \"inheritedTrafficGroup\": \"false\",\n    \"trafficGroup\": \"/Common/traffic-group-local-only\",\n    \"unit\": 0,\n    \"vlan\": \"/Common/fl-vxlan\"\n}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic YWRtaW46YWRtaW4=",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

print(response.text)
