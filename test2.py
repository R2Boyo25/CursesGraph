import CursesGraph
from curses import wrapper
import curses
import random

def main(scr):
    curses.curs_set(0)

    #y, x = scr.getmaxyx()

    #w = scr.derwin(y, round(x/2)-1, 0, 0)

    #w2 = scr.derwin(y, round(x/2)-2, 0, round(x/2))

    
    #g = CursesGraph.PercentGraph(scr)
    g = CursesGraph.NumberGraph(scr)

    for i in range(1, 201):
        g.add(i, color = 3)
        g.add(i/2, color = 1)

        g.increment()
        g.draw()


    #g.add(2, color = 5)
    #g.add(8, color = 2)

    #g.increment()

    '''
    for i in range(15):
        for e in range(11):
            g.add([10 - e], 10, color = 2)

            g.increment()

            g.draw(True)
        
        for e in range(10, 0, -1):
            g.add([10 - e], 10, color = 3)

            g.increment()

            g.draw(True)
    '''

    scr.getch()

wrapper(main)
