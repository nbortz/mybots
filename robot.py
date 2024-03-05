from sensor import SENSOR
from motor import MOTOR
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random
import pybullet as p
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
        def __init__(self): 
            self.robotId = p.loadURDF("body.urdf")
            self.nn = NEURAL_NETWORK("brain.nndf")
            pyrosim.Prepare_To_Simulate(self.robotId)
            self.Prepare_To_Sense()
            self.Prepare_To_Act()
        
        def Prepare_To_Sense(self):
            self.sensors = {}
            for linkName in pyrosim.linkNamesToIndices:
                self.sensors[linkName] = SENSOR(linkName)

        def Sense(self, i):
            for sensor in self.sensors.values():
                 sensor.Get_Value(i)

        def Prepare_To_Act(self):
                    self.motors = {}
                    for jointName in pyrosim.jointNamesToIndices:
                        self.motors[jointName] = MOTOR(jointName, self.robotId)

        def Act(self):
            for neuronName in self.nn.neurons:  # Directly iterate over neuron names
                if self.nn.Is_Motor_Neuron(neuronName):
                    jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                    #print(jointName)
                    desiredAngle = self.nn.Get_Value_Of(neuronName)
                    # Now, directly use the desiredAngle for the specific motor
                    #print(self.motors)
                    for motor in self.motors.values():
                        motor.Set_Value(desiredAngle)

                    
            
        def Think(self):
             self.nn.Update()
             self.nn.Print()
        
             
