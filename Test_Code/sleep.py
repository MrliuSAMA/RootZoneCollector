#!/usr/bin/env python
import time
import os
import sys
def funzioneDemo():
  time.sleep(100)
def createDaemon():	
  try:
    if os.fork() > 0: os._exit(0)
  except OSError, error:
    print 'fork #1 failed: %d (%s)' % (error.errno, error.strerror)
    os._exit(1)	
  os.chdir('/')
  os.setsid()
  os.umask(0)
  try:
    pid = os.fork()
    if pid > 0:
      print 'Daemon PID %d' % pid
      os._exit(0)
  except OSError, error:
    print 'fork #2 failed: %d (%s)' % (error.errno, error.strerror)
    os._exit(1)
  sys.stdout.flush()
  sys.stderr.flush()
  si = file("/dev/null", 'r')
  so = file("/dev/null", 'a+')
  se = file("/dev/null", 'a+', 0)
  os.dup2(si.fileno(), sys.stdin.fileno())
  os.dup2(so.fileno(), sys.stdout.fileno())
  os.dup2(se.fileno(), sys.stderr.fileno())
  funzioneDemo() # function demo
if __name__ == '__main__': 
  createDaemon()
