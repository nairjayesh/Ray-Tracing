# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 15:52:11 2023

@author: User
"""
# TODO: Install NetPbm Windows: https://gnuwin32.sourceforge.net/packages/netpbm.htm 
# TODO: Install GIMP (Already downloaded): https://www.gimp.org/downloads/thanks.html 
# TODO: Test pedinng for canvas pixel feature 


from features import Color 
import math 
#import string as str 

class Canvas: 
    
    def __init__(self, width, height, color=Color(0,0,0)) -> None: 
        self.width = width 
        self.height = height 
        self.color = color
        # TODO: Create Numpy arrays instead of 2D-List 
        self.grid = [[color for j in range(self.width)] for i in range(self.height)]
        
    def write_pixel(self, x, y, color):
        self.grid[y][x] = color  
        
    def pixel_at(self,x,y):
        return self.grid[y][x] 
    
    def canvas_to_ppm(self) -> str:
        """
        Returns
        -------
        Canvas header: 
                - First line is a string : P3 
                - Second line is numbers 
                - Third line is maximum color value
                - 
        Canvas Pixel values 
        """
        # TODO: Change the data structure - for ease of calculating the breaking point for a string line 
        magic_number = 'P3' #NetPbm identifier for image type 
        max_pixel_value = 255 #Max-Pixel value to be scaled towards
        header = '{0}\n{1} {2}\n{3}\n'.format(magic_number,self.width, self.height, max_pixel_value)
        pixel_value = ''
        for y in range(len(self.grid)):
            pixels = ''
            for x in range(len(self.grid[y])):
                color = self.grid[y][x]
                r = round(color.red*max_pixel_value) 
                g = round(color.green*max_pixel_value)
                b = round(color.blue*max_pixel_value) 
                if r < 0 : r = 0
                if g < 0 : g = 0
                if b < 0 : b = 0 
                if r > 255 : r = 255
                if g > 255 : g = 255
                if b > 255 : b = 255 
                
                if len(pixels) + len(f"{r} {g} {b} ") >= 70:
                    pixels += '\n' 
                pixels += f"{r} {g} {b} "
            pixel_value += pixels + '\n'
        return  header + pixel_value
    
def test_canvas() :
    c = Canvas(10, 20)
    assert c.width == 10
    assert c.height == 20
    assert c.pixel_at(2,3).value() == Color(0,0,0).value()
    # Write a color to Pixel 
    color = Color(1,0,0) #Red 
    c.write_pixel(2, 3, color)
    assert c.pixel_at(2, 3).value() == color.value()
    #max_pixel_value = 255
    cx = Canvas(5,3)
    c1 = Color(1.5, 0, 0)
    c2 = Color(0, 0.5, 0)
    c3 = Color(-0.5, 0, 1)
    cx.write_pixel(0,0,c1)
    cx.write_pixel(2,1,c2)
    cx.write_pixel(4,2,c3)
    assert cx.canvas_to_ppm() == 'P3\n5 3\n255\n255 0 0 0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 128 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 0 0 255 \n'

    return 'All the Canvas test\'s have passed'

print(test_canvas())

cx = Canvas(10,2)
c1 = Color(1, 0.8, 0.6)
for y in range(len(cx.grid)):
    for x in range(len(cx.grid[y])):
        cx.write_pixel(x,y,c1)
s = cx.canvas_to_ppm()
print(cx.canvas_to_ppm())

































