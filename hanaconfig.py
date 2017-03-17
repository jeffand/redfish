from jinja2 import Environment, FileSystemLoader
import socket

ENV = Environment(loader=FileSystemLoader('./'))

#with open("config.yaml") as _:
#    dict =  yaml.load(_)
dict = {}

#dict = { 'fqdn_hostname' : 'hana106.lab1.ariba.com', 'datacenter': 'lab1'}
#currentDatacenterName = socket.getfqdn().split('.')[1]
dict['fqdn_hostname'] = socket.getfqdn()
dict['datacenter'] = socket.getfqdn().split('.')[1]

# Print dictionary generated from yaml
print dict

# Render template and print generated config to console
template = ENV.get_template("hana.text")
print template.render(dict)
