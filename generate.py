import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[5, 5, .5], size=[1, 1, 1])
    pyrosim.End()
    
def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[1, 1, 1])
    ## Joints should not be in the same spot possibly, since links are not in same spot
    ## Reconsider the posiitoning of the joints and adjust links as needed
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-.5, 0, 1])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [.5, 0, 1])

    ## x, y, z. X runs across the screen, y runs "into" the screen and z runs up and down. Links are spaced on y axis, adjust x to adjust joints on face of link0
    ## Adjust y to adjust joint "depth" in link0, different from z to adjust joint height. Height is the only one I'm fairly certain is correct 
    pyrosim.Send_Cube(name ="BackLeg",pos=[-.5, 0, -.5], size=[1, 1, 1] )
    pyrosim.Send_Cube(name ="FrontLeg",pos=[.5, 0, -.5], size=[1, 1, 1] )
    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

    pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 1 )
    pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight =1 )
    pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = .5 )
    pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight =.5 )

    


    pyrosim.End()


    

Create_World()
Generate_Body()
Generate_Brain()
