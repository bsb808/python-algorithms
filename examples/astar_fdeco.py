import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'algorithms'))
import a_star_path_finding as pf
reload(pf)
import astar_utils as autils
reload(autils)

from subprocess import call

close('all')

movie=True

# Size of space
N = 21#201
M =1 # multiplier
W= 1#11#3  # should be odd
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
    #centers = [(7,5),(3,7),(10,11),(17,9),(16,15)]
    #centers.append((11.9,9.4))
    #centers.append((8.5,11))

    centers = [(10,10),
               (11,9),
               (12,8),
               (13,7),
               (9,11),
               (8,12),
               (7,13),
               (6,12),
               (5,11),
               (4,10),
               (3,9),
               (12,6),
               (11,5),
               (10,4),
               (9,3)]
    for c in centers:
        sq = autils.make_square((c[0]*M,c[1]*M),W,orient)
        walls += sq


a = pf.AStar()
a.init_grid(N,N, tuple(walls), start, end)

# add cost around blocks

for c in centers:
    sq = autils.make_square((c[0]*M,c[1]*M),W,orient)
    added= []
    for s in sq:
        cell = a.get_cell(*s)            
        for adj in a.get_surrounding_cells(cell):
            if not adj in added:
                added.append(adj)
                adj.c += .2 #2.0
                '''
    # Add second layer
    for s in sq:
        cell = a.get_cell(*s)
        for adj in a.get_surrounding_cells(cell):
            if adj.reachable:
                for aadj in a.get_surrounding_cells(adj):
                    if not aadj in added:
                        added.append(aadj)
                        aadj.c += 1.0

    # Add third layer
    for s in sq:
        cell = a.get_cell(*s)
        for adj in a.get_surrounding_cells(cell):
            if adj.reachable:
                for aadj in a.get_surrounding_cells(adj):
                    for aaadj in a.get_surrounding_cells(aadj):
                        if not aaadj in added:
                            added.append(aaadj)
                            aaadj.c += 0.5

    # Add fourth layer
    for s in sq:
        cell = a.get_cell(*s)
        for adj in a.get_surrounding_cells(cell):
            if adj.reachable:
                for aadj in a.get_surrounding_cells(adj):
                    for aaadj in a.get_surrounding_cells(aadj):
                        for aaaadj in a.get_surrounding_cells(aaadj):
                            if not aaaadj in added:
                                added.append(aaaadj)
                                aaaadj.c += 0.25
'''
if not movie:
    autils.plotAstar(a,None,anime=False,spline=False)
    show()

NN=20
path,cnt = a.solve(animate=movie)
fname = ("anime/test%04d.png"%cnt)
autils.plotAstar(a,path,anime=False,fname=fname,spline=False)
# make some copies of the last image for the movie
if movie:
    ofname = fname
    for ii in range(NN):
        cnt+=1
        fname = ("anime/test%04d.png"%cnt)
        print 'cp %s to %s'%(ofname,fname)
        call(['cp',ofname,fname])

# Now add the spline and copy
cnt+=1
fname = ("anime/test%04d.png"%cnt)
autils.plotAstar(a,path,anime=False,fname=fname,spline=True)
if movie:
    ofname = fname
    for ii in range(NN):
        cnt+=1
        fname = ("anime/test%04d.png"%cnt)
        print 'cp %s to %s'%(ofname,fname)
        call(['cp',ofname,fname])
else:
    show()
