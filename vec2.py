import math
import collections
import numbers

class Vec2(object):
  def __init__(self, x, y=None):
    if isinstance(x, Vec2):
      self.v = [val for val in x.v]
    elif isinstance(x, collections.Iterable):
      if len(x) != 2:
        raise ValueError("Iterable must have length 2")
      self.v = [val for val in x]
    else:
      self.v = (x, y)
    self.__set_public_vars()

  def __set_public_vars(self):
    self.x = self.v[0]
    self.y = self.v[1]

  def __len__(self):
    return 2

  def __getattr__(self, name):
    # used to lazily evaluate the length
    if name == 'length':
      self.length = math.sqrt(self.x ** 2 + self.y ** 2)
      return self.length
    # otherwise just raise an attribute error
    raise AttributeError

  def __getitem__(self, k):
    return self.v[k]

  def __str__(self):
    return "<%r, %r>" % (self.x, self.y)

  def __repr__(self):
    return "pyvec.Vec2(x=%r, y=%r)" % (self.x, self.y)

  def __cmp__(self, other):
    # Just compare the lengths
    if self.length < other.length:
      return -1
    elif self.length > other.length:
      return 1
    return 0

  def __iter__(self):
    yield self.x
    yield self.y

  def __add__(self, other):
    return Vec2(self.x + other.x, self.y + other.y)

  def __sub__(self, other):
    return Vec2(self.x - other.x, self.y - other.y) 

  def __mul__(self, other):
    # If other is a number we simply scale by that
    # value, if it is not a number then we do
    # elementwise multiplication.  If a dot product
    # is required use the dot function
    if (isinstance(other, numbers.Number)):
      return Vec2(self.x * other, self.y * other)
    return Vec2(self.x * other.x, self.y * other.y)

  def __rmul__(self, other):
    return self * other

  def __neg__(self):
    return Vec2(-self.x, -self.y)

  def __invert__(self):
    return -self

  def __pos__(self):
    return Vec2(self)

  # don't implement __rdiv__ because deciding what
  # to do is a little tricky and not really worth
  # doing...

  def __div__(self, other):
    # Essentially the same as mult except we divide
    if (isinstance(other, numbers.Number)):
      return Vec2(self.x / float(other), self.y / float(other))
    return Vec2(float(self.x) / other.x, float(self.y) / other.y)

  def dot(self, other):
    return self.x * other.x + self.y * other.y

  def __pow__(self, other):
    # overload the pow operation to do dot product
    return self.dot(other)

  def unit(self):
    return Vec2(self.x / self.length, self.y / self.length)

  def round(self):
    return Vec2(int(round(self.x)), int(round(self.y)))

  def rads(self):
    # convert this vector's direction into
    # radians around the unit circle from -Pi to Pi
    return math.atan2(self.y, self.x)
