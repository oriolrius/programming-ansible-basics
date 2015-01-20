#!/usr/bin/python 
import ansible.runner
import ansible.playbook
import ansible.inventory
from ansible import callbacks
from ansible import utils
import json

### setting up the inventory

## first of all, set up a host (or more)
example_host = ansible.inventory.host.Host(
    name = '10.11.12.66',
    port = 22
    )
# with its variables to modify the playbook
example_host.set_variable( 'var', 'foo')

## secondly set up the group where the host(s) has to be added
example_group = ansible.inventory.group.Group(
    name = 'sample_group_name'
    )
example_group.add_host(example_host)

## the last step is set up the invetory itself
example_inventory = ansible.inventory.Inventory()
example_inventory.add_group(example_group)
example_inventory.subset('sample_group_name')

# setting callbacks
stats = callbacks.AggregateStats()
playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)

# creating the playbook instance to run, based on "test.yml" file
pb = ansible.playbook.PlayBook(
    playbook = "test.yml",
    stats = stats,
    callbacks = playbook_cb,
    runner_callbacks = runner_cb,
    inventory = example_inventory,
    check=True
    )

# running the playbook
pr = pb.run()  

# print the summary of results for each host
print json.dumps(pr, sort_keys=True, indent=4, separators=(',', ': '))
