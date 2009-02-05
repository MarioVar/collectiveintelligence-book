import unittest

import treepredict

class DividesetTest(unittest.TestCase):

  def testIntegerDivide(self):
    self.assertEquals(([(3,), (4,)], [(1,), (2,)]),
        treepredict.divideset([(1,), (2,), (3,), (4,)], 0, 3))

  def testFloatDivide(self):
    self.assertEquals(([(3.0,), (4.0,)], [(1.0,), (2.0,)]),
        treepredict.divideset([(1.0,), (2.0,), (3.0,), (4.0,)], 0, 3.0))

  def testStringDivide(self):
    self.assertEquals(([('a',)], [('b',), ('c',)]),
        treepredict.divideset([('a',), ('b',), ('c',)], 0, 'a'))


class GiniimpurityTest(unittest.TestCase):

  def testBasics(self):
    d = treepredict.testdata()
    self.assertAlmostEquals(0.6328125, treepredict.giniimpurity(d))

    s1, s2 = treepredict.divideset(d, 2, 'yes')
    self.assertAlmostEquals(0.53125, treepredict.giniimpurity(s1))


class EntropyTest(unittest.TestCase):

  def testBasics(self):
    d = treepredict.testdata()
    self.assertAlmostEquals(1.5052408, treepredict.entropy(d))

    s1, s2 = treepredict.divideset(d, 2, 'yes')
    self.assertAlmostEquals(1.2987949, treepredict.entropy(s1))


if __name__ == '__main__':
  unittest.main()
