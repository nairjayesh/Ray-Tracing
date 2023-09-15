# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 09:18:57 2023

@author: Dell
"""

from features import Projectile, Environment, tick, Point, Vector, Color
from canvas import Canvas

# Defining starting variables - for more info --check features.py and canvas.py
start = Point(0,1,0)
vector = Vector(1,1.8,0).normalize().scale(11.25)
p = Projectile(start, vector) 
gravity = Vector(0, -0.1, 0) 
wind = Vector(-0.01, 0, 0)
e = Environment(gravity, wind)
c = Canvas(900, 500)
color = Color(1,0,0)

# Calculating the projectile co-ordinates 
plot = []
while p.position.value()[1] >= 0:
  plot.append((int(p.position.value()[0]), int(c.height - p.position.value()[1])))
  p = tick(e, p)

# Mapping the projectile co-ordinates with pixel co-ordinates 
for x,y in plot:
        c.write_pixel(x,y,color)

c.write_to_ppm()