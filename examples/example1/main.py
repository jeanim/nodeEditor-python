import sys
from PySide import QtGui
import src.FlowScene
reload(src.FlowScene)
import src.FlowGraphicsView
reload(src.FlowGraphicsView)
from src.FlowScene import FlowScene
from src.FlowGraphicsView import FlowGraphicsView

def main():
    global app
    global win
    try:
        win.close()
        win.deleteLater()
    except:pass

    import qdarkstyle
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    view = FlowGraphicsView(FlowScene.instance())
    view.setWindowTitle('Node-based flow editor')
    view.resize(800,600)
    view.show()

    try:
        view.raise_()
        app.exec_()
    except:pass

if __name__=='__main__':
    main()