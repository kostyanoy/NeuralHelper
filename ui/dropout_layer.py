# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dropout_layer.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_DropoutLayer(object):
    def setupUi(self, DropoutLayer):
        if not DropoutLayer.objectName():
            DropoutLayer.setObjectName(u"DropoutLayer")
        DropoutLayer.resize(139, 86)
        self.gridLayout = QGridLayout(DropoutLayer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_dropout_rate = QLabel(DropoutLayer)
        self.lbl_dropout_rate.setObjectName(u"lbl_dropout_rate")

        self.gridLayout.addWidget(self.lbl_dropout_rate, 2, 0, 1, 1)

        self.lbl_name = QLabel(DropoutLayer)
        self.lbl_name.setObjectName(u"lbl_name")

        self.gridLayout.addWidget(self.lbl_name, 0, 0, 1, 2, Qt.AlignHCenter|Qt.AlignTop)

        self.btn_delete = QPushButton(DropoutLayer)
        self.btn_delete.setObjectName(u"btn_delete")

        self.gridLayout.addWidget(self.btn_delete, 1, 0, 1, 2)

        self.spin_dropout_rate = QDoubleSpinBox(DropoutLayer)
        self.spin_dropout_rate.setObjectName(u"spin_dropout_rate")
        self.spin_dropout_rate.setMaximum(1.000000000000000)
        self.spin_dropout_rate.setSingleStep(0.010000000000000)

        self.gridLayout.addWidget(self.spin_dropout_rate, 2, 1, 1, 1)


        self.retranslateUi(DropoutLayer)
        self.btn_delete.clicked.connect(DropoutLayer.delete_layer)

        QMetaObject.connectSlotsByName(DropoutLayer)
    # setupUi

    def retranslateUi(self, DropoutLayer):
        DropoutLayer.setWindowTitle(QCoreApplication.translate("DropoutLayer", u"Form", None))
        self.lbl_dropout_rate.setText(QCoreApplication.translate("DropoutLayer", u"Dropout rate", None))
        self.lbl_name.setText(QCoreApplication.translate("DropoutLayer", u"Dropout", None))
        self.btn_delete.setText(QCoreApplication.translate("DropoutLayer", u"Delete layer", None))
    # retranslateUi

