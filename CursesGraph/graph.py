import curses
from .point import Point

class PointGraph:
    def __init__(self, 
            wind : "Window to draw to", 
            points : "Points list (List of Point objects)" = []):
        self.wind = wind
        self.points = points
        self.wdim = (10, 10)

    def _getMax(self, 
            points : "Points List", 
            axis : "Axis to get, x or y" = "y"):
        curmax = 0

        for point in points:
            if point.y > curmax:
                curmax = getattr(point, axis)
            
        return curmax
    
    def _getMin(self, 
            points : "Points List", 
            axis : "Axis to get, x or y" = "y"):
        curmin = 0

        for point in points:
            if point.y < curmin:
                curmin = getattr(point, axis)
            
        return curmin

    def _rng(self, 
            points : "Points List", 
            axis : "Axis to get, x or y" = "y"):
        return abs(self._getMax(points, axis) - self._getMin(points, axis))

    def _fit(self, 
            num : "Number to fit", 
            wd : "Window dimension for axis", 
            mn : "Max of range", 
            mx : "Min of range"):

        # formula from https://stats.stackexchange.com/a/281164
        try:
            return round(((( num - mn ) / ( mx - mn ))) * wd)
        except ZeroDivisionError:
            return 0

    def drawPoint(self, 
            point : "Point", 
            points : "Points List", 
            wd : "Window Dimensions", 
            l : "Whether to draw under the line" = True):
        wx, wy = wd

        x = self._fit(point.x, wx, self._getMax(points, 'x'), self._getMin(points, 'x'))
        y = self._fit(point.y, wy, self._getMax(points, 'y'), self._getMin(points, 'y'))

        mx = self._getMax(points, 'x')
        x = x if mx > wx else point.x

        if x > wx:
            point.rem = True

        if l:
            for i in range(y + 1):
                try:
                    self.wind.addch(wy - i, wx - x, curses.ACS_BLOCK)
                except Exception:
                    pass
        else:
            try:
                self.wind.addch(wy - y, wx - x, curses.ACS_BLOCK)
            except Exception:
                pass

        return wy - y, wx - x

    def addPoint(self, x, y):
        self.points.append(Point(x, y))

    def increment(self, 
            amt : "Amount to increment by" = 1, 
            crop : "Whether to remove points that go off the screen's X axis" = True):

        for i, point in enumerate(self.points):

            point.x = point.x + amt

            if crop:

                if point.x > self.wdim[0]:

                    del self.points[i]

    def draw(self, 
            l : "Whether to fill in under points" = True):
        self.wind.erase()
        my, mx = self.wind.getmaxyx()
        self.wdim = (mx, my)

        for point in self.points:
            self.drawPoint(point, self.points, (mx, my), l)

        self.wind.refresh()