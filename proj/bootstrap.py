
import sys
from PySide2 import QtCore as qtc, QtWidgets as qtw, QtQml as qtqml
from main import Main



if __name__ == "__main__":

    #   Set attributes
    qtw.QApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling)
    qtc.QCoreApplication.setAttribute(qtc.Qt.AA_UseHighDpiPixmaps)


    #   Define application
    app = qtw.QApplication(sys.argv)
    app.setOrganizationName("Yeahlowflicker Production")


    #   Define engine
    from os.path import dirname, abspath
    engine = qtqml.QQmlApplicationEngine()
    engine.load("/mnt/YFP/Projects/PRJ001-Productivity-Clock/proj/main.qml")


    #   Define Main
    manager = Main(engine)


    #   Exit handler
    sys.exit(app.exec_())
