import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os

class SOLUTION:
    def __init__(self):
        # Initialize the weights as a 3x2 matrix with values in the range of -1 to 1
        self.weights = np.random.rand(3, 2) * 2 - 1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
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
        pyrosim.Start_NeuralNetwork("brain.nndf")
        sensor_neurons = [0, 1, 2]  # Sensor Neurons
        motor_neurons = [3, 4]  # Motor Neurons

        # Send Sensor Neurons
        for i, linkName in enumerate(["Torso", "BackLeg", "FrontLeg"]):
            pyrosim.Send_Sensor_Neuron(name=sensor_neurons[i], linkName=linkName)

        # Send Motor Neurons
        for i, jointName in enumerate(["Torso_BackLeg", "Torso_FrontLeg"]):
            pyrosim.Send_Motor_Neuron(name=motor_neurons[i], jointName=jointName)

        # Iterate over the rows and columns of the weight matrix
        for currentRow in range(3):  # Iterates over 0, 1, 2 corresponding to the three sensor neurons
            for currentColumn in range(2):  # Iterates over 0, 1 corresponding to the two motor neurons
                # Correctly reference the weight using square brackets
                weight = self.weights[currentRow][currentColumn]
                # Adjust sourceNeuronName to currentRow and targetNeuronName to currentColumn + 3
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + 3, weight=weight)

        pyrosim.End()

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 mybots/simulate.py " + directOrGUI)
        with open("mybots/fitness.txt", "r") as file:
            self.fitness = float(file.readline())

    def Mutate(self):
        # Choose a random row (corresponding to one of the three sensor neurons)
        row = random.randint(0, 2)
        # Choose a random column (corresponding to one of the two motor neurons)
        column = random.randint(0, 1)
        # Apply a mutation to the selected weight
        self.weights[row, column] = np.random.rand() * 2 - 1