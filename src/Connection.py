from PySide import QtCore,QtGui
# import Node
# import ConnectionGraphicsObject
# import ConnectionState
# import ConnectionGeometry

class Connection():
    def __init__(self):
        self._impl = 0

    def __del__(self):
        pass

    def id(self):
        pass

    def setRequiredPort(self,portType):
        pass

    def requiredPort(self):
        pass

    def getAddress(self):
        pass

    def setAddress(self):
        pass

    def tryConnectToNode(self,node,scenePoint):
        pass

    def connectToNode(self,address):
        pass

    def getConnectionGraphicsObject(self):
        pass

    def connectionState(self):
        pass

    def connectionGeometry(self):
        pass