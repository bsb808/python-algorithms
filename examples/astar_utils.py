from pylab import *
def plotAstar(astar,path):
    ax=subplot(111,aspect='equal')
    xmax=0.0
    ymax=0.0
    for c in astar.cells:
        bg="white"
        if not c.reachable:
            bg="black"
        elif c==astar.start:
            bg="green"
        elif c==astar.end:
            bg="red"
        ax.add_patch(Rectangle((c.x-0.5,c.y-0.5),1.0,1.0,edgecolor="black",facecolor=bg))
    xmax=max(xmax,c.x+0.5)
    ymax=max(ymax,c.y+0.5)
    ax.set_xlim(-0.5,xmax)
    ax.set_ylim(-0.5,ymax)

    xx = []
    yy = []
    if not (path is None):
        for p in path:
            xx.append(p[0])
            yy.append(p[1])
            plot(xx,yy,'g',linewidth=5)

# Webloes
# Jared Pechan 264-3217
