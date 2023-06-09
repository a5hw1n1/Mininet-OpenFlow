from mininet.topo import Topo
from mininet.util import irange

class DatacenterBasicTopo( Topo ):
    "Datacenter topology with 4 hosts per rack, 4 racks, and a root switch"

    def build( self ):
        self.racks = []
        rootSwitch = self.addSwitch( 's1' )
        for i in irange( 1, 4 ):
            rack = self.buildRack( i )
            self.racks.append( rack )
            for switch in rack:
                self.addLink( rootSwitch, switch )

    def buildRack( self, loc ):
        "Build a rack of hosts with a top-of-rack switch"

        dpid = ( loc * 16 ) + 1
        switch = self.addSwitch( 's1r%s' % loc, dpid='%x' % dpid )

        for n in irange( 1, 4 ):
            host = self.addHost( 'h%sr%s' % ( n, loc ) )
            self.addLink( switch, host )

        # Return list of top-of-rack switches for this rack
        return [switch]


topos = {
    'dcbasic': DatacenterBasicTopo
}