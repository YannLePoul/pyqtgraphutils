from PyQt5 import QtGui
from PyQt5 import QtCore
import pyqtgraph as pg
from pyqtgraph.Point import Point


class LineSegmentItem(pg.GraphicsObject):
    def __init__(self, p1, p2):
        pg.GraphicsObject.__init__(self)
        self.p1 = p1
        self.p2 = p2
        self.generatePicture()

    def generatePicture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        p.drawLine(QtCore.QPoint(self.p1[0], self.p1[1]), QtCore.QPoint(self.p2[0], self.p2[1]))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())


class CircleItem(pg.GraphicsObject):

    sigDragged = QtCore.Signal(object)
    sigPositionChangeFinished = QtCore.Signal(object)
    sigPositionChanged = QtCore.Signal(object)

    def __init__(self, center, radius):
        pg.GraphicsObject.__init__(self)
        self.center = center
        self.radius = radius
        self.setCenter(center)
        self.setRadius(radius)
        self.generatePicture()

    def generatePicture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        p.drawEllipse(QtCore.QRectF(0, 0, self.radius * 2, self.radius * 2))

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def setRadius(self, radius):
        self.radius = radius
        self.setCenter(self.center)
        self.generatePicture()

    def setCenter(self, center):
        self.center = center
        pg.GraphicsObject.setPos(self, Point(center.x()-self.radius, center.y()-self.radius))
        self.update()

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())


class RectangleItem(pg.GraphicsObject):
    def __init__(self, topLeft, size):
        pg.GraphicsObject.__init__(self)
        self.topLeft = topLeft
        self.size = size
        self.generatePicture()

    def generatePicture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        tl = QtCore.QPointF(self.topLeft[0], self.topLeft[1])
        size = QtCore.QSizeF(self.size[0], self.size[1])
        p.drawRect(QtCore.QRectF(tl, size))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())
