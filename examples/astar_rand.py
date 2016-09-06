import algorithms.a_star_path_finding as pf
import astar_utils as autils
reload(autils)

cnt=0
pmax=0
for jj in range(1000):
    a = pf.AStar()
    N = 100
    walls = []
    start = (0,0)
    end= (N-1,N-1)
    for ii in range(int((N**2)*.75)):
        w = (randint(0,N),randint(0,N))
        if (w==start) or (w==end):
            pass
        else:
            walls.append(w)

    a.init_grid(N,N, tuple(walls), start, end)
    path = a.solve()
    
    if not(path is None):
        cnt+=1
        if len(path) > pmax:
            pmax=len(path)
            fig=figure(jj)
            clf()
            autils.plotAstar(a,path)

show()
print cnt
