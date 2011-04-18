## with negatives allowed
# best is [-0.95000000000000062, -0.95000000000000062, 0.98000000000000065, 8.0300000000000011]
# sum is 7.11
# prod is 7.1021335
# distance of best is 0.00786649999999


# dad's answer: 2.65 1.96 1.69 0.81

# mine, better precision: 3.18 * 1.40 * 1.21 * 1.32
# starting at 2,2,2: 2 * 2.07 * 2.29 * 0.75
#    10k 2 2.07 * 2.29 * 0.75 *p = 7.110450
#     2k 2 2.07 * 2.29 * 0.75 *p = 7.11

import numpy

def equalish(a, b):
  return abs(a - b) < 0.00001

def distanceFromProduct(costs):
  total = numpy.product(costs)
  return abs(total - 7.11)

def completeTriple(triple):
  return triple + [7.11 - sum(triple)]

def totalDistance(triple):
  return distanceFromProduct(completeTriple(triple))

def createSpread(triple):
  spread = [applySpread(spread, triple) for spread in spreads()]
  return filterNegativeValuesFromSpread(spread)

def spreads():
  vec = [-0.10, -0.01, 0, 0.01, 0.10]
  return [[a,b,c] for a in vec for b in vec for c in vec]

def applySpread(spread, triple):
  return [spread[0] + triple[0],
          spread[1] + triple[1],
          spread[2] + triple[2]]

def pickFittest(options):
  fittest = options[0]
  bestScore = totalDistance(fittest)

  for o in options:
    if totalDistance(o) < bestScore:
      fittest = o
      bestScore = totalDistance(o)

  return fittest

def solutionFound(triple):
  return equalish(totalDistance(triple), 0)

def filterNegativeValuesFromSpread(spread):
  return filter(tripletAllPositive, spread)

def tripletAllPositive(triplet):
  return (triplet[0] >= 0
      and triplet[1] >= 0
      and triplet[2] >= 0)

def main():
  best = [2,2,2]
  while not solutionFound(best):
    print best, totalDistance(best)
    newBest = pickFittest(createSpread(best))
    if best == newBest: break
    best = newBest
  complete = completeTriple(best)
  print "best is", complete
  print "sum is", sum(complete)
  print "prod is", numpy.prod(complete)
  print "distance of best is", totalDistance(best)

if __name__ == '__main__':
  main()
