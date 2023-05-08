# Mininet-OpenFlow
CS 553 Project on emulating OpenFlow on a mininet

Setup
The Mininet VM is meant to speed up Mininet installation. The first step is to Download the Mininet VM on a virtualization program, VirtualBox. Sign in as user mininet with password mininet. Once in the system, we can install all dependencies including Open vSwitch as well as the additions like the OpenFlow wireshark dissector using command:
mininet@mininet-vm:~$ ./util/install.sh -s ./build/ -a

Then install Ryu Controller Using pip3:
mininet@mininet-vm:~$sudo pip3 install ryu

After successful installation, we are ready to build topologies using an RYU controller, which supports OpenFlow protocol and measure network performance metrics across devices.

It is also possible to ssh into our mininet-vm from a host machine terminal. This proved useful in our experiments. 
Grab the ip of the mininet-vm using ifconfig on the mininet terminal and ssh from a host terminal:
ssh -Y mininet@<ip>

Running the RYU controller:
In another new terminal and run a simple switch controller.
mininet@mininet-vm:~$ryu-manager ryu.app.simple_switch

After starting up the controller, we will be able to have the nodes in the topology communicate and measure network characteristics.

To view control traffic using the OpenFlow Wireshark dissector, we need to start wireshark in another terminal:
mininet@mininet-vm:~$wireshark
When the window opens, choose to capture the loopback interface :lo four our experiments.
  
Test a simple topology using the command
mininet@mininet-vm:~$sudo mn --topo=minimal --switch ovsk,protocols=OpenFlow13 --controller remote,ip=127.0.0.1 --test none
  
To use our custom toplogies, you will need to copy the python files from your host machine to the vm. An scp command here is useful. Used like from host terminal:
scp /location_to_file_on_host/largeNetwork.py mininet@mininet-vm:/home/mininet/location_on_vm

To test the topology, you will use the python class in the mn command like:
mininet@mininet-vm:~$sudo mn --custom largeNetwork.py --topo largeNet  --switch ovsk,protocols=OpenFlow13 --controller remote --test none
  
Using the above command with the --test none parameter, the network will be built, the ryu controller, switches, hosts, links added and configured, and finally dismantled.
  
Running the above commadn without the test argument will create the network, ready for us to use the mininet.
  
In the mininet, to see all the nodes using the nodes command:
mininet> nodes

We can see information about links using the net command:
mininet> net
  
To dump all information about nodes using the dump command:
mininet> dump
  
To check connectivity between all nodes:
mininet> pingall

We now have a mininet we can use to perform our experiments!
