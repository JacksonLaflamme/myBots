import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
planeId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = numpy.zeros(1000)

for i in range(0,1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Back_Leg")
    time.sleep(1/60)
numpy.save("data/sensorValues.npy", backLegSensorValues)
print(backLegSensorValues)
p.disconnect()
