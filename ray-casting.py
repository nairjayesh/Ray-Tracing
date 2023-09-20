"""
1. Each Ray has origin (starting point) and direction (vector)
2. Each Sphere is of unit radius 
"""
from features import Tuple, Point, Vector
import math  

class Ray: 
    
    def __init__(self, origin, direction) -> None: 
        self.origin = origin  
        self.direction = direction   
    
    def position(self,t) -> Point: 
        origin = self.origin  
        distance = self.direction.scale(t) 
        return origin.__class__(origin.x+distance.x, 
								origin.y+distance.y, 
								origin.z+distance.z, 
								origin.w+distance.w) 
	
    #TODO: Change the implementation - this is bad 
    @property  
    def sphere_to_ray(self) -> Vector: 
        print('sphere_to_ray:',Tuple.subtract(self.origin, Point(0,0,0)).value())
        return Tuple.subtract(self.origin, Point(0,0,0))
	
    @property  
    def a(self) -> float: 
        print('a-dot',Tuple.dot(self.direction, self.direction))
        return Tuple.dot(self.direction, self.direction)

    @property  
    def b(self) -> float: 
        print('b-dot',Tuple.dot(self.direction, self.sphere_to_ray))
        return (Tuple.dot(self.direction, self.sphere_to_ray))*2

    @property  
    def c(self) -> float: 
        print('c-dot:',Tuple.dot(self.sphere_to_ray, self.sphere_to_ray))
        return Tuple.dot(self.sphere_to_ray, self.sphere_to_ray)

    def discriminate(self) -> float:  
        print('dis-a:',self.a)  
        print('dis-c:',self.c) 
        print('dis-b:',pow(self.b,2))
        return pow(self.b,2) - 4*self.a*self.c  

def intersect(sphere, ray) -> tuple: 
    d = ray.discriminate() 
    print('d:',d)
    if d < 0: 
        return () 
    t1 = (-ray.b - math.sqrt(ray.discriminate())) / (2*ray.a) 
    t2 = (-ray.b + math.sqrt(ray.discriminate())) / (2*ray.a) 
    return (min(t1, t2), max(t1, t2)) 
		 	

class Sphere:
	
	def __init__(self, name) -> None:
		self.name = name  
	
	def name(self) -> int:
		return self.name   


def test_ray_casting() -> str:
	
	# Testing instantiation 
    origin = Point(1,2,3) 
    direction = Vector(4,5,6)
    r1 = Ray(origin, direction)
    assert Tuple.equal(r1.origin, origin)
    assert Tuple.equal(r1.direction, direction)
	
	# Testing position() 
    r2 = Ray(Point(2,3,4), Vector(1, 0, 0))
    assert Tuple.equal(Point(2,3,4), r2.position(0))
    assert Tuple.equal(Point(3,3,4), r2.position(1))
    assert Tuple.equal(Point(1,3,4), r2.position(-1))
    assert Tuple.equal(Point(4.5, 3, 4), r2.position(2.5)) 
	
	# Testing intersect()
	# Ray doesn't intersect  
    r3 = Ray(Point(0, 1, -5), Vector(0, 0, 1))
    s1 = Sphere(1)
    xs1 = intersect(s1, r3)
    assert len(xs1) == 0  
	
	#1-Ray intersects at 2 points 
    r4 = Ray(Point(0, 0, -5), Vector(0, 0, 1)) 
    s2 = Sphere(2) 
    xs2 = intersect(s2, r4)
    assert len(xs2) == 2 
    print(xs2[0],xs2[1])
    assert math.isclose(xs2[0], 4.0)  
    assert math.isclose(xs2[1], 6.0) 
	
	#2-Ray intersects at 1 point  
    r5 = Ray(Point(0, 1, 5), Vector(0, 0, 1)) 
    s3 = Sphere(3) 
    xs3 = intersect(s3, r5) 
    assert len(xs3) == 2 
    assert math.isclose(xs3[0], 5.0)  
    assert math.isclose(xs3[1], 5.0) 
	
	#3-Ray originates from within a sphere  
    r6 = Ray(Point(0,0,0), Vector(0,0,1)) 
    s4 = Sphere(4) 
    xs4 = intersect(s4, r6) 
    assert len(xs4) == 4 
    assert math.isclose(xs4[0], -1.0) 
    assert math.isclose(xs4[1], 1.0)

	#4-Sphere is behind the Ray  
    r7 = Ray(Point(0,0,5), Vector(0,0,1)) 
    s5 = Sphere(5) 
    xs5 = intersect(s5, r7) 
    assert len(xs5) == 2 
    assert math.isclose(xs5[0], -6.0) 
    assert math.isclose(xs5[1], -4.0)
    
    return 'All tests in ray-casting passed' 


print(test_ray_casting())




 


