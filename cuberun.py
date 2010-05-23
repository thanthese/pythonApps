#!/usr/bin/env python

"""
Stephen Mann
April 25, 2010


Terminal program for timing Rubik's Cube solves using a
modified Roux method.

Intended to be used as a bash utility.  Run chmod +x on the
file and drop it in your PATH somewhere.  Now the script can
be run from anywhere on the system with just

  $ cuberun


Credits
-------

Editing and suggestions from Adam Colton, http://adamcolton.net

"""

import timeit
import shufflecube

stages = [
  "inspect",
  "step 1: left 3x2x1",
  "step 2: right 3x2x1",
  "step 3a: move corners",
  "step 3b: twist corners",
  "step 4a: twist edges",
  "step 4b: R/L edges",
  "step 4c: move edges"]

def wait(message):
  """
  Return how many seconds it takes the user to hit <enter>.
  Display message in meantime.
  """

  cmd = "raw_input('  %s')" % message
  return timeit.Timer(cmd).timeit(1)

print
print "============"
print "shuffle cube"
print "============"
print
print shufflecube.prettyMoves(25)
print

wait("press <enter> once cube is shuffled")

print
print "press <enter> after completing each stage"
print "========================================="

durs  = map(wait, stages)  # durations
nDurs = zip(durs, stages)  # named durations

total   = sum(durs)
slowest = max(nDurs)
fastest = min(nDurs)

print
print "results"
print "======="

for nDur in nDurs:
  print "%4.1f: %s" % nDur

print "total: %.1f seconds" % total
print
print 'slowest stage at %4.1f seconds was "%s"' % slowest
print 'fastest stage at %4.1f seconds was "%s"' % fastest
