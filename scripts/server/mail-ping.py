"""
This script ping LAN hosts, send email.
"""

from mailjet_rest import Client
import os
import socket
import requests

IP = 0
PING = 1

hosts = [
  ["192.168.0.4", -1],
  ["192.168.0.88", -1],
  ["192.168.0.6", -1],
  ["192.168.0.254", -1],
]

import urllib.request
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

#api_key = os.environ['api_key']
#api_secret = os.environ['api_secret']
api_key = 'api_key'
api_secret = 'api_secret'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

""" get WAN IP of this device""" 
def get_wan_ip():
  f = requests.request('GET', 'http://myip.dnsomatic.com')
  ip = f.text
  return ip

""" get LAN IP of this device""" 
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def create_message():
  body= ""
  body += "Ping results\n"
  for i in range(len(hosts)):
    body += hosts[i][IP] + " "
    if hosts[i][PING] !=0: 
      body += "ping FAILED\n"
    else:
      body += "ok\n"

  body += "\nLAN "+ get_ip() +"\nWAN "+get_wan_ip()+"\n"
  #print(body)

  emails = { 'Messages': 
  [
    {
    "From": {
      "Email": "TO BE REPLACE",
      "Name": "TO BE REPLACE"
    },
    "To": [
    {
      "Email": "TO BE REPLACE",
      "Name": "admin"
    }
    ],
    "Subject": "TO BE REPLACE",
    "TextPart": body,
    "HTMLPart": ""
    }]
  }
  return(emails)

def ping():
  flag_alert = False
  for i in range(len(hosts)):
    response = os.system("ping -c 1 " + hosts[i][IP])
    hosts[i][PING] = response # !=0 -> failed
    if response != 0: flag_alert = True # set flag if any fail to send mail
  if flag_alert == True : send_mail()
  #send_mail() # Always, even if ping ok.

def send_mail():
    content = create_message()
    result = mailjet.send.create(data=content)
    #print (result.status_code)
    #print (result.json())

ping()
