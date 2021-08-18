import imp
import os
import sys
import operator
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from DialogoImprimir import DialogoImprimir

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = DialogoImprimir()
    myapp.show()
    sys.exit(app.exec_())


def iniciar(*datos):
    app = QtWidgets.QApplication.instance()
    print (app)
    if app is None:
        app = QtWidgets.QApplication([])
    myapp = DialogoImprimir()
    myapp.show()
    return myapp.exec_()