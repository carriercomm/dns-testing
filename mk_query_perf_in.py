#!/usr/bin/python

import sys

domain = "example"
ext = ".com"
r_type = "A"
num_recs = int(sys.argv[1])
filename = sys.argv[2]

f = open(filename, 'w')
for i in range(num_recs):
    f.write("a.{0}{1}{2} {3}\n".format(domain, i, ext, r_type))
    f.write("b.{0}{1}{2} {3}\n".format(domain, i, ext, r_type))
    f.write("c.{0}{1}{2} {3}\n".format(domain, i, ext, r_type))
    f.write("d.{0}{1}{2} {3}\n".format(domain, i, ext, r_type))
    f.write("e.{0}{1}{2} {3}\n".format(domain, i, ext, r_type))
    f.write("ns1.{0}{1}{2} {3}\n".format(domain, i, ext, r_type))
