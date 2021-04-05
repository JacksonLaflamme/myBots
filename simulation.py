import pybullet as p
import pybullet_data
import time
from world import WORLD
from robot import ROBOT
import constants as c
class SIMULATION():
    def __init__(self,arg,time, simulationID):
        if arg == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        if arg == "GUI":
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.time = float(time)


        self.world = WORLD()
        self.robot = ROBOT(simulationID)

    def Run(self):
        for i in range(0,c.iterations):
            
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            time.sleep(self.time)

    def Get_Fitness(self):
            self.robot.Get_Fitness()


    def __del__(self):

        p.disconnect()
