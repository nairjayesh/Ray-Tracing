# -*- coding: utf-8 -*-
"""
Create - Matrices & Transformations 
"""
# TODO: In second iteration of matricies write an implementation without numpy 
# TODO: The clock project tracking in the end 
# TODO: Implement Fluent API - for chain of transformations 

import numpy as np 
from numpy.linalg import inv 
from features import Point, Vector, Tuple 
import math 
import time 

start = time.monotonic() 

#
identity_matrix = np.identity(4)

def translation(x,y,z):
	"""
	Creates a 4x4 translate matrix from an identity matrix 
	"""
	translate = identity_matrix.copy()	 
	translate[0,3] = x 
	translate[1,3] = y
	translate[2,3] = z 
	return translate 

def scaling(x,y,z):
	"""
	Creates a 4x4 scale matrix from an identity matrix 
	"""
	scale = identity_matrix.copy()
	scale[0,0] = x 
	scale[1,1] = y
	scale[2,2] = z 
	return scale

def rotation(axis, radians):
	"""
	Creates a 4x4 rotate matrix based on particular axes from an identity matrix 
	"""
	rotate = identity_matrix.copy()
	if axis == 'x':
		rotate[1,1] = math.cos(radians)
		rotate[1,2] = -(math.sin(radians))
		rotate[2,1] = math.sin(radians)
		rotate[2,2] = math.cos(radians)
	if axis == 'y':
		rotate[0,0] = math.cos(radians)
		rotate[0,2] = math.sin(radians)
		rotate[2,0] = -(math.sin(radians))
		rotate[2,2] = math.cos(radians)
	if axis == 'z': 
		rotate[0,0] = math.cos(radians)
		rotate[0,1] = -(math.sin(radians))
		rotate[1,0] = math.sin(radians)
		rotate[1,1] = math.cos(radians)
	return rotate 

def shearing(x_y, x_z, y_x, y_z, z_x, z_y):
	shear = identity_matrix.copy()
	shear[0,1] = x_y 
	shear[0,2] = x_z
	shear[1,0] = y_x 
	shear[1,2] = y_z
	shear[2,0] = z_x 
	shear[2,1] = z_y
	return shear  

def mul_tup(matrix, tup): 
	"""
	Multiplies Point / Vector tuples with the transform matrix 
	"""
	tup_matrix = np.array([[tup.x],[tup.y],[tup.z],[tup.w]])
	result = (matrix @ tup_matrix)
	return tup.__class__(result[0,0], result[1,0], result[2,0], result[3,0]) 

def chain_transform(A=identity_matrix, B=identity_matrix, C=identity_matrix): 
	result = C @ B @ A 
	return result 

