# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main-window-gui.ui'
#
# Created: Sat May 21 17:27:30 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Bhavcopy(object):
    def setupUi(self, Bhavcopy):
        Bhavcopy.setObjectName(_fromUtf8("Bhavcopy"))
        Bhavcopy.resize(550, 350)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Bhavcopy.sizePolicy().hasHeightForWidth())
        Bhavcopy.setSizePolicy(sizePolicy)
        Bhavcopy.setMaximumSize(QtCore.QSize(550, 1000))
        Bhavcopy.setAutoFillBackground(True)
        Bhavcopy.setAnimated(True)
        self.centralwidget = QtGui.QWidget(Bhavcopy)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(17, 13, 526, 51))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.startDateLabel = QtGui.QLabel(self.widget)
        self.startDateLabel.setObjectName(_fromUtf8("startDateLabel"))
        self.horizontalLayout.addWidget(self.startDateLabel)
        self.startDate = QtGui.QDateTimeEdit(self.widget)
        self.startDate.setCalendarPopup(True)
        self.startDate.setObjectName(_fromUtf8("startDate"))
        self.horizontalLayout.addWidget(self.startDate)
        self.endDateLabel = QtGui.QLabel(self.widget)
        self.endDateLabel.setObjectName(_fromUtf8("endDateLabel"))
        self.horizontalLayout.addWidget(self.endDateLabel)
        self.endDate = QtGui.QDateTimeEdit(self.widget)
        self.endDate.setAccelerated(False)
        self.endDate.setCalendarPopup(True)
        self.endDate.setObjectName(_fromUtf8("endDate"))
        self.horizontalLayout.addWidget(self.endDate)
        self.downloadButton = QtGui.QPushButton(self.widget)
        self.downloadButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadButton.sizePolicy().hasHeightForWidth())
        self.downloadButton.setSizePolicy(sizePolicy)
        self.downloadButton.setAutoDefault(True)
        self.downloadButton.setDefault(True)
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.horizontalLayout.addWidget(self.downloadButton)
        self.cancelButton = QtGui.QPushButton(self.widget)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.progressUpdate = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressUpdate.sizePolicy().hasHeightForWidth())
        self.progressUpdate.setSizePolicy(sizePolicy)
        self.progressUpdate.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 255);"))
        self.progressUpdate.setObjectName(_fromUtf8("progressUpdate"))
        self.verticalLayout.addWidget(self.progressUpdate)
        Bhavcopy.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Bhavcopy)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Bhavcopy.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(Bhavcopy)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        Bhavcopy.setMenuBar(self.menubar)
        self.actionExit = QtGui.QAction(Bhavcopy)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(Bhavcopy)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout_2 = QtGui.QAction(Bhavcopy)
        self.actionAbout_2.setObjectName(_fromUtf8("actionAbout_2"))
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Bhavcopy)
        QtCore.QMetaObject.connectSlotsByName(Bhavcopy)

    def retranslateUi(self, Bhavcopy):
        Bhavcopy.setWindowTitle(QtGui.QApplication.translate("Bhavcopy", "NSE Data Downloader", None, QtGui.QApplication.UnicodeUTF8))
        self.startDateLabel.setText(QtGui.QApplication.translate("Bhavcopy", "  Start Date:", None, QtGui.QApplication.UnicodeUTF8))
        self.startDate.setDisplayFormat(QtGui.QApplication.translate("Bhavcopy", "dd/MM/yy", None, QtGui.QApplication.UnicodeUTF8))
        self.endDateLabel.setText(QtGui.QApplication.translate("Bhavcopy", "    End Date:", None, QtGui.QApplication.UnicodeUTF8))
        self.endDate.setDisplayFormat(QtGui.QApplication.translate("Bhavcopy", "dd/MM/yy", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadButton.setText(QtGui.QApplication.translate("Bhavcopy", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("Bhavcopy", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.progressUpdate.setText(QtGui.QApplication.translate("Bhavcopy", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("Bhavcopy", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("Bhavcopy", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("Bhavcopy", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("Bhavcopy", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_2.setText(QtGui.QApplication.translate("Bhavcopy", "About", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Bhavcopy = QtGui.QMainWindow()
    ui = Ui_Bhavcopy()
    ui.setupUi(Bhavcopy)
    Bhavcopy.show()
    sys.exit(app.exec_())

