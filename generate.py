import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

# Initial dimensions
initial_length = 1
initial_width = 1
initial_height = 1

for j in range(5):  # Rows in the grid
    for k in range(5):  # Columns in the grid
        # Reset the base position for each tower
        x = j * initial_width  # No need to recalculate these each loop
        y = k * initial_length
        z = 0.5

        # Reset dimensions for each tower
        loopLength = initial_length
        loopWidth = initial_width
        loopHeight = initial_height

        for i in range(10):  # Blocks in each tower
            name = f"Box_{j}_{k}_{i}"  # Unique name for each cube
            pyrosim.Send_Cube(name=name, pos=[x, y, z], size=[loopLength, loopWidth, loopHeight])
            z += loopHeight  # Move up for the next block
            # Decrease dimensions for the next block within the same tower
            loopLength *= 0.9
            loopWidth *= 0.9
            loopHeight *= 0.9

pyrosim.End()
