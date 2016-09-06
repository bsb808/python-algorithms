
# Size of space
N = 200
NodeWidth = 2
NodeCenter = (100,100)
NodeOrient = 0
def make_square(center,width,orient):
    walls = []
    for ii in range(width):
        for jj in range(width):
            xx = center[0]-width/2+ii
            yy = center[1]-width/2+jj
            print (xx,yy)
            walls.append((xx,yy))

make_square(NodeCenter,NodeWidth,NodeOrient)
#a.init_grid(N,N, tuple(walls), start, end)
