import unittest
import math
from vec2 import Vec2

class TestVec2(unittest.TestCase):
  def setUp(self):
    self.v1 = Vec2(1, 1)
    self.v2 = Vec2(2, 2)
    self.v3 = Vec2(1, 2)

  def test_instantiation(self):
    # instantiation using array
    v = Vec2([1, 2])
    self.assertEqual(v.x, 1)
    self.assertEqual(v.y, 2)
    # instantiation using tuple
    v = Vec2((1, 2))
    self.assertEqual(v.x, 1)
    self.assertEqual(v.y, 2)
    # instantion using Vec2
    v2 = Vec2(v)
    self.assertEqual(v.x, 1)
    self.assertEqual(v.y, 2)
    # should raise a type error if we try to pass
    # an iterable with length != 2
    self.assertRaises(ValueError, Vec2, (1, 2, 3))

  def test_public_interfaces(self):
    self.assertEqual(self.v1.x, 1)
    self.assertEqual(self.v1.y, 1)
    len_should_be = math.sqrt(2**2 + 2**2)
    self.assertEqual(self.v2.length, len_should_be)
    self.assertEqual(self.v3[0], 1)
    self.assertEqual(self.v3[1], 2)

  def test_len(self):
    # len should always be 2
    self.assertEqual(len(self.v1), 2)

  def test_cmp(self):
    self.assertLess(self.v1, self.v2)
    self.assertGreater(self.v2, self.v1)
    self.assertEqual(self.v1, self.v1)

  def test_iter(self):
    i = 0
    for value in self.v3:
      if i == 0:
        self.assertEqual(value, 1)
        i += 1
      else:
        self.assertEqual(value, 2)

  def test_add(self):
    v = self.v1 + self.v3
    self.assertEqual(v, Vec2(2, 3))

  def test_sub(self):
    v = self.v1 - self.v3
    self.assertEqual(v, Vec2(0, -1))

  def test_mul(self):
    v = self.v1 * self.v3
    self.assertEqual(v, Vec2(1, 2))
    v = self.v1 * 4
    self.assertEqual(v, Vec2(4, 4))

  def test_rmul(self):
    # make sure if we multiply a number
    # by a vector it works out as we would
    # expect
    v = 5 * self.v1
    self.assertEqual(v, Vec2(5, 5))

  def test_neg(self):
    v = -self.v1
    self.assertEqual(v, Vec2(-1, -1))

  def test_invert(self):
    v = ~self.v1
    self.assertEqual(v, Vec2(-1, -1))

  def test_pos(self):
    v = +self.v1
    self.assertEqual(v, Vec2(1, 1))

  def test_div(self):
    v = self.v1 / self.v2
    self.assertEqual(v, Vec2(1.0/2.0, 1.0/2.0))
    v = self.v1 / 3
    self.assertEqual(v, Vec2(1.0/3, 1.0/3))

  def test_dot(self):
    n = self.v1.dot(self.v2)
    self.assertEqual(n, 4)

  def test_pow(self):
    # test to make sure pow is returning
    # the dot product
    n = self.v1 ** self.v2
    self.assertEqual(n, 4)

  def test_round(self):
    v = Vec2(1.4, 1.5)
    vr = v.round()
    self.assertEqual(vr, Vec2(1, 2))

  def tearDown(self):
    pass

if __name__ == "__main__":
  unittest.main()