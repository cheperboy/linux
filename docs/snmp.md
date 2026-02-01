# SNMP

## tutorial

- [monitoring-mikrotik-with-grafana-and-prometheus-a-complete-setup-guide](https://tech.layer-x.com/monitoring-mikrotik-with-grafana-and-prometheus-a-complete-setup-guide/)
- [prometheus-monitoring-mikrotik](https://dernasherbrezon.com/en/posts/prometheus-monitoring-mikrotik/)
- [MIB Browser](https://mibs.observium.org/mib/MIKROTIK-MIB/#Power)

## stack

`sudo service snmp_exporter status`  
`sudo service prometheus status`  
`sudo service grafana-server status`  


## conf files

`/etc/snmp/snmp.conf`  
`/etc/prometheus/prometheus.yml`  
`/etc/systemd/system/snmp_exporter.service`  


## commands

`snmpwalk -v2c -c public 192.168.0.4 1.3.6.1.2.1.1`  
`snmpget -v2c -c public 192.168.0.88 .1.3.6.1.4.1.14988.1.1.3.100.1.2.13`  

## interfaces
http://localhost:9116/snmp  
http://localhost:9090/graph  
http://WAN_IP:3000/  


