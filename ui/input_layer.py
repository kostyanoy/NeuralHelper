# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'input_layer.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_InputLayer(object):
    def setupUi(self, InputLayer):
        if not InputLayer.objectName():
            InputLayer.setObjectName(u"InputLayer")
        InputLayer.resize(137, 202)
        self.gridLayout = QGridLayout(InputLayer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.layout_inputs = QFormLayout()
        self.layout_inputs.setObjectName(u"layout_inputs")
        self.lbl_first_dimention = QLabel(InputLayer)
        self.lbl_first_dimention.setObjectName(u"lbl_first_dimention")

        self.layout_inputs.setWidget(0, QFormLayout.LabelRole, self.lbl_first_dimention)

        self.spin_first_dimention = QSpinBox(InputLayer)
        self.spin_first_dimention.setObjectName(u"spin_first_dimention")
        self.spin_first_dimention.setMinimum(1)
        self.spin_first_dimention.setMaximum(1000)
        self.spin_first_dimention.setValue(10)

        self.layout_inputs.setWidget(0, QFormLayout.FieldRole, self.spin_first_dimention)

        self.btn_add_input = QPushButton(InputLayer)
        self.btn_add_input.setObjectName(u"btn_add_input")

        self.layout_inputs.setWidget(1, QFormLayout.LabelRole, self.btn_add_input)

        self.btn_delete_input = QPushButton(InputLayer)
        self.btn_delete_input.setObjectName(u"btn_delete_input")

        self.layout_inputs.setWidget(1, QFormLayout.FieldRole, self.btn_delete_input)


        self.gridLayout.addLayout(self.layout_inputs, 1, 0, 1, 1)

        self.lbl_name = QLabel(InputLayer)
        self.lbl_name.setObjectName(u"lbl_name")

        self.gridLayout.addWidget(self.lbl_name, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)


        self.retranslateUi(InputLayer)
        self.btn_add_input.clicked.connect(InputLayer.add_input)
        self.btn_delete_input.clicked.connect(InputLayer.delete_input)

        QMetaObject.connectSlotsByName(InputLayer)
    # setupUi

    def retranslateUi(self, InputLayer):
        InputLayer.setWindowTitle(QCoreApplication.translate("InputLayer", u"Form", None))
        self.lbl_first_dimention.setText(QCoreApplication.translate("InputLayer", u"1 dimention", None))
        self.btn_add_input.setText(QCoreApplication.translate("InputLayer", u"Add", None))
        self.btn_delete_input.setText(QCoreApplication.translate("InputLayer", u"Delete", None))
        self.lbl_name.setText(QCoreApplication.translate("InputLayer", u"Input", None))
    # retranslateUi