def test_matrices():
	# Testing a 4x4 matrix
	M = np.array([[1,2,3,4],[5.5,6.5,7.5,8.5],[9,10,11,12],[13.5,14.5,15.5,16.5]])
	assert M[0,0] == 1
	assert M[0,3] == 4
	assert M[1,0] == 5.5
	assert M[1,2] == 7.5
	assert M[2,2] == 11
	assert M[3,0] == 13.5
	assert M[3,2] == 15.5 
   
	# Testing a 2x2 matrix
	M = np.array([[-3, 5], [1, -2]])
	assert M[0,0] == -3
	assert M[0,1] == 5
	assert M[1,1] == -2 
   
	# Testing a 3x3 matrix 
	M = np.array([[-3, 5, 0],[1,-2,-7],[0,1,1]])
	assert M[0,0] == -3
	assert M[1,1] == -2
	assert M[2,2] == 1
	
	# Testing equality of matrices 
	M1 = np.array([[1.0,2.0,3.0,4.0],[5.0,6.0000000009,7.0,8.0],[9.0,8.0,7.0,6.0],[5.0,4.0,3.0,2.0]])
	M2 = np.array([[1.0,2.0,3.0,4.0],[5.0,6.0,7.0,8.0],[9.0,8.0,7.0,6.0],[5.0,4.0,3.0,2.0]])
	assert np.allclose(M1, M2) == True
	M3 = np.array([[1,2,3,4],[2,3,4,5],[1,1,1,1],[0,1,1,2]])
	assert np.allclose(M1, M3) == False
	M4 = np.array([[1,1],[2,2]])
	M5 = np.array([[2,2],[1,1]])
	assert np.allclose(M4 @ M5, np.array([[3,3],[6,6]]))
	
	# HOWTO: Handle tuple multiplication -- update: Use mul_tup
	M6 = np.array([[1,2,3,4],[2,4,4,2],[8,6,4,1],[0,0,0,1]])
	b = (1,2,3,1)
	assert	np.allclose(M6@b, np.array([18,24,33,1]))
	
	# Identity matrix
	M7 = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
	identity = np.identity(4)
	assert np.allclose(M7 @ identity, M7)
	
	# Transposing of matrix 
	M8 = np.array([[0,9,3,0],[9,8,0,8],[1,8,5,3],[0,0,5,8]])
	M9 = np.transpose(M8)
	assert np.allclose(M9, np.array([[0,9,1,0],[9,8,8,0],[3,0,5,5],[0,8,3,8]]))
	assert np.allclose(identity, np.transpose(identity))
	
	# Inverting Matrices -- from native numpy package 
	M10 = np.array([[6,4,4,4],[5,5,7,6],[4,-9,3,-7],[9,1,7,-6]])
	assert np.linalg.det(M10) == -2120
	M11 = np.array([[-5,2,6,-8],[1,-5,1,8],[7,7,-6,-7],[1,-3,7,4]]) 
	M12 = (inv(M11)) 
	
	# Translating Matrices	
	# Test with Point 
	p = Point(-3, 4, 5)
	transform_1 = translation(5, -3, 2)
	result = (mul_tup(transform_1, p))
	assert Point(2,1,7).value() == result.value() 
	assert Tuple.equal(Point(-8,7,3), (mul_tup(inv(transform_1), p))) 
	# Test with vector 
	assert Vector(-3,4,5).value() == (mul_tup(transform_1, Vector(-3,4,5))).value() 
	
	# Scaling Matrices 
	transform_2 = scaling(2, 3, 4)
	p1 = Point(-4,6,8)
	v1 = Vector(-4,6,8)
	assert Tuple.equal(Point(-8,18,32), mul_tup(transform_2, p1))
	assert Vector(-2,2,2).value() == mul_tup(inv(transform_2), v1).value() 
	
	# Reflecting Matrices -- along a particular axis 
	# Check reflection across - x axis 
	transform_3 = scaling(-1, 1, 1)
	assert Point(-2,3,4).value() == mul_tup(transform_3, Point(2,3,4)).value() 
	
	# Rotating Matrices 
	
	# Rotate around x 
	p2 = Point(0,1,0) 
	half_quarter = rotation('x', math.pi/4)
	full_quarter = rotation('x', math.pi/2)
	assert Tuple.equal(Point(0, math.sqrt(2)/2, math.sqrt(2)/2), mul_tup(half_quarter, p2)) 
	assert Tuple.equal(Point(0,0,1), mul_tup(full_quarter, p2)) 
	
	# Rotate around y 
	p3 = Point(0,0,1) 
	half_quarter = rotation('y', math.pi/4)
	full_quarter = rotation('y', math.pi/2)
	assert Tuple.equal(Point(math.sqrt(2)/2, 0, math.sqrt(2)/2), mul_tup(half_quarter, p3)) 
	assert Tuple.equal(Point(1,0,0), mul_tup(full_quarter, p3)) 
	
	# Rotate around z 
	half_quarter = rotation('z', math.pi/4)
	full_quarter = rotation('z', math.pi/2)
	assert Tuple.equal(Point(-math.sqrt(2)/2, math.sqrt(2)/2, 0), mul_tup(half_quarter, p2)) 
	assert Tuple.equal(Point(-1,0,0), mul_tup(full_quarter, p2))
	
	# Shearing Matrices 
	
	#Shear x in prop to y 
	p4 = Point(2,3,4) 
	shear_transform = shearing(1,0,0,0,0,0)
	assert Tuple.equal(Point(5,3,4), mul_tup(shear_transform, p4))
	# Shear x in prop to z 
	shear_transform = shearing(0,1,0,0,0,0)
	assert Tuple.equal(Point(6,3,4), mul_tup(shear_transform, p4) )
	
	# Shear y in prop to x 
	shear_transform = shearing(0,0,1,0,0,0)
	assert Tuple.equal(Point(2,5,4), mul_tup(shear_transform, p4))
	#Shear y in prop to z 
	shear_transform = shearing(0,0,0,1,0,0)
	assert Tuple.equal(Point(2,7,4), mul_tup(shear_transform, p4))
	
	#Shear z in prop to x 
	shear_transform = shearing(0,0,0,0,1,0) 
	assert Tuple.equal(Point(2,3,6), mul_tup(shear_transform, p4)) 
	# Shear z in prop to y 
	shear_transform = shearing(0,0,0,0,0,1)
	assert Tuple.equal(Point(2,3,7), mul_tup(shear_transform, p4))
	
	# Matrix Transformations 
	p = Point(1,0,1)
	A = rotation('x', math.pi/2)
	B = scaling(5,5,5)
	C = translation(10,5,7)
	# Applying rotation  
	p2 = mul_tup(A, p)
	assert Tuple.equal(Point(1, -1, 0), p2)

	# Applying scaling 
	p3 = mul_tup(B, p2)
	assert Tuple.equal(Point(5, -5, 0), p3)

	# Applying translation 
	p4 = mul_tup(C, p3)
	assert Tuple.equal(Point(15, 0, 7), p4)

	# Chained Transform 
	T = chain_transform(A, B, C)
	p5 = mul_tup(T, p)
	assert Tuple.equal(Point(15, 0, 7), p5)


	



	return 'All matrices test passed'

end = time.monotonic() 
	
print(test_matrices())
time = (end - start)*(10**3)
print(time) 
