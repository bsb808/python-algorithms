from pylab import *

def plotAstar(astar,path,ax=None,anime=False,fname=None):
    if ax is None:
        figure(1)
        clf()
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
        elif c.c > 1.0:
            bg="%f"%(1-(min((c.c-1)/5.0,1)))
            #print bg

        if not bg=='white':
            ax.add_patch(Rectangle((c.x-0.5,c.y-0.5),1.0,1.0,edgecolor="black",facecolor=bg))
        xmax=max(xmax,c.x+0.5)
        ymax=max(ymax,c.y+0.5)

    if anime:
        for f,c in astar.opened:
            bg='yellow'
            ax.add_patch(Rectangle((c.x-0.5,c.y-0.5),1.0,1.0,edgecolor="black",facecolor=bg))
        for c in astar.closed:
            bg='orange'  
            ax.add_patch(Rectangle((c.x-0.5,c.y-0.5),1.0,1.0,edgecolor="black",facecolor=bg))

        
    ax.set_xlim(-0.5,xmax)
    ax.set_ylim(-0.5,ymax)
    ax.set_xticks(arange(-0.5,xmax,1.0),minor=True)
    ax.set_yticks(arange(-0.5,ymax,1.0),minor=True)
    ax.grid(True,which='minor',linestyle='-',xdata=range(50))
    draw()
    # Normalize to axes to value
    for tl,setf in zip([ax.get_xticklabels(), ax.get_yticklabels()],
                       [ax.set_xticklabels,ax.set_yticklabels]):
        axt = tl
        newl = []
        for a in axt:
            try:
                n=int(a.get_text())
                newl.append("%d"%(n/float(xmax-.5)*200))
            except ValueError:
                newl.append(a.get_text())
        setf(newl)
                      

    xx = []
    yy = []
    if not (path is None):
        for p in path:
            xx.append(p[0])
            yy.append(p[1])
            plot(xx,yy,'g',linewidth=5)
    if fname is None:
        draw()
    else:
        print fname
        title(fname)
        savefig(fname)
def make_square(center,width,orient):
    walls = []
    for x in arange(width):
        for y in arange(width):
            xx = x*cos(orient) - y*sin(orient)
            yy = x*sin(orient) + y*cos(orient)
            xxx = center[0]-width/2+xx
            yyy = center[1]-width/2+yy
            #print (xxx,yyy)
            #print (round(xxx),round(yyy))
            wall = (int(round(xxx)),int(round(yyy)))
            if wall in walls:
                print (xxx,yyy)
                print str(wall)
            else:
                walls.append(wall)
            #walls.append((x,y))

    return walls
# Webloes
# Jared Pechan 264-3217
