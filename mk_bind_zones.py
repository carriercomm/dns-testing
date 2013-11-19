#!/usr/bin/python

import os
import sys
import subprocess

num_attempts = int(sys.argv[1])
named_conf_path = "/etc/bind/named.conf.local"
zones_dir = "/var/cache/bind"

named_conf_str = "\nzone \"{0}\" {{\n\ttype master;\n\tfile \"{1}/{2}\";\n}};\n"
zone_str = """
$TTL	60 ; 24 hours could have been written as 24h or 1d
$ORIGIN {0}.
@  1D  IN	 SOA ns1.{0}.	hostmaster.{0}. (
			      2002022401 ; serial
			      3H ; refresh
			      15 ; retry
			      1w ; expire
			      3h ; minimum
			     )
       IN  NS     ns1.{0}. ; in the domain
; server host definitions
a    IN  A      192.168.0.1  ;name server definition     
b    IN  A      192.168.0.2  ;web server definition
c    IN  A      192.168.0.3
d    IN  A      192.168.0.4
e    IN  A      192.168.0.5
ns1  IN  A      192.168.0.6
"""

for i in range(num_attempts):
   zone = "example{0}.com".format(i)
   zone_filename = "{0}.zone".format(zone)
#   out = subprocess.check_output("./mkzone.sh {0} zone.cnf".format(zone), shell=True)
   out = zone_str.format(zone)
   zone_f = open("{0}/{1}".format(zones_dir, zone_filename), 'w')
   zone_f.write(out)
   named_f = open(named_conf_path, "a")
   named_f.write(named_conf_str.format(zone, zones_dir, zone_filename))
