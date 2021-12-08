import CursesGraph
from curses import wrapper
import curses

def main(scr):
    curses.curs_set(0)

    #y, x = scr.getmaxyx()

    #w = scr.derwin(y, round(x/2)-1, 0, 0)

    #w2 = scr.derwin(y, round(x/2)-2, 0, round(x/2))

    g = CursesGraph.PercentGraph(scr)
    #g2 = CursesGraph.PointGraph(w2)


    for e in range(11):
        g.add([10 - e], 10, color = 2)

        g.increment()

        g.draw(True)
    
    for e in range(10, 0, -1):
        g.add([10 - e], 10, color = 3)

        g.increment()

        g.draw(True)

    scr.getch()

wrapper(main)