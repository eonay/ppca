#!/usr/bin/python3
#
#
print("")
print("")
print("                               |")
print("                               S1                  <- core layer")
print("               ................|...............")
print("              |                               |")
print("              S2                              S3        <- distribution layer")
print("      ........|.......                ........|.......")
print("     |               |               |               |")
print("     S4              S5              S6              S7      <- access layer")
print("  ...|....        ...|....        ...|....        ...|....")
print(" |       |       |       |       |       |       |       |")
print(" H1      H2      H3      H4      H5      H6      H7      H8")
print("")
print("")


import os

from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.net import Mininet
from mininet.node import Host
from mininet.node import OVSKernelSwitch
from mininet.node import RemoteController

import manager_controllers

controller1='172.16.187.129'
controller2='172.16.187.130'

# verifica controladores apos os erros
def init_controllers():
    os.system("python3 check_controllers.py")

# cria topologia, inicia controles e integras nodes de rede
def topologyNetwork():
    net = Mininet(topo=None,
                  build=False,
                  ipBase='192.168.0.1/24')

    info('*** Adding controller\n')
    c0 = net.addController(name='c0',
                           controller=RemoteController,
                           ip='10.0.0.1',
                           protocol='tcp',
                           port=6633)

    info('*** Add switches\n')

    info('***** Add switch core\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

    info('***** Add switch distribution\n')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)

    info('***** Add switch access\n')
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)

    info('*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='192.168.0.1', defaultRoute='192.168.0.254')
    h2 = net.addHost('h2', cls=Host, ip='192.168.0.2', defaultRoute='192.168.0.254')
    h3 = net.addHost('h3', cls=Host, ip='192.168.0.3', defaultRoute='192.168.0.254')
    h4 = net.addHost('h4', cls=Host, ip='192.168.0.4', defaultRoute='192.168.0.254')
    h5 = net.addHost('h5', cls=Host, ip='192.168.0.5', defaultRoute='192.168.0.254')
    h6 = net.addHost('h6', cls=Host, ip='192.168.0.6', defaultRoute='192.168.0.254')
    h7 = net.addHost('h7', cls=Host, ip='192.168.0.7', defaultRoute='192.168.0.254')
    h8 = net.addHost('h8', cls=Host, ip='192.168.0.8', defaultRoute='192.168.0.254')

    info('*** Add links\n')
    net.addLink(s1, s2)
    net.addLink(s1, s3)

    net.addLink(s2, s4)
    net.addLink(s2, s5)

    net.addLink(s3, s6)
    net.addLink(s3, s7)

    net.addLink(s4, h1)
    net.addLink(s4, h2)

    net.addLink(s5, h3)
    net.addLink(s5, h4)

    net.addLink(s6, h5)
    net.addLink(s6, h6)

    net.addLink(s7, h7)
    net.addLink(s7, h8)

    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c0])
    net.get('s4').start([c0])
    net.get('s5').start([c0])
    net.get('s6').start([c0])
    net.get('s7').start([c0])

    info('*** Post configure switches and hosts\n')

    CLI(net)
    manager_controllers.stop_controllers()
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    manager_controllers.start_controllers()
    topologyNetwork()
    init_controllers()
