import sevenEleven as S
import unittest

class TestSevenEleven(unittest.TestCase):

  def test_distanceFromProduct(self):
    self.assertTrue(S.equalish(S.distanceFromProduct([1, 1, 1, 1]), 6.11))
    self.assertTrue(S.equalish(S.distanceFromProduct([1, 2, 3, 4]), (1 * 2 * 3 * 4) - 7.11))

  def test_equalish(self):
    self.assertTrue(S.equalish(1.0001, 1.0009))
    self.assertFalse(S.equalish(1.01, 1.09))

  def test_completeTriple(self):
    self.assertEqual([1, 1, 1, 4.11], S.completeTriple([1, 1, 1]))

  def test_totalDistance(self):
    self.assertEqual(S.totalDistance([1, 1, 1]), 3)
    self.assertTrue(S.equalish(S.totalDistance([1, 2, 3]), 0.45))

  def test_filterNegativeValuesFromSpread(self):
    before = [[0,0,0], [-1,0,0], [0,-1,0], [0,0,-1], [0,0,0]]
    after = [[0,0,0], [0,0,0]]
    self.assertEqual(S.filterNegativeValuesFromSpread(before), after)

  def test_tripletAllPositive(self):
    self.assertFalse(S.tripletAllPositive([-1,0,0]))
    self.assertFalse(S.tripletAllPositive([0,-1,0]))
    self.assertFalse(S.tripletAllPositive([0,0,-1]))
    self.assertTrue(S.tripletAllPositive([0,0,0]))

  def test_createSpread(self):
    start = [0, 0, 0]
    spread = S.createSpread(start)

    self.assertTrue(len(spread) > 4)

    likeStart = 0
    for s in spread:
      if s == start:
        likeStart += 1
      else:
        self.assertNotEqual(s, start)
        self.assertNotEqual(S.totalDistance(s), 0)

    self.assertEqual(likeStart, 1)

  def test_applySpread(self):
    self.assertEqual(S.applySpread([1,1,1], [3,3,3]), [4,4,4])
    self.assertEqual(S.applySpread([1,-1,1], [3,3,3]), [4,2,4])

  def test_pickFittest(self):
    options = [[0,0,0], [2,2,2], [1,1,1]]
    self.assertEqual([2,2,2], S.pickFittest(options))

  def test_solutionFound(self):
    #self.assertTrue(
    pass

if __name__ == '__main__':
  unittest.main()
