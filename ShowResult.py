import matplotlib.pyplot as plt
import InitMap

def addRoundObs():
    for i in InitMap.roundObs:
        circle = plt.Circle((i[0], i[1]), radius = i[2])
        plt.gca().add_patch(circle)

def addRectObs():
    for i in InitMap.rectObs:
        rect = plt.Rectangle((i[0], i[1]), i[2], i[3], fc='r')
        plt.gca().add_patch(rect)

InitMap.init()
plt.axes()
addRoundObs()
addRectObs()
plt.axis('scaled')
plt.show()

