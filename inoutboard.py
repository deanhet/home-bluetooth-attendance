#!/usr/bin/python

import bluetooth
import time
import os
import signal
import subprocess
import sys

# Ignore SIGCHLD
# This will prevent zombies
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

print "In/Out Board"

DEVNULL = open(os.devnull, 'wb')

while True:
    print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())

    deanHome = bluetooth.lookup_name('B8:53:AC:38:4F:25', timeout=5)
    sarahHome = bluetooth.lookup_name('28:ED:6A:B1:87:27', timeout=5)

    if( deanHome != None and sarahHome != None):
      print "Everyone's home!"
    elif( deanHome == None and sarahHome == None):
      print "Nobody's home"
    else:
      cmd = 'node notify.js {0} {1}'.format(deanHome, sarahHome)
      proc = subprocess.Popen(cmd.split(), close_fds=True, bufsize=0, stdout=subprocess.PIPE)

      line = proc.stdout.readline()
      sys.stdout.write(line)

    time.sleep(15)
