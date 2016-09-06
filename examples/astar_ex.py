import algorithms.a_star_path_finding as pf
import astar_utils as autils
reload(autils)

a = pf.AStar()
walls = ((0, 5), (1, 0), (1, 1), (1, 5), (2, 3),
         (3, 1), (3, 2), (3, 5), (4, 1), (4, 4), (5, 1))
start = (0,0)
end= (5,5)
a.init_grid(6, 6, walls, start, end)
path = a.solve()

fig=figure(1)
clf()
autils.plotAstar(a,path)
show()
