import CursesGraph
from curses import wrapper
import curses
import random
import time

def main(scr):
    curses.curs_set(0)

    g = CursesGraph.PointGraph(scr)


    for e in range(5):
        for i in range(30, 1, -1):
            g.addPoint(1, (i/5)**2)

            g.draw()
            g.increment()
        
        for i in range(1, 30):
            g.addPoint(1, (i/5)**2)

            g.draw()
            g.increment()

    scr.getch()

wrapper(main)