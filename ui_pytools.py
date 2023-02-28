# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pytools.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QToolButton,
    QWidget)

from widgets import (ConvertToolGroupBox, DeleteToolGroupBox)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(736, 309)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.DeleteToolGroupBox = DeleteToolGroupBox(self.centralwidget)
        self.DeleteToolGroupBox.setObjectName(u"DeleteToolGroupBox")
        self.DeleteToolGroupBox.setGeometry(QRect(10, 20, 331, 211))
        self.DeleteToolGroupBox.setAcceptDrops(True)
        self.DeleteToolGroupBox.setFlat(False)
        self.DeleteToolGroupBox.setCheckable(False)
        self.pathEdit = QLineEdit(self.DeleteToolGroupBox)
        self.pathEdit.setObjectName(u"pathEdit")
        self.pathEdit.setEnabled(True)
        self.pathEdit.setGeometry(QRect(20, 30, 231, 20))
        self.pathEdit.setFrame(False)
        self.pathEdit.setDragEnabled(False)
        self.pathEdit.setReadOnly(True)
        self.toolButton = QToolButton(self.DeleteToolGroupBox)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(260, 30, 61, 22))
        self.pushButton = QPushButton(self.DeleteToolGroupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 70, 75, 24))
        self.status_label_2 = QLabel(self.DeleteToolGroupBox)
        self.status_label_2.setObjectName(u"status_label_2")
        self.status_label_2.setGeometry(QRect(60, 80, 54, 16))
        self.status_label = QLabel(self.DeleteToolGroupBox)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(120, 80, 54, 16))
        self.ConvertToolGroupBox = ConvertToolGroupBox(self.centralwidget)
        self.ConvertToolGroupBox.setObjectName(u"ConvertToolGroupBox")
        self.ConvertToolGroupBox.setGeometry(QRect(380, 30, 331, 201))
        self.pushButton_2 = QPushButton(self.ConvertToolGroupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(170, 100, 75, 24))
        self.pathEdit_2 = QLineEdit(self.ConvertToolGroupBox)
        self.pathEdit_2.setObjectName(u"pathEdit_2")
        self.pathEdit_2.setEnabled(True)
        self.pathEdit_2.setGeometry(QRect(20, 30, 231, 20))
        self.pathEdit_2.setFrame(False)
        self.pathEdit_2.setDragEnabled(False)
        self.pathEdit_2.setReadOnly(True)
        self.toolButton_2 = QToolButton(self.ConvertToolGroupBox)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(260, 30, 61, 22))
        self.label = QLabel(self.ConvertToolGroupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 100, 54, 16))
        self.lineEdit = QLineEdit(self.ConvertToolGroupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 100, 71, 20))
        self.lineEdit.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(True)
        self.progressBar = QProgressBar(self.ConvertToolGroupBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QRect(17, 160, 311, 23))
        self.progressBar.setMouseTracking(False)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.pushButton, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.pathEdit_2)
        QWidget.setTabOrder(self.pathEdit_2, self.toolButton)
        QWidget.setTabOrder(self.toolButton, self.toolButton_2)
        QWidget.setTabOrder(self.toolButton_2, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pathEdit)

        self.retranslateUi(MainWindow)
        self.toolButton.clicked.connect(self.DeleteToolGroupBox.clickToolButton)
        self.pushButton.clicked.connect(self.DeleteToolGroupBox.clickPushButton)
        self.ConvertToolGroupBox.setMax.connect(self.progressBar.setMaximum)
        self.ConvertToolGroupBox.setNow.connect(self.progressBar.setValue)
        self.DeleteToolGroupBox.setPath.connect(self.pathEdit.setText)
        self.toolButton_2.clicked.connect(self.ConvertToolGroupBox.clickToolButton)
        self.pushButton_2.clicked.connect(self.ConvertToolGroupBox.clickPushButton)
        self.ConvertToolGroupBox.setPath.connect(self.pathEdit_2.setText)
        self.lineEdit.textEdited.connect(self.ConvertToolGroupBox.setSize)
        self.DeleteToolGroupBox.setStatus.connect(self.status_label.setText)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyTools", None))
        self.DeleteToolGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Delete Tool", None))
        self.pathEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6307\u5b9a\u6587\u4ef6\u5939\u8def\u5f84", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"SELECT", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.status_label_2.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001\uff1a", None))
        self.status_label.setText("")
        self.ConvertToolGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Photo Size", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.pathEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6307\u5b9a\u6587\u4ef6\u5939\u8def\u5f84", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"SELECT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"128", None))
    # retranslateUi

