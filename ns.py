#!/usr/bin/python
import sys
import os
import ConfigParser
from unshare import *

class NS:
    
    def __init__(self):
        try
        conf-parser = ConfigParser.RawConfigParser()
        conf-parser.read(".ns-conf")
        #add any conf for namespaces
        except ValueError as e:
            print e
            
    def unshare(pipe,tenant_id, vm_id):
        pipe1, pipe2 = pipe;
        pipe2.close();
        #create namespace
        new_netns = unshare(CLONE_NEWNET)
        pipe1.send("unshared")
        line = pipe1.recv()
        if line != "go" :
            exit(1)
        for intf in xrange(1,3):
        guest_iface="ve-%04x-%03x-%d" % (tenant_id,vm_id,intf)
        mac = "02:c0:%02x:%02x:%02x:%02x" % ( ((tenant_id & 0xff00) >> 8), (tenant_id & 0x00ff), (vm_id & 0x00ff), ((vm_id & 0x0f00) >> 4)+ intf )
        cmd = "ifconfig i%s hw ether %s" % (guest_iface,mac)
        shell_pid = subprocess.Popen(cmd, shell=True)
        shell_pid.wait()
        print cmd
        cmd = "ifconfig i%s up" % guest_iface
        shell_pid = subprocess.Popen(cmd, shell=True)
        shell_pid.wait()
        print cmd
        os.system("/bin/bash")
        
        #set and ip?
            
    def CreateNamespace(tenant_id, vm_id):
        vm_id = vm_id
        tenant_id = tenant_id
        (pipe1, pipe2) = multiprocessing.Pipe()
        p = multiprocessing.Process(target=unshare, args=((pipe1, pipe2),tenant_id, vm_id))
        p.start()
        pipe1.close()

        line = pipe2.recv()

        #make sure net namespace has unshared
        if line != "unshared" :
            exit(1)
        ##
        pipe2.send("go")
        ##
        print "Done"
        
    def DelNamespace():
        #