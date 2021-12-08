import CursesGraph
from curses import wrapper
import curses

def main(scr):
    curses.curs_set(0)

    y, x = scr.getmaxyx()

    w = scr.derwin(y, round(x/2)-1, 0, 0)

    w2 = scr.derwin(y, round(x/2)-2, 0, round(x/2))

    g = CursesGraph.PointGraph(w)
    g2 = CursesGraph.PointGraph(w2)


    for e in range(5):
        for i in range(1, 30):
            g.addPoint(1, (i/5)**2)
            #g.addPoint(1, -(i/5)**2)

            g.increment()
        
        for i in range(1, 30):
            g2.addPoint(1, (i/5)**2)
            #g2.addPoint(1, -(i/5)**2)

            g2.increment()

        g.draw(False)
        g2.draw(True)

    scr.getch()

wrapper(main)