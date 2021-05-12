from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
    
    def Evaluate(self, solutions):
        for i in range(0, c.populationSize):
            solutions[i].Start_Simulation("DIRECT","0.0")
        for i in range(0, c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()


    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(0, c.numberOfGenerations):
               self.Evolve_For_One_Generation()
        

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        
        

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()


    def Select(self):
        for i in self.parents:
            if self.parents[i].fitness>self.children[i].fitness:
                self.parents[i] = self.children[i]

    def Print(self):
        print("\n")
        for i in self.parents:
            print(str(self.parents[i].fitness)+"  "+str(self.children[i].fitness))
        print("\n")

    def Show_Best(self):
        minfitness = 100000000
        minidx = -1
        for i in self.parents:
            if self.parents[i].fitness<minfitness:
                minfitness = self.parents[i].fitness
                minidx = i
        self.parents[minidx].Start_Simulation("GUI", "0.0005")
        print(minfitness)
