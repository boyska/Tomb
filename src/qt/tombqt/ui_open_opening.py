# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tombqt/open_opening.ui'
#
# Created: Thu Feb  2 17:06:53 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_opening(object):
    def setupUi(self, opening):
        opening.setObjectName(_fromUtf8("opening"))
        opening.resize(480, 640)
        self.verticalLayout = QtGui.QVBoxLayout(opening)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(opening)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(opening)
        QtCore.QMetaObject.connectSlotsByName(opening)

    def retranslateUi(self, opening):
        opening.setWindowTitle(QtGui.QApplication.translate("opening", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        opening.setTitle(QtGui.QApplication.translate("opening", "Opening", None, QtGui.QApplication.UnicodeUTF8))
        opening.setSubTitle(QtGui.QApplication.translate("opening", "We\'re almost there...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("opening", "Going to open the tomb", None, QtGui.QApplication.UnicodeUTF8))

