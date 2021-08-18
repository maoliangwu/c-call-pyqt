MainModule = "__init__"

import sys
import imp
import os

from PyQt5 import QtCore, QtGui, QtWidgets

class DialogoImprimir(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)        
        self.GeneraUI()     

    def GeneraUI(self):
        self.setObjectName("Dialog")
        self.resize(200, 293)       
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")       
        self.retranslateUi()
        #acciones       
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate