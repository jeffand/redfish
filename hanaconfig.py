#!/usr/bin/env python
from jinja2 import Environment, FileSystemLoader
import socket

ENV = Environment(loader=FileSystemLoader('./'))

# Init the dictionary
dict = {}

#dict = { 'fqdn_hostname' : 'hana106.lab1.riba.com', 'datacenter': 'lab1'}

dict['fqdn_hostname'] = socket.getfqdn()
dict['datacenter'] = socket.getfqdn().split('.')[1]


# Render template and print generated config to console
template = ENV.get_template("hana.text")
print template.render(dict)
