import os
from hillclimber import HILL_CLIMBER

for i in range (1):
    #os.system("python3 mybots/generate.py")
    #os.system("python3 mybots/simulate.py")
    hc = HILL_CLIMBER()
    hc.evolve()
    hc.Show_Best()

