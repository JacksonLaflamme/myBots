import os
import numpy as np
import time
import matplotlib.pyplot

os.system('cd ../A && python search.py')
os.system('cd ../B && python search.py')



fitnessesA = np.load('../A/fitnessesA.npy')
fitnessesB = np.load('../B/fitnessesB.npy')

for i in fitnessesA:
    matplotlib.pyplot.plot(i)

for j in fitnessesB:
    matplotlib.pyplot.plot(j, linestyle = ':')
matplotlib.pyplot.title("Fitness")
matplotlib.pyplot.show()

avgFitnessA = np.mean(fitnessesA, axis=0)
avgFitnessB = np.mean(fitnessesB, axis = 0)

matplotlib.pyplot.plot(avgFitnessA)
matplotlib.pyplot.plot(avgFitnessB, linestyle = ':')
matplotlib.pyplot.title("Average Fitness")
matplotlib.pyplot.show()

SDA = np.std(fitnessesA, axis=0)
SDB = np.std(fitnessesB, axis=0)

matplotlib.pyplot.plot(avgFitnessA-SDA)
matplotlib.pyplot.plot(avgFitnessA)
matplotlib.pyplot.plot(avgFitnessA+SDA)

matplotlib.pyplot.plot(avgFitnessB-SDB, linestyle = ':')
matplotlib.pyplot.plot(avgFitnessB, linestyle = ':')
matplotlib.pyplot.plot(avgFitnessB+SDB, linestyle = ':')

matplotlib.pyplot.title("Fitness Rainbows")
matplotlib.pyplot.show()


