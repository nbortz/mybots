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
            
            for neuronName in self.nn.Get_Neuron_Names():
                #print("neuron name: ", neuronName)
                
                if self.nn.Is_Motor_Neuron(neuronName):
                
                    self.jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                    desiredAngle = self.nn.Get_Value_Of(neuronName)
                    #print("self motors", self.motors[self.jointName])
                    self.motors[bytes(self.jointName, 'ASCII')].Set_Value(desiredAngle, self.robotId)
                    # if self.jointName in self.motors:
                    #     #error in act, this if is not triggering
                    #     #set value is not being called here
                    #     print("self.motors: ", self.motors)
                    # self.motors[jointName].Set_Value(desiredAngle, self.robotId)
                    
            
        def Think(self):
             self.nn.Update()
        
        def Get_Fitness(self):
             stateOfLink0 = p.getLinkState(self.robotId,0)
             positionOfLink0 = stateOfLink0[0]
             xCoordinateLink0 = positionOfLink0[0]

             with open("mybots/fitness.txt", "w") as file:
                file.write(f"{str(xCoordinateLink0)}")