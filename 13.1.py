from ipaddress import *
for mask in range(33):
    net = ip_network(f'98.162.71.94/{mask}', 0)
    print(net, net.netmask)