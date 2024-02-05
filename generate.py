import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[5, 5, .5], size=[1, 1, 1])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Link0", pos=[0, 0, 1.5], size=[1, 1, 1])
    ## Joints should not be in the same spot possibly, since links are not in same spot
    ## Reconsider the posiitoning of the joints and adjust links as needed
    pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [-.5, 0, 1])
    pyrosim.Send_Joint( name = "Link0_Link2" , parent= "Link0" , child = "Link2" , type = "revolute", position = [.5, 0, 1])

    ## x, y, z. X runs across the screen, y runs "into" the screen and z runs up and down. Links are spaced on y axis, adjust x to adjust joints on face of link0
    ## Adjust y to adjust joint "depth" in link0, different from z to adjust joint height. Height is the only one I'm fairly certain is correct 
    pyrosim.Send_Cube(name ="Link1",pos=[-.5, 0, -.5], size=[1, 1, 1] )
    pyrosim.Send_Cube(name ="Link2",pos=[.5, 0, -.5], size=[1, 1, 1] )
     
    pyrosim.End()

Create_World()
Create_Robot()