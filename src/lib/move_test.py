from robodk.robolink import *  # API to communicate with RoboDK
from robodk.robomath import *       # import the robotics toolbox


def movement_test(robot):
    # calculate a new approach position 100 mm along the Z axis of the tool with respect to the target
    approach = robot.Pose()*transl(0,0,-10)
    robot.MoveL(approach)               # linear move to the approach position
    original = robot.Pose()*transl(0,0,10)
    robot.MoveL(original) 
    return True