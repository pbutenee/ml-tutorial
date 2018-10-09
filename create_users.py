#!/usr/bin/python2

import subprocess as p
import os
import sys

if len(sys.argv) != 3:
    print "Usage %s <number_of_users> <password>" % sys.argv[0]
    sys.exit()

N = int(sys.argv[1])
PWD = sys.argv[2]

if N > 1000:
    raise Exception("Cannot create more than 1000 users (%d asked)" % N)

for ix in range(N):
    read, write = os.pipe()
    os.write(write, '%s\n%s' % (PWD, PWD))
    os.close(write)

    username = "user%03d" % ix
    print "Adding user " + username

    p.check_call(['adduser', '--gecos', '""', username], stdin=read)
    p.check_call(['cp', '-R', '/home/cs/tutorial', '/home/%s' % username])
    p.check_call(['chown', '-R', '%s:%s' % (username, username), '/home/%s/tutorial' % username])
