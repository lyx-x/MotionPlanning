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
    f = open('inputGame','r')
    n = int(f.readline())
    Plan = [([0 for x in range(n)]) for y in range(n)]
    k = int(f.readline())
    for i in range(k):
        s = f.readline()
        l = [int(x) for x in s.split(' ')]
        if (len(l) == 3):
            for i in range(-l[2]+1,l[2]):
                for j in range(-l[2]+1,l[2]):
                    if ((i * i + j * j) <= l[2] * l[2] and (l[0] + i) >= 0 and (l[0] + i) < n and (l[1] + j) >= 0 and l[1] + j < n):
                        Plan[l[0]+i][l[1]+j] = 1
        else:
            for i in range(l[0],l[0]+l[2]):
                for j in range(l[1],l[1]+l[3]):
                    Plan[i][j] = 1;

    l = f.readline().split(' ')
    end = Point(int(l[0]),int(l[1]),0,-1)
    l = f.readline().split(' ')
    start = Point(int(l[0]),int(l[1]),0,-1)
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
    for i in range(x -int(ballr/2)-1,x+int(ballr/2)+1 ):
        for j in range(y-int(ballr/2)-1,y+int(ballr/2)+1 ):
            if (i>=0 and j>=0 and i<n and j<n):
                if Plan[i][j]!=0:
                    return 1
    return 0;
                   
def find():
    global n,s,Plan,start,end,direction,D,l,ch
    l = [start]
    D = [([0 for x in range(n)]) for y in range(n)]
    ch = [([0 for x in range(n)]) for y in range(n)]
    for i in range(n):
        for j in range(n):
            ch[i][j] = check(i,j)
    D[start.x][start.y] = 1
    find = 0
    t = 1
    h = 0
    refresh = True
    while refresh and find == 0:
        refresh = False
        for u in range(h,t):
            for k in range(8):
                i = l[u].x + direction[k][0]
                j = l[u].y + direction[k][1]
                add = abs(direction[k][0])+abs(direction[k][1])
                if (i >=0 and j >=0 and i<n and j<n and ch[i][j] == 0):
                    r = D[i][j]
                    if r == 0:
                        l.append(Point(i,j,l[u].w+add,D[l[u].x][l[u].y]))
                        t = t + 1
                        D[i][j] = t
                        refresh = True
                    elif l[r - 1].w > l[u].w + add:
                        l[r - 1].w = l[u].w + add
                        l[r - 1].p = D[l[u].x][l[u].y]
                        refresh = True
                    if i == end.x and j == end.y:
                        print_path(t)
                        find = 1
        h = h + 1
    if find != 1:
        print ("No solution!")
    return;

global n,s,Plan,start,end,direction,D,l                                  
input_file()
find()
        
        
