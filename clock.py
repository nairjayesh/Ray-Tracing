"""
- Use Rotation Matrix to compute positions of hrs on clock 
- Draw the pixel on a 2D-canvas
- Assuming that the diagram is 2D and hence, noting only value of x,y in each transform.
"""
from canvas import Canvas 
from matrices import translation, scaling, rotation, shearing, mul_tup  
import math 

start = Point(0,0,0)
transform = rotation(axis='y', radians=math.pi/6)
c = Canvas(900, 500) 

def clock(start, transform): 
	"""
	Computes the positions and passes them on 
	"""
	
	return ppm_file 
















