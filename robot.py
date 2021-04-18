from motor import MOTOR
from sensor import SENSOR
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c
class ROBOT:
    def __init__(self, simulationID):
        self.myID = simulationID
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain"+str(simulationID)+".nndf")
        os.system("rm brain"+str(self.myID)+".nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self,t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self,t):
        #for i in self.motors:
        #    self.motors[i].Set_Value(t, self.robot)
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)*c.motorJointRange
                self.motors[jointName].Set_Value(desiredAngle, self.robot)

    def Think(self):
        self.nn.Update()

    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        xCoordinateOfLinkZero = basePosition[2]
        #stateOfLinkZero=p.getLinkState(self.robot,0)
        #positionOfLinkZero=stateOfLinkZero[0]
        #xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open("tmp"+str(self.myID)+".txt","w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.system("rename tmp"+str(self.myID)+".txt fitness"+str(self.myID)+".txt")
