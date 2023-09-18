# -*- coding: utf-8 -*-
"""
Create - Matrices  
"""
# TODO: In second iteration of matricies write an implementation without numpy 

import numpy as np 

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
    
    # HOWTO: Handle tuple multiplication 
    M6 = np.array([[1,2,3,4],[2,4,4,2],[8,6,4,1],[0,0,0,1]])
    b = (1,2,3,1)
    assert  np.allclose(M6@b, np.array([18,24,33,1]))
    
    # Identity matrix
    M7 = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
    identity = np.identity(4)
    assert np.allclose(M7 @ identity, M7)
    
    # Transposing of matrix 
    M8 = np.array([[0,9,3,0],[9,8,0,8],[1,8,5,3],[0,0,5,8]])
    M9 = np.transpose(M8)
    assert np.allclose(M9, np.array([[0,9,1,0],[9,8,8,0],[3,0,5,5],[0,8,3,8]]))
    assert np.allclose(identity, np.transpose(identity))
    
    # Inverting Matrices 
    # Testing if a matrix can be invertible -- via determinant 
	M10 = np.array([[6,4,4,4],[5,5,7,6],[4,-9,3,7],[9,1,7,-6]])
	assert np.linalg.det(M10) == -2120 
    
    return 'All matrices test passed'
    
    
print(test_matrices())
    
