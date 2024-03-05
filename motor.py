import pyrosim.pyrosim as pyrosim
import constants as c
import numpy
import pybullet as p
import math

class MOTOR:
        def __init__(self, jointName, robotId): 
            self.jointName = jointName
            self.robotId = robotId
        
        def Set_Value(self, desiredAngle):
             print("setting value")
             pyrosim.Set_Motor_For_Joint(bodyIndex = self.robotId, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = desiredAngle, maxForce = 50)

        def Save_Sensor_Values(self):
            numpy.save(r"C:\Users\Nick\mybots\data\motorVals.npy", self.motor_vals)

