import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
BackLegTargetAngles = numpy.load("data/BackLegTargetAngles.npy")
FrontLegTargetAngles = numpy.load("data/FrontLegTargetAngles.npy")

##matplotlib.pyplot.plot(frontLegSensorValues, label = "Front Leg", linewidth = 4)
##matplotlib.pyplot.plot(backLegSensorValues, label = "Back Leg")
matplotlib.pyplot.plot(BackLegTargetAngles)
matplotlib.pyplot.plot(FrontLegTargetAngles)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
