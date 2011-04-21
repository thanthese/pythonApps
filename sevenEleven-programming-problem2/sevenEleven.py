import math

##
# Stephen Mann
# April 2011
#
# 7-11 problem: find 4 numbers whose sum and product are exactly 7.11
#
# Method: use algebra to reduce the search space from 711^4 to 711^2.  Then
# iterate only over factors of 711,000,000, up to 711, instead of one-by-one
#
# Notes:
# - precision is python is annoying, hence the fiddling with powers of ten
# - a,b,c,d are the numbers to find.  b and c are givens (by loops), a and
#   d are solved for.  m and n are helpers.
# - runtime is less than one-tenth of a second
# - there is exactly one solution
#
# Python 2.5.1
#

z = 7.11
z_sum = z * 100
z_prod = z * 100000000

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
  return a1 + b1 + c1 + d1 == z_sum and a1 * b1 * c1 * d1 == z_prod

def findSolution():
  factors = getAllFactors(z_prod, z_sum)
  for b in factors:
    for c in factors:
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

def getAllFactors(of, upto):
  possibilities = range(1, int(upto) + 1)
  isFactor = lambda f: float(of) / f == round(of / f)
  return filter(isFactor, possibilities)

def main():
  solution = findSolution()
  prettyDisplay(*solution)

if __name__ == '__main__':
  main()
