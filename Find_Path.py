'''
Created on Apr 18, 2015

@author: czx
'''
class Point:
    def __init__(self, x, y, w, p):
        self.x = x
        self.y = y
        self.w = w
        self.p = p

def input_file():
    global n,Plan,start,end,direction,ballr
    f = open('input','r')
    n = int(f.readline())
    Plan = [([0 for x in range(n)]) for y in range(n)]
    k = int(f.readline())
    for i in range(k):
        s = f.readline()
        l = [int(x) for x in s.split(' ')]
        if (len(l) == 3):
            for i in range(-l[2],l[2]+1):
                for j in range(-l[2],l[2]+1):
                    if ((i * i + j * j) <= l[2] * l[2] and (l[0] + i) >= 0 and (l[0] + i) < n and (l[1] + j) >= 0 and l[1] + j < n):
                        Plan[l[0]+i][l[1]+j] = 1
        else:
            for i in range(l[0],l[0]+l[3]):
                for j in range(l[1],l[1]+l[2]):
                    Plan[i][j] = 1;

    l = f.readline().split(' ')
    start = Point(int(l[0]),int(l[1]),0,-1)
    l = f.readline().split(' ')
    end = Point(int(l[0]),int(l[1]),0,-1)
    ballr = int(f.readline())
    direction = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    return;


def print_path( h ):
    global n,s,Plan,start,end,direction,D,l,ballr
    p = l[h-1];
    f = open('outputPath','w')
    while p.p != -1:
        f.write(str(p.x)+' '+str(p.y)+'\n')
        p = l[p.p - 1]
    return;
      
def check(x,y):
    global n,s,Plan,start,end,direction,D,l,ballr
    for i in range(x - ballr,x+ballr + 1):
        for j in range(y - ballr,y+ballr + 1):
            if (i>=0 and j>=0 and i<n and j<n):
                if Plan[i][j]!=0:
                    return False
    return True;
                   
def find():
    global n,s,Plan,start,end,direction,D,l
    l = [start]
    D = [([0 for x in range(n)]) for y in range(n)]
    D[start.x][start.y] = 1
    find = 0
    h = 1
    refresh = True
    while refresh and find == 0:
        refresh = False
        for i in range(n):
            for j in range(n):
                for p in direction:
                    if (check(i,j) and i + p[0] >=0 and i + p[0] < n and j + p[1] >=0 and j + p[1] < n):
                        r = D[i+p[0]][j+p[1]]
                        if r != 0:
                            if D[i][j] == 0:
                                l.insert(h,Point(i,j,l[r-1].w+1,r))
                                h = h + 1
                                D[i][j] = h
                                refresh = True
                            elif l[D[i][j]- 1].w > l[r-1].w + 1:
                                l[D[i][j] - 1].w = l[r-1].w + 1
                                l[D[i][j] - 1].p = r
                                refresh = True
                            if i == end.x and j == end.y:
                                print_path(h)
                                find = 1
    if find != 1:
        print "No solution!"
    return;

global n,s,Plan,start,end,direction,D,l                                  
input_file()
find()
        
        