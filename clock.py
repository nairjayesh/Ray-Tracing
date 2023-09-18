"""
- Use Rotation Matrix to compute positions of hrs on clock 
- Draw the pixel on a 2D-canvas
- Assuming that the diagram is 2D and hence, noting only value of x,y in each transform.
"""
from features import Point, Color
from canvas import Canvas 
from matrices import rotation, mul_tup  
import math 



start = Point(0,-1,0)
transform = rotation(axis='z', radians=math.pi/6)
c = Canvas(500, 500) 
n = 1
color = Color(1,1,1)
radius = c.width*(3/8) #--only square shaped canvasas supporter through this #TODO: Extend support for rectangular canvas shape as well. 
origin_x = c.width/2
origin_y = c.height/2
plot = [(int(start.x*radius+origin_x),int(start.y*radius+origin_y))] 

while n < 12 :
    p = mul_tup(transform, start)
    plot.append((int(p.x*radius+origin_x), int(p.y*radius+origin_y)))
    n += 1
    start = p

for x,y in plot:
        c.write_pixel(x,y,color)
        
c.write_to_ppm()











