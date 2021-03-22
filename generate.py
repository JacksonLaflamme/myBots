import random
import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 1.5
y = 0
z = 1.5

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos = [x-3,y-3,z], size = [length,width,height])
    pyrosim.End()

def Generate_Body():
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
    
    for i in range(0,3):
        for j in range(3,5):
            pyrosim.Send_Synapse(sourceNeuronName = i, targetNeuronName = j, weight = (2*random.random())-1)

    pyrosim.End()



Create_World()
Generate_Body()
Generate_Brain()
