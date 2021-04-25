import numpy as np
import time as t
import random
import pyrosim.pyrosim as pyrosim
import os
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = 2*np.random.rand(c.numSensorNeurons,c.numMotorNeurons)-1
        self.myID = nextAvailableID


    def Start_Simulation(self, arg, time):
        def Create_World():
            length = 1
            width = 1
            height = 1

            x = 1.5
            y = 0
            z = 1.5

            pyrosim.Start_SDF("world.sdf")
            pyrosim.Send_Cube(name="Box", pos = [-400,0,1.5], size = [1000,3.5,3])
            pyrosim.End()
            while not os.path.exists("world.sdf"):
                time.sleep(0.01)

        def Generate_Body():
            length = 1
            width = 1
            height = 1  

            x = 0
            y = 0
            z = 1

            pyrosim.Start_URDF("body.urdf")
            pyrosim.Send_Cube(name="Torso", pos = [x,y,z+3], size = [length,width,height])
            
            pyrosim.Send_Joint( name = "Torso_Back_Leg" , parent= "Torso" , child = "Back_Leg" , type = "revolute", position =  "0.0 -0.5 4.0", jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="Back_Leg", pos = [0,-0.5,0], size = [0.2,1.0,0.2])
            
            pyrosim.Send_Joint( name = "Torso_Front_Leg" , parent= "Torso" , child = "Front_Leg" , type = "revolute", position =  "0.0 0.5 4.0", jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="Front_Leg", pos = [0,0.5,0], size = [0.2,1,0.2])
            
            pyrosim.Send_Joint(name = "Torso_Left_Leg", parent = "Torso", child = "Left_Leg", type = "revolute", position = "-0.5 0.0 4.0", jointAxis = "0 1 0")
            pyrosim.Send_Cube(name = "Left_Leg", pos = [-0.5, 0.0, 0], size = [1,0.2,0.2]) 
            
            pyrosim.Send_Joint(name = "Torso_Right_Leg", parent = "Torso", child = "Right_Leg", type = "revolute", position = "0.5 0.0 4.0", jointAxis = "0 1 0")
            pyrosim.Send_Cube(name = "Right_Leg", pos = [0.5, 0.0, 0], size = [1,0.2,0.2])

            pyrosim.Send_Joint(name = "Back_Leg_Lower_Back_Leg", parent = "Back_Leg", child = "Lower_Back_Leg", type = "revolute", position = "0 -1 0", jointAxis = "1 0 0")
            pyrosim.Send_Cube(name = "Lower_Back_Leg", pos = [0, 0, -0.5], size = [0.2, 0.2, 1.0])

            pyrosim.Send_Joint(name = "Front_Leg_Lower_Front_Leg", parent = "Front_Leg", child = "Lower_Front_Leg", type = "revolute", position = "0, 1, 0", jointAxis = "1 0 0")
            pyrosim.Send_Cube(name = "Lower_Front_Leg", pos = [0,0,-0.5], size = [0.2, 0.2, 1.0])

            pyrosim.Send_Joint(name = "Left_Leg_Lower_Left_Leg", parent = "Left_Leg", child = "Lower_Left_Leg", type = "revolute", position = "-1 0 0", jointAxis = "0 1 0")
            pyrosim.Send_Cube(name = "Lower_Left_Leg", pos = [0,0,-0.5], size = [0.2, 0.2, 1.0])

            pyrosim.Send_Joint(name = "Right_Leg_Lower_Right_Leg", parent = "Right_Leg", child = "Lower_Right_Leg", type = "revolute", position = "1 0 0", jointAxis = "0 1 0")
            pyrosim.Send_Cube(name = "Lower_Right_Leg", pos = [0,0,-0.5], size = [0.2, 0.2, 1.0])

            pyrosim.End()
            while not os.path.exists("body.urdf"):
                time.sleep(0.01)



        def Generate_Brain():
            pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
            pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Lower_Back_Leg")
            pyrosim.Send_Sensor_Neuron(name = 1, linkName = "Lower_Front_Leg")
            pyrosim.Send_Sensor_Neuron(name = 2, linkName = "Lower_Left_Leg")
            pyrosim.Send_Sensor_Neuron(name = 3, linkName = "Lower_Right_Leg")
            


            pyrosim.Send_Motor_Neuron(name = 4, jointName="Torso_Back_Leg")
            pyrosim.Send_Motor_Neuron(name = 5, jointName="Torso_Front_Leg")
            pyrosim.Send_Motor_Neuron(name = 6, jointName = "Torso_Left_Leg")
            pyrosim.Send_Motor_Neuron(name = 7, jointName = "Torso_Right_Leg")
            pyrosim.Send_Motor_Neuron(name = 8, jointName = "Back_Leg_Lower_Back_Leg")
            pyrosim.Send_Motor_Neuron(name = 9, jointName = "Front_Leg_Lower_Front_Leg")
            pyrosim.Send_Motor_Neuron(name = 10, jointName = "Left_Leg_Lower_Left_Leg")
            pyrosim.Send_Motor_Neuron(name = 11, jointName = "Right_Leg_Lower_Right_Leg")

            for currentRow in range(0,c.numSensorNeurons):
                for currentColumn in range(0, c.numMotorNeurons):
                    pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])

            pyrosim.End()
            while not os.path.exists("brain"+str(self.myID)+".nndf"):
                time.sleep(0.01)


        Create_World()
        Generate_Body()
        Generate_Brain()
        os.system('start /B python simulate.py '+ arg + " " + time+" "+str(self.myID))
        
    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            t.sleep(0.01)

        f = open("fitness"+str(self.myID)+".txt","r")
        self.fitness = float(f.read())
        f.close()
        os.system("rm fitness"+str(self.myID)+".txt")

    def Mutate(self):
        randomRow = random.randint(0,c.numSensorNeurons-1)
        randomColumn = random.randint(0,c.numMotorNeurons-1)
        self.weights[randomRow, randomColumn] = random.random()*2-1

    def Set_ID(self, ID):
        self.myID = ID
        
