# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:24:57 2023

@author: User
"""


import math
#import matplotlib.pyplot as plt
 
EPSILON = 0.00001 # reference float-number for function equal() 

class Tuple:
    
    def __init__(self, x, y, z, w) -> None :
        self.x = x
        self.y = y 
        self.z = z 
        self.w = w 
    
    @staticmethod
    def add(a,b) :
        assert a.w + b.w in [0,1], 'Cannot add these arguments'
        return a.__class__(a.x + b.x, a.y + b.y, a.z + b.z, a.w + b.w) #self.__class__() used to referece class of the object
    
    @staticmethod
    def subtract(a,b) : 
        assert a.w - b.w in [0,1], 'Cannot subtract the argument'
        return a.__class__(a.x - b.x, a.y - b.y, a.z - b.z, a.w - b.w)
    
    @staticmethod
    def equal(a,b) :
        return (abs(a.x - b.x) < EPSILON and abs(a.y - b.y) < EPSILON and abs(a.z - b.z) < EPSILON and abs(a.w - b.w) < EPSILON)
    
    def value(self, decimal_places=2):
        return (
            round(self.x, decimal_places),
            round(self.y, decimal_places),
            round(self.z, decimal_places),
            round(self.w, decimal_places)
        )
    
    def negate(self) : 
        return  self.__class__(-self.x, -self.y, -self.z, -self.w)
    
    def scale(self, val):
        return self.__class__(val*self.x, val*self.y, val*self.z, val*self.w)
    
    def divide(self, val):
        return self.__class__(self.x/val, self.y/val, self.z/val, self.w/val)
    
    def magnitude(self):
        return math.sqrt(sum(x**2 for x in self.value()))
    
    def normalize(self):
        val = self.magnitude()
        assert val != 0
        return self.__class__(self.x/val, self.y/val, self.z/val, self.w/val)
    
    @staticmethod
    def dot(a, b) -> float:
      """
      Function computes the dot product of two vectors 
      :param a -- vector data type 
      :param b -- vector data type 
      """
      return (a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w) 
        
    @staticmethod
    def cross(a, b):
      assert a.w == b.w == 0, 'Points are not allowed to be cross-multiplied '
      return a.__class__(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z,
                    a.x * b.y - a.y * b.x)
    
class Point(Tuple):

  def __init__(self, x, y, z, w=1) -> None:
    """
    Creates a Point object with 4 parameters 
    """
    super().__init__(x,y,z,w)


class Vector(Tuple):

  def __init__(self, x, y, z, w=0) -> None:
    """
    Creates a Vector object with 4 parameters 
    """
    super().__init__(x,y,z,w)
    
class Color(Tuple):
    
    def __init__(self, x, y, z, w=0) -> None:
        """
        Parameters
        ----------
        x : type <Float> b/w 0 , 1
            R = Red of RGB color module
        y : type <Float> b/w 0, 1
            G = Green of RGB color module 
        z : type <Float> b/w 0, 1
            B = Blue of RGB color module.
        w : type <int> b/w 0, 1
            Identifies color.

        Returns
        -------
        None.
        """
        super().__init__(x, y, z, w)
    
    #Using property decorator -- this is a solution to insted using a.red in the init because we are inheriting from the class Tuple - which doesn't recognize what .red, .green, .blue is
    @property
    def red(self):
        return self.x 
    
    @property
    def green(self):
        return self.y 
    
    @property
    def blue(self):
        return self.z
    
    @staticmethod
    def blend(a, b) : # For better readability -- will use red, green , blue instead of x, y, z --
        return a.__class__(a.red*b.red, a.green*b.green, a.blue*b.blue, a.w*b.w)
    
    

class Projectile:
  """
  Projectile: A data structure that has a position (a point) and a velocity (a vector)
  """

  def __init__(self, position, velocity) -> None:
    self.position = position
    self.velocity = velocity

  def print_val(self):
    pass


class Environment:
  """
  Environment: A data structure that has gravity (a vector) and wind (a vector).
  :arg gravity --> vector data type 
  :arg wind --> vector data type 
  """

  def __init__(self, gravity, wind) -> None:
    self.gravity = gravity
    self.wind = wind

  def print_val(self):
    pass


def tick(env, proj) -> Projectile:
  """
  Provides a new projective after 1 unit of time or ticks has elapsed
  :arg env 
  :arg proj
  :param postion
  :param environment 
  :param velocity 
  returns -> updated Projectile 
  """
  position = Tuple.add(proj.position, proj.velocity)
  environment = Tuple.add(env.gravity, env.wind)
  velocity = Tuple.add(proj.velocity, environment)
  return Projectile(position, velocity)






def test_features():
  """
  Function that test's all the features 
  :returns assertion error in case test fails 
  """
  #TODO: Write Assertion error statements for clarity
  #Test Points and Vectors
  a = Point(3, 2, 1)
  b = Vector(-2, 3, 1)
  c = Point(5, 6, 7)
  d = Vector(3, 2, 1)
  e = Vector(5, 6, 7)
  assert Point(1, 2, 3).value() == (1, 2, 3, 1)
  assert Vector(2, 3, 4).value() == (2, 3, 4, 0)
  # Adding Tuples
  assert Tuple.add(a, b).value() == (1, 5, 2, 1)
  #Subtracting Tuples
  assert Tuple.subtract(a, c).value() == (-2, -4, -6, 0)
  assert Tuple.subtract(a, b).value() == (5, -1, 0, 1)
  assert Tuple.subtract(d, e).value() == (-2, -4, -6, 0)
  #Negating Vector
  assert b.negate().value() == (2, -3, -1, 0)
  #Scaling a Vector
  assert b.scale(3.5).value() == (-7.0, 10.5, 3.5, 0)
  #Magnitude of a Vector
  #Test vectors
  v1 = Vector(1, 0, 0)
  v2 = Vector(0, 1, 0)
  v3 = Vector(0, 0, 1)
  v4 = Vector(1, 2, 3)
  v5 = Vector(-1, -2, -3)
  assert v1.magnitude() == 1
  assert v2.magnitude() == 1
  assert v3.magnitude() == 1
  assert v4.magnitude() == math.sqrt(14)
  assert v5.magnitude() == math.sqrt(14)
  #Normalizing a vector
  v6 = Vector(4, 0, 0)
  assert v6.normalize().value() == Vector(1, 0, 0).value()
  assert v1.normalize().value() == Vector(1, 0, 0).value()
  assert Tuple.equal(v4.normalize(), Vector(0.26726, 0.53452, 0.80178)) == True
  #Dot Product tests
  v7 = Vector(1, 2, 3)
  v8 = Vector(2, 3, 4)
  assert Vector.dot(v7, v8) == 20.0
  # Cross Product tests
  assert Vector.cross(v7, v8).value() == Vector(-1, 2, -1).value()
  assert Vector.cross(v8, v7).value() == Vector(1, -2, 1).value()
  # Color add
  # TODO: Investigate - why do I always need to add .value() to my tests? 
  assert Tuple.add(Color(0.9, 0.6, 0.75), Color(0.7, 0.1, 0.25)).value() == Color(1.6, 0.7, 1.0).value()
  # Color subtract 
  assert Tuple.subtract(Color(0.9, 0.6, 0.75), Color(0.7, 0.1, 0.25)).value() == Color(0.2, 0.5, 0.5).value() 
  #Scale function of color
  c1 = Color(0.2,0.3,0.4)
  assert c1.scale(2).value() == Color(0.4,0.6,0.8).value()
  #Color blend
  c2 = Color(1, 0.2, 0.4)
  c3 = Color(0.9, 1, 0.1)
  assert Color.blend(c2, c3).value() == Color(0.9, 0.2, 0.04).value()
  
  
  return 'All the feature test\'s have passed!'

#Test outcomes on the terminal 

#print(test_features())
#simulate() 
