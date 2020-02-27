import unittest
import Ball
import Brick
import numpy
from Simples import AABB
from Simples import BVH

class Test(unittest.TestCase):

    def test_0vTrue(self):
        ball = Ball.Ball(numpy.array([0,0]), numpy.array([0,0]))
        brick = Brick.Brick(numpy.array([0,0]),1,1)
        intersections = brick.intersect(ball)
        self.assertTrue([intersections[0].t, intersections[0].t] == [0,0], "Expected: " + str([0,0]) + " Got: " + str([intersections[0].t, intersections[0].t]))

    def test_0vFalse(self):
        ball = Ball.Ball(numpy.array([10,10]), numpy.array([0,0]))
        brick = Brick.Brick(numpy.array([0,0]),1,1)
        self.assertTrue(brick.intersect(ball) == [])

    def test_TopDownTrue(self):
        ball = Ball.Ball(numpy.array([0,1]), numpy.array([0,-1]))
        brick = Brick.Brick(numpy.array([0,0]),1,1)
        self.assertTrue(brick.intersect(ball) == [0.5,1.5], "Expected: " + str([0.5,1.5]) + " Got: " + str(brick.intersect(ball)))

    def test_BottomUpTrue(self):
        ball = Ball.Ball(numpy.array([0,-1]), numpy.array([0,1]))
        brick = Brick.Brick(numpy.array([0,0]),1,1)
        self.assertTrue(brick.intersect(ball) == [0.5,1.5], "Expected: " + str([0.5,1.5]) + " Got: " + str(brick.intersect(ball)))

    def test_LeftRightTrue(self):
        ball = Ball.Ball(numpy.array([-1,0]), numpy.array([1,0]))
        brick = Brick.Brick(numpy.array([0,0]),1,1)
        self.assertTrue(brick.intersect(ball) == [0.5,1.5], "Expected: " + str([0.5,1.5]) + " Got: " + str(brick.intersect(ball)))

    def test_RightLeftTrue(self):
        ball = Ball.Ball(numpy.array([1,0]), numpy.array([-1,0]))
        brick = Brick.Brick(numpy.array([0,0]),1,1)
        self.assertTrue(brick.intersect(ball) == [0.5,1.5], "Expected: " + str([0.5,1.5]) + " Got: " + str(brick.intersect(ball)))

    def test_UpperRightTrue(self):
        ball = Ball.Ball(numpy.array([1,1]), numpy.array([-1,-1]))
        brick = Brick.Brick(numpy.array([0,0]),1,1)
        intersections = brick.intersect(ball)
        self.assertTrue([intersections[0].t,intersections[1].t] == [0.5,1.5], "Expected: " + str([0.5,1.5]) + " Got: " + str([intersections[0].t,intersections[1].t]))

    def test_UpperLeftTrue(self):
        ball = Ball.Ball(numpy.array([-1,1]), numpy.array([1,-1]))
        brick = Brick.Brick(numpy.array([0,0]),1,1)
        intersections = brick.intersect(ball)
        self.assertTrue([intersections[0].t, intersections[1].t] == [0.5,1.5], "Expected: " + str([0.5,1.5]) + " Got: " + str([intersections[0].t,intersections[1].t]))


    def test_bhv(self):
        simples = [AABB.AABB(numpy.array([0, 0]), 1, 1), AABB.AABB(numpy.array([5, 5]), 1, 1)]
        a = BVH.bvh(simples)
        a.divide()
        print(a.elements)