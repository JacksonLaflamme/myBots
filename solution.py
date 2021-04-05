import numpy as np
import time as t
import random
import pyrosim.pyrosim as pyrosim
import os

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = 2*np.random.rand(3,2)-1
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
            pyrosim.Send_Cube(name="Box", pos = [x-3,y-3,z], size = [length,width,height])
            pyrosim.End()
            while not os.path.exists("world.sdf"):
                time.sleep(0.01)

        def Generate_Body():
            length = 1
            width = 1
            height = 1  

            x = 1.5
            y = 0
            z = 1.5

            pyrosim.Start_URDF("body.urdf")
            pyrosim.Send_Cube(name="Torso", pos = [x,y,z], size = [length,width,height])
            pyrosim.Send_Joint( name = "Torso_Back_Leg" , parent= "Torso" , child = "Back_Leg" , type = "revolute", position =  "1.0 0.0 1.0")
            pyrosim.Send_Cube(name="Back_Leg", pos = [-.5,0,-.5], size = [length,width,height])
            pyrosim.Send_Joint( name = "Torso_Front_Leg" , parent= "Torso" , child = "Front_Leg" , type = "revolute", position =  "2.0 0.0 1.0")
            pyrosim.Send_Cube(name="Front_Leg", pos = [.5,0,-.5], size = [length,width,height])
            pyrosim.End()
            while not os.path.exists("body.urdf"):
                time.sleep(0.01)



        def Generate_Brain():
            pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
            pyrosim.Send_Sensor_Neuron(name = 0, linkName="Back_Leg")                
            pyrosim.Send_Sensor_Neuron(name = 1, linkName="Front_Leg")
            pyrosim.Send_Sensor_Neuron(name = 2, linkName="Torso")
            pyrosim.Send_Motor_Neuron(name = 3, jointName="Torso_Back_Leg")
            pyrosim.Send_Motor_Neuron(name = 4, jointName="Torso_Front_Leg")

            for currentRow in range(0,3):
                for currentColumn in range(0,2):
                    pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+2, weight = self.weights[currentRow][currentColumn])

            pyrosim.End()
            while not os.path.exists("brain"+str(self.myID)+".nndf"):
                time.sleep(0.01)


        Create_World()
        Generate_Body()
        Generate_Brain()
        os.system('start /B python3 simulate.py '+ arg + " " + time+" "+str(self.myID))
        
    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            t.sleep(0.01)

        f = open("fitness"+str(self.myID)+".txt","r")
        self.fitness = float(f.read())
        f.close()
        os.system("rm fitness"+str(self.myID)+".txt")

    def Mutate(self):
        randomRow = random.randint(0,2)
        randomColumn = random.randint(0,1)
        self.weights[randomRow, randomColumn] = random.random()*2-1

    def Set_ID(self, ID):
        self.myID = ID
        
