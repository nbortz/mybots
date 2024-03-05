from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim


class SIMULATION:
        def __init__(self): 
            
            self.physicsClient = p.connect(p.GUI)
            p.setAdditionalSearchPath(pybullet_data.getDataPath())
            p.setGravity(0,0,-9.8)
            self.world = WORLD()
            self.robot = ROBOT()

            
        def Run(self):
              for i in range(1000):
                    p.stepSimulation()
                    self.robot.Sense(i)
                    self.robot.Think()
                    self.robot.Act()
                    

                
                    time.sleep(1/40)

        def __del__(self):
              p.disconnect()
