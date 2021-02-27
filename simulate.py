import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

BackLegAmplitude = np.pi/4
BackLegFrequency = 10
BackLegPhaseOffset = 0

FrontLegAmplitude = np.pi/4
FrontLegFrequency = 10
FrontLegPhaseOffset = 0


physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

BackLegTargetAngles = (np.sin((BackLegFrequency*np.linspace(-np.pi,np.pi, 1000))+BackLegPhaseOffset))*(BackLegAmplitude)
FrontLegTargetAngles = (np.sin((FrontLegFrequency*np.linspace(-np.pi,np.pi, 1000))+FrontLegPhaseOffset))*(FrontLegAmplitude)

##np.save("data/BackLegTargetAngles.npy", BackLegTargetAngles)
##np.save("data/FrontLegTargetAngles.npy", FrontLegTargetAngles)
##exit()

for i in range(0,1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Back_Leg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Front_Leg")

    ##Motor one
    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_Back_Leg", controlMode = p.POSITION_CONTROL, targetPosition = BackLegTargetAngles[i] , maxForce = 25) 
    
    ##Motor Two
    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_Front_Leg", controlMode = p.POSITION_CONTROL, targetPosition = FrontLegTargetAngles[i] , maxForce = 25)
    time.sleep(1/60)

numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
p.disconnect()
