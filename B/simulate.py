import sys
from simulation import SIMULATION

directOrGUI = sys.argv[1]
time = sys.argv[2]
solutionID = sys.argv[3]

simulation = SIMULATION(directOrGUI, time, solutionID)
simulation.Run()
simulation.Get_Fitness()

