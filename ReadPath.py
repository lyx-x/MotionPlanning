global path;

def readPath():
    file = open('outputPath', 'r')
    for line in file:
        path.append(tuple(map(int, line.split())))

path = []