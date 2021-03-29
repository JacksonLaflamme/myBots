import sys
from simulation import SIMULATION

directOrGUI = sys.argv[1]
time = sys.argv[2]

simulation = SIMULATION(directOrGUI, time)
simulation.Run()
simulation.Get_Fitness()

