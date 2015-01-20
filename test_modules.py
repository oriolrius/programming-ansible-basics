#!/usr/bin/python 
import ansible.runner
import ansible.playbook
import ansible.inventory
from ansible import callbacks
from ansible import utils
import json

# the fastest way to set up the inventory

# hosts list
hosts = ["10.11.12.66"]
# set up the inventory, if no group is defined then 'all' group is used by default
example_inventory = ansible.inventory.Inventory(hosts)

pm = ansible.runner.Runner(
    module_name = 'command',
    module_args = 'uname -a',
    timeout = 5,
    inventory = example_inventory,
    subset = 'all' # name of the hosts group 
    )

out = pm.run()

print json.dumps(out, sort_keys=True, indent=4, separators=(',', ': '))

