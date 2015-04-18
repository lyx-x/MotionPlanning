global roundObs, rectObs, origin, destination, robotSize

def init():
    global roundObs, rectObs, origin, destination, robotSize
    file = open('inputGame', 'r')
    n = int(file.readline())
    s = int(file.readline())
    roundObs = []
    rectObs = []
    for i in range(s):
        obs = tuple(map(int, file.readline().split()))
        if len(obs) == 3:
            roundObs.append(obs)
        else:
            rectObs.append(obs)
    origin = tuple(map(int, file.readline().split()))
    destination = tuple(map(int, file.readline().split()))
    robotSize = int(file.readline())

roundObs = []
rectObs = []
origin = ()
destination = ()
robotSize = 0

