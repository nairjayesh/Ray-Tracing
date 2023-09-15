# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 15:52:11 2023

@author: User
"""
# TODO: Install NetPbm Windows: https://gnuwin32.sourceforge.net/packages/netpbm.htm 
# TODO: Install GIMP (Already downloaded): https://www.gimp.org/downloads/thanks.html 
# TODO: Test pedinng for canvas pixel feature 


from features import Color 
import numpy as np 

class Canvas: 
    
    def __init__(self, width, height, color=Color(0,0,0)) -> None: 
        """
        width: Width of canvas -> No. of columns in the matrix holding pixel values
        height: Height of canvas -> No. of rows in the matrix holding pixel values 
        """
        self.width = width 
        self.height = height 
        self.color = color
        self.grid = np.full((height, width), color)
        
    def write_pixel(self, col, row, color) -> None:
        """
        row -> Row no.
        col -> Column no.
        """
        self.grid[row, col] = color  
        
    def pixel_at(self, col, row) -> Color:
        """
        row -> Row no. 
        col -> Col no. 
        """
        return self.grid[row, col] 
    
    def canvas_to_ppm(self) -> str:
        """
        Returns
        -------
        Canvas Pixel in PPM format to read 
        """
        magic_number = 'P3' #NetPbm identifier for image type 
        max_pixel_value = 255 #Max-Pixel value to be scaled towards
        header = '{0}\n{1} {2}\n{3}\n'.format(magic_number, self.width, self.height, max_pixel_value)
        pixel_value = ''
        for row in range(self.height):
            pixels = []
            for col in range(self.width):
                color_scaled = pixel_conversion(self.grid[row, col])
                pixels.extend(color_scaled)     
                #Consider: each pixel has 12 characters -- 12*col = No. of Characters per line # No rationale of 17? 
            for line in [pixels[i:i+17] for i in range(0, len(pixels), 17)]: #HOWTO: Decide the total characters in a line 
                pixel_value += " ".join(line) + '\n'
        return  header + pixel_value
    
def pixel_conversion(pixel_value) -> list:
    """ 
    Converts the pixel value from 0 - 1 scale to 0 - 255 scale 
    Allows for clamping of values < 0 and values > 255 
    Returns
    -------
    Tuple with new RGB values 
    """ 
    #TODO: Change the implementation - using only single value instead of whole pixel
    color = pixel_value
    max_pixel_value = 255
    r = round(max(min(color.red*max_pixel_value, max_pixel_value),0)) 
    g = round(max(min(color.green*max_pixel_value, max_pixel_value), 0))
    b = round(max(min(color.blue*max_pixel_value, max_pixel_value), 0)) 
    return [str(r),str(g),str(b)] 

def test_canvas() :
    c = Canvas(10, 20)
    assert c.width == 10
    assert c.height == 20
    assert c.pixel_at(2,3).value() == Color(0,0,0).value()
    # Write a color to Pixel 
    color = Color(1,0,0) #Red 
    c.write_pixel(2, 3, color)
    assert c.pixel_at(2, 3).value() == color.value()
    cx = Canvas(5,3)
    c1 = Color(1.5, 0, 0)
    c2 = Color(0, 0.5, 0)
    c3 = Color(-0.5, 0, 1)
    cx.write_pixel(0,0,c1)
    cx.write_pixel(2,1,c2)
    cx.write_pixel(4,2,c3)
    assert cx.canvas_to_ppm() == 'P3\n5 3\n255\n255 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 128 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 255\n'
    cy = Canvas(10,2)
    for x in range(cy.height):
        for y in range(cy.width):
            cy.write_pixel(y, x, Color(1, 0.8, 0.6))
    assert cy.canvas_to_ppm() == 'P3\n10 2\n255\n255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n153 255 204 153 255 204 153 255 204 153 255 204 153\n255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n153 255 204 153 255 204 153 255 204 153 255 204 153\n'
    assert cy.canvas_to_ppm()[-1:] == '\n'
    return 'All the Canvas test\'s have passed'

#print(test_canvas())

# GET THE IMAGE.PPM FILE 
c = Canvas(10,10)
for x in range(c.height):
    for y in range(c.width):
        c.write_pixel(y, x, Color(1, 0.8, 0.6))
ppm_data = c.canvas_to_ppm()
with open('Image.ppm','w') as ppm_file: 
    ppm_file.write(ppm_data)   






























