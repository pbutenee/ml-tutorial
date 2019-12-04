#!/usr/bin/python3

import subprocess as p
import os
import sys

if len(sys.argv) != 3:
    print(f"Usage {sys.argv[0]} <number_of_users> <password>")
    sys.exit()

N = int(sys.argv[1])
PWD = str(sys.argv[2])

if N > 1000:
    raise Exception(f"Cannot create more than 1000 users ({N} asked)")

for ix in range(N):
    read, write = os.pipe()
    os.write(write, str.encode(f'{PWD}\n{PWD}'))
    os.close(write)

    username = f"user{ix:03}"
    print(f"Adding user {username}")

    p.check_call(['adduser', '--gecos', '""', username], stdin=read)
    p.check_call(['cp', '-R', '/home/cs/tutorial', f'/home/{username}'])
    p.check_call(['chown', '-R', f'{username}:{username}', f'/home/{username}/tutorial'])
