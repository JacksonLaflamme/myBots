import numpy as np
import random
import pyrosim.pyrosim as pyrosim
import os

class SOLUTION:
    def __init__(self):
        self.weights = 2*np.random.rand(3,2)-1


    def Evaluate(self,arg, time):
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


        def Generate_Brain():
            pyrosim.Start_NeuralNetwork("brain.nndf")
            pyrosim.Send_Sensor_Neuron(name = 0, linkName="Back_Leg")
            pyrosim.Send_Sensor_Neuron(name = 1, linkName="Front_Leg")
            pyrosim.Send_Sensor_Neuron(name = 2, linkName="Torso")
            pyrosim.Send_Motor_Neuron(name = 3, jointName="Torso_Back_Leg")
            pyrosim.Send_Motor_Neuron(name = 4, jointName="Torso_Front_Leg")

            for currentRow in range(0,3):
                for currentColumn in range(0,2):
                    pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+2, weight = self.weights[currentRow][currentColumn])

            pyrosim.End()

        Create_World()
        Generate_Body()
        Generate_Brain()
        os.system('py simulate.py '+ arg + " " + time)
        f = open("fitness.txt","r")
        self.fitness = float(f.read())

    def Mutate(self):
        randomRow = random.randint(0,2)
        randomColumn = random.randint(0,1)
        self.weights[randomRow, randomColumn] = random.random()*2-1


