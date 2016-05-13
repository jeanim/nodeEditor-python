from PySide import QtGui

class FlowScene(QtGui.QGraphicsScene):
    def __init__(self):
        QtGui.QGraphicsScene.__init__(self)
        self.setItemIndexMethod(QtGui.QGraphicsScene.NoIndex)
        self._connections = []
        self._nodes = []

    def __del__(self):
        pass

    @classmethod
    def instance(cls):
        return FlowScene()

    def createConnection(self):
        pass

    def deleteConnection(self,id):
        pass

    def createNodes(self):
        pass

    def getConnection(self,id):
        pass

    def getNode(self,id):
        pass

    def locateNodeAt(self,event):
        pass