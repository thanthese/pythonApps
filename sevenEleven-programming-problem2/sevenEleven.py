import math

##
# Stephen Mann
# April 2011
#
# Solution 7-11 problem: find 4 numbers whose sum and product are exactly 7.11
#
# Method: use algebra to reduce the search space from 711^4 to 711^2.
#
# Notes:
# - precision is python is annoying, hence the fiddling with powers of ten
# - a,b,c,d are the numbers to find.  b and c are givens (by loops), a and
#   d are solved for.  m and n are helpers.
# - this solution doesn't scale well, obviously
# - runtime is less than one second
# - there is exactly one solution
#

z = 7.11

def a(b, c):
  _m = m(b, c)
  _n = n(b, c)
  top = -_n + math.sqrt(_n*_n - 4*_m*z)
  bottom = 2 * _m
  return top / bottom

def m(b, c):
  return b*c

def n(b, c):
  return b*b*c + b*c*c - b*c*z

def d(b, c):
  _a = a(b, c)
  return z / (_a*b*c)

def forcePrecision(n):
  # turn our decimals into integers
  return round(n * 100)

def isSolution(a, b, c, d):
  a1 = forcePrecision(a)
  b1 = forcePrecision(b)
  c1 = forcePrecision(c)
  d1 = forcePrecision(d)
  return a1 + b1 + c1 + d1 == z * 100 and a1 * b1 * c1 * d1 == z * 100000000

def findSolution():
  for b in xrange(1, 712):  # xrange doesn't support decimals
    for c in xrange(b, 712):
      B = b / 100.0  # divide to make proper decimal
      C = c / 100.0
      A = a(B, C)
      D = d(B, C)
      if isSolution(A, B, C, D):
        return [A, B, C, D]

def prettyDisplay(a, b, c, d):
  print "a: %.2f" % a
  print "b: %.2f" % b
  print "c: %.2f" % c
  print "d: %.2f" % d
  print "sum: %.2f" % (a + b + c + d)
  print "product: %.2f" % (a * b * c * d)

if __name__ == '__main__':
  solution = findSolution()
  prettyDisplay(*solution)
