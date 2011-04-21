import sevenEleven as S
import unittest

class TestSevenEleven(unittest.TestCase):

  def test_isSolution_good(self):
    self.assertTrue(S.isSolution(1.20, 1.25, 1.50, 3.16))

  def test_isSolution_bad(self):
    self.assertFalse(S.isSolution(2.00, 2.07, 2.29, 0.75))
    self.assertFalse(S.isSolution(3.18, 1.40, 1.21, 1.32))
    self.assertFalse(S.isSolution(2.65, 1.96, 1.69, 0.81))

  def test_findSolution(self):
    solution = S.findSolution()
    roundedSolution = map(lambda n: round(n * 100), solution)
    self.assertEqual(set(roundedSolution), set([120, 125, 150, 316]))

  def test_getAllFactors(self):
    self.assertEqual(set(S.getAllFactors(12, 5)), set([1, 2, 3, 4]))

if __name__ == '__main__':
  unittest.main()
