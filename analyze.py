import matplotlib
import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load(r"C:\Users\Nick\mybots\data\backLegSensorValues.npy")
frontLegSensorValues = numpy.load(r"C:\Users\Nick\mybots\data\frontLegSensorValues.npy")

matplotlib.pyplot.plot(backLegSensorValues, label = "Back Leg", linewidth = 3)
matplotlib.pyplot.plot(frontLegSensorValues, label = "Front Leg", lw = 1.5)

matplotlib.pyplot.legend()
matplotlib.pyplot.show()