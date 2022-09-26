# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle1 import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(3,3,3), 'Equilateral')
        self.assertEqual(classifyTriangle(3,3,4), 'Isoceles')
    def testScalene(self):
        self.assertEqual(classifyTriangle(3, 5, 7),'Scalene')
    def testIsoceles(self):
        self.assertEqual(classifyTriangle(2,2,3), "Isoceles")
    def testTriangle(self):
        self.assertEqual(classifyTriangle(1.1,2,3),'Scalene')
        self.assertEqual(classifyTriangle(3,5,1),'Scalene')
        
    def testTriangle1(self):
        self.assertEqual(classifyTriangle(-5,3,5),'InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

