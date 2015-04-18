import matplotlib.pyplot as plt
import InitMap
import ReadPath

def addRoundObs():
    for i in InitMap.roundObs:
        circle = plt.Circle((i[0], i[1]), radius = i[2], fc = 'k')
        plt.gca().add_patch(circle)

def addRectObs():
    for i in InitMap.rectObs:
        rect = plt.Rectangle((i[0], i[1]), i[2], i[3], fc = 'k')
        plt.gca().add_patch(rect)

def addPath():
    for i in ReadPath.path:
        circle = plt.Circle(i, radius = InitMap.robotSize, fc = 'r')
        plt.gca().add_addPath(circle)

InitMap.init()
plt.axes()
addRoundObs()
addRectObs()
addPath()
plt.axis('scaled')
plt.show()

