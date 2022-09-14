# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a script file.s
"""
import unittest

def classify_triangle( a: float, b : float, c: float):
    if a <= 0 or b <= 0 or c <= 0:
        return 'NoTriangle'
        raise ValueError("length can't be less than 0")
    #if length is less than zero you don't need to check all the conditions
    else:
       # print(" it's a Triangle")
        Type_of_Triangle(a,b,c)
        return Type_of_Triangle(a, b, c)

        #return True
    
def Type_of_Triangle(a,b,c):
    if a == b and b == c:
        #print(' Equilateral Triangle')
        return 'Equilateral'
    elif (a==b and b!=c) or (b==c and a!=b) or (a==c and a!=b):
        #print(' Isoceles Triangle')
        return 'Isoceles'
    elif (a!=b and b!=c and c!=a) and (a*a == (b*b + c*c)) or (b*b == (a*a + c*c)) or (c*c == (a*a + b*b)):
        #print(' Right angel Triangle')
        return 'Right'
    
    elif a !=b and  a!=c and (a<=b+c and b<=a+c and c<=a+b):
        return 'Scalene'
    elif a>= b+c or b>=a+c or c>=a+b:
        return 'NotATriangle'
    else:
        raise ValueError("you have discovered something new")
    
class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testMyTestSet2(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classify_triangle(10,10,10),'Equilateral','Should be Equilateral')
        self.assertEqual(classify_triangle(10,15,30),'NotATriangle')
        self.assertEqual(classify_triangle(10,12,20), 'Scalene')
    def testMyTestSet3(self):
        self.assertEqual(classify_triangle(3,4,5), 'Right')
        self.assertEqual(classify_triangle(2,4,5), 'Scalene')
    def testMyTestSet4(self):
        self.assertEqual(classify_triangle(2.5,4.5,5), 'Scalene')
        self.assertEqual(classify_triangle(0,4,5), 'NoTriangle')
    def testMyTestSet5(self):
        self.assertEqual(classify_triangle(-2,4,5), 'NoTriangle')
        self.assertEqual(classify_triangle(0,-2,6), 'NoTriangle')


if __name__ == '__main__':
    # examples of running the code
    unittest.main(exit=False)
        