from robodk.robolink import *  # API to communicate with RoboDK
from robodk.robomath import *       # import the robotics toolbox

from robodk import *
from robolink import *

class Moves:
    robot: Item
    
    def __init__(self, robot: Item):
        self.robot = robot
        return None

    def movement_test(self):
        """
        #### Realiza un pequeño movimiento en el brazo.
        ----------
        Requiere:
            - Item del robot(self.robot).
        """
        # calculate a new approach position 100 mm along the Z axis of the tool with respect to the target
        approach = self.robot.Pose()*transl(0,0,-10)
        self.robot.MoveL(approach)               # linear move to the approach position
        original = self.robot.Pose()*transl(0,0,10)
        self.robot.MoveL(original) 
        print("INF: Movimiento realizado")
        return True