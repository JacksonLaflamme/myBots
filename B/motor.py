import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        if(self.jointName == "Torso_Front_Leg"):
            self.amplitude = c.FrontLegAmplitude
            self.frequency = c.FrontLegFrequency
            self.offset = c.FrontLegPhaseOffset
            self.motorValues = (np.sin((self.frequency*np.linspace(-np.pi,np.pi, 1000))+self.offset))*(self.amplitude)
        else:
            self.amplitude = c.BackLegAmplitude
            self.frequency = c.BackLegFrequency
            self.offset = c.BackLegPhaseOffset
            self.motorValues = (np.sin((self.frequency*np.linspace(-np.pi,np.pi, 1000))+self.offset))*(self.amplitude)


    def Set_Value(self,desiredAngle,robot):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = desiredAngle , maxForce = c.maxForce)


    def Save_Values(self):
        np.save("data/"+ self.jointName+".npy", self.motorValues)
