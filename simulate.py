import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

amplitudeFront = numpy.pi /4
frequencyFront = 10
phaseOffsetFront = numpy.pi

amplitudeBack = numpy.pi /4
frequencyBack = 10
phaseOffsetBack = numpy.pi

motor_valsFront = numpy.linspace(0, 2*numpy.pi, 1000)
motor_valsBack = numpy.linspace(0, 2*numpy.pi, 1000)


sin_motor_valsFront = amplitudeFront * numpy.sin(frequencyFront * motor_valsFront + phaseOffsetFront)
sin_motor_valsBack = amplitudeBack * numpy.sin(frequencyBack * motor_valsBack + phaseOffsetBack)

numpy.save(r"C:\Users\Nick\mybots\data\front_motor_vals.npy", sin_motor_valsFront)
numpy.save(r"C:\Users\Nick\mybots\data\back_motor_vals.npy", sin_motor_valsBack)
#numpy.save(r"C:\Users\Nick\mybots\data\sinMotorVals", sin_motor_vals)

for i in range(1000):
    p.stepSimulation()
    #backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Link2")
    #frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Link1")
    
    pyrosim.Set_Motor_For_Joint(bodyIndex = 1, jointName = b'Link0_Link2', controlMode = p.POSITION_CONTROL, targetPosition = sin_motor_valsBack[i], maxForce = 50)
    pyrosim.Set_Motor_For_Joint(bodyIndex = 1, jointName = b'Link0_Link1', controlMode = p.POSITION_CONTROL, targetPosition = sin_motor_valsFront[i], maxForce = 50)

   
    time.sleep(1/40)

p.disconnect()
