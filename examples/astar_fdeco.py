import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'algorithms'))
import a_star_path_finding as pf
reload(pf)
import astar_utils as autils
reload(autils)

# Size of space
N = 21

W= 3  # should be odd
Nc = 5  # number of blocks
centers=[]
orient=0.0
start = (0,0)
end= (N-1,N-1)
walls = []

if False:
    for ii in range(Nc):
        w = W/2
        center=(randint(w,N-2),randint(w,N-2))
        alls = autils.make_square(center,W,orient)
        if (not end in alls) and (not start in alls):
            walls += alls
        else:
            print "wall start/end conflict"
else:
    centers = [(7,5),(3,7),(10,11),(17,9),(16,15)]
    for c in centers:
        sq = autils.make_square(c,W,orient)
        walls += sq


a = pf.AStar()
a.init_grid(N,N, tuple(walls), start, end)

# add cost around blocks
for c in centers:
    sq = autils.make_square(c,W,orient)
    added= []
    for s in sq:
        cell = a.get_cell(*s)            
        for adj in a.get_surrounding_cells(cell):
            if not adj in added:
                added.append(adj)
                adj.c += 1.0

    for s in sq:
        cell = a.get_cell(*s)
        for adj in a.get_surrounding_cells(cell):
            if adj.reachable:
                for aadj in a.get_surrounding_cells(adj):
                    if not aadj in added:
                        added.append(aadj)
                        aadj.c += 0.5

path,cnt = a.solve(animate=True)
fname = ("anime/test%04d.png"%cnt)
autils.plotAstar(a,path,anime=True,fname=fname)

from subprocess import call
ofname = fname
for ii in range(40):
    cnt+=1
    fname = ("anime/test%04d.png"%cnt)
    print 'cp %s to %s'%(ofname,fname)
    call(['cp',ofname,fname])
show()
