import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time

class SOLUTION:
    def __init__(self, ID):
        self.weights = np.random.rand(3, 2) * 2 - 1
        self.myID = ID

    def Create_World(self):
        pyrosim.Start_SDF("mybots/world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[5, 5, .5], size=[1, 1, 1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[-.5, 0, 1])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[.5, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5], size=[1, 1, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5], size=[1, 1, 1])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        sensor_neurons = [0, 1, 2]
        motor_neurons = [3, 4]
        for i, linkName in enumerate(["Torso", "BackLeg", "FrontLeg"]):
            pyrosim.Send_Sensor_Neuron(name=sensor_neurons[i], linkName=linkName)
        for i, jointName in enumerate(["Torso_BackLeg", "Torso_FrontLeg"]):
            pyrosim.Send_Motor_Neuron(name=motor_neurons[i], jointName=jointName)
        for currentRow in range(3):
            for currentColumn in range(2):
                weight = self.weights[currentRow][currentColumn]
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + 3, weight=weight)
        pyrosim.End()

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system(f"start /B python3 mybots/simulate.py {directOrGUI} {self.myID}")

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = f"mybots/fitness{self.myID}.txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        with open(fitnessFileName, "r") as file:
            self.fitness = float(file.readline())
        try:
            os.remove(fitnessFileName)
        except FileNotFoundError:
            print(f"Fitness file not found for deletion: {fitnessFileName}")
        except Exception as e:
            print(f"Error deleting fitness file: {fitnessFileName}")
            print(f"Exception: {str(e)}")
    def Mutate(self):
        row = random.randint(0, 2)
        column = random.randint(0, 1)
        self.weights[row, column] = np.random.rand() * 2 - 1

    def Set_ID(self, ID):
        self.myID = ID

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        
        os.system(f"start /B python3 simulate.py {directOrGUI} {self.myID}")
        
        fitnessFileName = f"mybots/fitness{self.myID}.txt"
        print(f"Waiting for fitness file: {fitnessFileName}")
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        print(f"Fitness file found: {fitnessFileName}")
        
        with open(fitnessFileName, "r") as fitnessFile:
            self.fitness = float(fitnessFile.readline())
        print(f"Fitness value read: {self.fitness}")
        
        try:
            os.remove(fitnessFileName)
            print(f"Fitness file deleted: {fitnessFileName}")
        except FileNotFoundError:
            print(f"Fitness file not found for deletion: {fitnessFileName}")
        except Exception as e:
            print(f"Error deleting fitness file: {fitnessFileName}")
            print(f"Exception: {str(e)}")