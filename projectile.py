# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 09:18:57 2023

@author: Dell
"""

from features import Projectile, Environment, tick, Point, Vector, Color
from canvas import Canvas

start = Point(0,1,0)
vector = Vector(1,1.8,0).normalize().scale(11.25)
p = Projectile(start, vector) 
gravity = Vector(0, -0.1, 0) 
wind = Vector(-0.01, 0, 0)
e = Environment(gravity, wind)
c = Canvas(900, 500)
color = Color(1,0,0)

plot = []
while p.position.value()[1] >= 0:
  plot.append((int(p.position.value()[0]), int(c.height - p.position.value()[1])))
  p = tick(e, p)

      
for x,y in plot:
        c.write_pixel(x,y,color)

ppm_data = c.canvas_to_ppm()
with open('Project.ppm','w') as ppm_file: 
    ppm_file.write(ppm_data) 