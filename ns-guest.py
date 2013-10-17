#!/usr/bin/python
import os
import sys
import ConfigParser
import NS

if __name__ == '__main__':
    
    if len(sys.argv) != 4:
        print "usage: %s <create|delete> <tenant#> <vm#>" % sys.argv[0]
        
    cmd = sys.argv[1]
    tenant_id = int(sys.argv[2])
    vm_id = int(sys.argv[3])
    
    bridge_id = "br-int"
    ip_prefix = "192.168."
    
    if cmd = 'create':
        if NS.CreateNamespace(bridge_id,ip_prefix,tenant_id,vm_id) == 0:
        #create namespace (unshare/python-unshare)
        #add network / ports / attachments via quantum api -->(talks to) ovs-plugin

    #if == "connect"
    #attatch logical Viface with ovs-vsctl commands (del,add)

#if == "delete"
#delete the things