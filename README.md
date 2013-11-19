dnsperformance
==============

Scripts to create many zone files.

On server with bind:

./mkzones [num_zones]

this well create zone files starting with example1.com to exampleX.com (where X is num_zones).
Each zone will have a, b, c, d, e, and ns1 A records. (i.e. a.example1.com, b.example1.com,...)
By all means make this configurable if this gets used a lot.

Creates zone files in /var/cache/bind and adds zones to /etc/bind/named.conf.local

zone2sql --gmysql --named-conf=/etc/bind/named.conf --verbose > pdns.sql

This requires pdns installed to get zone2sql.  Creates a sql script to run on a pdns mysql backend.  Copy pdns.sql to the powerdns server.

On server with pdns:

mysql -u <username> <pdns_database> -p < pdns.sql


On another server:

locate queryperf

./mk_query_perf_in [num_zones] [out_file]

This creates the input file query perf uses to make requests

./queryperf -d [out_file] -s [server_ip]

queryperf is in the BIND source code.  make install it.




