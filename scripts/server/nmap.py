#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
-----
using python on ubuntu 24.04:
sudo apt install -y python3-virtualenv
virtualenv pyenv
source pyenv/bin/activate
then use pip install somelibrary
-----
requirements for this script:
sudo apt install nmap
pip install python3-nmap
-----
Usage
the script should be run as root
using sudo you need to  explicitely call the venv python like this
sudo /home/.../pyenv/bin/python3 script.py
-----
Exemple de script pour scanner les ports les plus courants sur un hôte
"""
from tabulate import tabulate
import nmap3
import json
FILE = "temp.json"
SUBNET = "192.168.1.1/24"

def read_json():
  with open(FILE, "r") as f: 
    return (json.load(f))

def write_json(data): 
  with open(FILE, "w") as f: 
    f.write(json.dumps(data, indent=2))

def print_result(result): 
  print(json.dumps(result, indent=2))

def save_result(result): 
  write_json(result)

def nmap_no_portscan():
  nmap = nmap3.NmapHostDiscovery()
  result = nmap.nmap_no_portscan(SUBNET)
  return (result)

def scan_top_ports(ip):
  nmap = nmap3.Nmap()
  result = nmap.scan_top_ports(ip)
  return (result)

def scan():
  result = nmap_no_portscan()   
  return (result)

def print_no_portscan(result):
  result = read_json()
  #print_result(result)
  table = [["name", "ip", "mac", "vendor"]]
  for ip in result:
    try:
      host = result.get(ip)
      if ((type(host) is not list) and (host.get("macaddress") is not None)):
        state = host.get("state").get("state")
        macaddress = host.get("macaddress")
        name = ""
        #if ((type(host) is not list) and (host.get("macaddress") is not None))
        for item in host.get("hostname"): 
          name = name + item.get("name") 
          #if (hostname) : host.get("hostname").get("name")
        if state == "up":
          row = [name, ip, macaddress.get("addr"), macaddress.get("vendor") ]
          #print(f'{name} {ip} {macaddress.get("addr")} {macaddress.get("vendor")}')
        table.append(row)
    except Exception as e:
      print ("EXCEPTION \n"+str(e))
  print(tabulate(table, headers='firstrow'))

result = nmap_no_portscan()
save_result(result)
print_no_portscan(result)

#nmap = nmap3.Nmap()

# -sn  192.168.1.0/24
#result = nmap.scan_top_ports("localhost /24")
#result = nmap.scan_top_ports("scanme.nmap.org")
#result  = nmap.NmapHostDiscovery("192.168.1.1 /24")
#result = nmap.nmap_list_scan("192.168.1.1/24")
#result = nmap.nmap_subnet_scan("192.168.1.1/24")
#nmap = nmap3.NmapHostDiscovery()
#result = nmap.nmap_no_portscan("192.168.1.1/24")


