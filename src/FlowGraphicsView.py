from PySide import QtGui,QtCore
import math

class FlowGraphicsView(QtGui.QGraphicsView):
    def __init__(self,scene):
        QtGui.QGraphicsView.__init__(self)
        self.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setBackgroundBrush(QtGui.QColor(QtCore.Qt.gray).darker(300))
        self.setTransformationAnchor(QtGui.QGraphicsView.AnchorUnderMouse)
        self.setCacheMode(QtGui.QGraphicsView.CacheBackground)
        self.setScene(scene)

    def contextMenuEvent(self,event):
        modelMenu = QtGui.QMenu()
        modelName = 'test'
        modelMenu.addAction(modelName)

        action = modelMenu.exec_(event.globalPos())
        if action:
            QtCore.qDebug(action.text())

        # modelName = action.text()

    def wheelEvent(self, event, *args, **kwargs):
        operator,factor = event.delta(),1.2
        scaleFactor = self.transform().m11()
        if operator > 0 and scaleFactor < 3:
            self.scale(factor, factor)
        if operator < 0 and scaleFactor > 0.2:
            self.scale(1.0/factor, 1.0/factor)
        self.update()

    def drawBackground(self, painter, rect, *args, **kwargs):
        QtGui.QGraphicsView.drawBackground(self,painter,rect)
        def drawGrid(gridStep):
            windowRect = self.rect()
            tl = self.mapToScene(windowRect.topLeft())
            br = self.mapToScene(windowRect.bottomRight())

            left = int(math.floor(tl.x()/gridStep-0.5))
            right = int(math.floor(br.x()/gridStep+1.0))
            bottom = int(math.floor(tl.y()/gridStep-0.5))
            top = int(math.floor(br.y()/gridStep+1.0))

            for xi in range(left,right):
                line = QtCore.QLineF(xi*gridStep,bottom*gridStep,xi*gridStep,top*gridStep)
                painter.drawLine(line)

            for yi in range(bottom,top):
                line = QtCore.QLineF(left*gridStep,yi*gridStep,right*gridStep,yi*gridStep)
                painter.drawLine(line)

        bBrush = self.backgroundBrush()
        gridColor = bBrush.color().lighter(120)
        pfine = QtGui.QPen(gridColor,1.0)
        painter.setPen(pfine)
        drawGrid(15)

        gridColor = bBrush.color().darker(200)
        p = QtGui.QPen(gridColor,1.0)
        painter.setPen(p)
        drawGrid(150)