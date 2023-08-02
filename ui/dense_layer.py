# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dense_layer.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_DenseLayer(object):
    def setupUi(self, DenseLayer):
        if not DenseLayer.objectName():
            DenseLayer.setObjectName(u"DenseLayer")
        DenseLayer.resize(143, 143)
        self.gridLayout = QGridLayout(DenseLayer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.combo_regularizer = QComboBox(DenseLayer)
        self.combo_regularizer.addItem("")
        self.combo_regularizer.addItem("")
        self.combo_regularizer.addItem("")
        self.combo_regularizer.setObjectName(u"combo_regularizer")
        self.combo_regularizer.setEnabled(True)

        self.gridLayout.addWidget(self.combo_regularizer, 5, 1, 1, 1)

        self.lbl_regularizer = QLabel(DenseLayer)
        self.lbl_regularizer.setObjectName(u"lbl_regularizer")
        self.lbl_regularizer.setEnabled(True)

        self.gridLayout.addWidget(self.lbl_regularizer, 5, 0, 1, 1)

        self.lbl_name = QLabel(DenseLayer)
        self.lbl_name.setObjectName(u"lbl_name")

        self.gridLayout.addWidget(self.lbl_name, 0, 0, 1, 2, Qt.AlignHCenter|Qt.AlignTop)

        self.btn_delete = QPushButton(DenseLayer)
        self.btn_delete.setObjectName(u"btn_delete")

        self.gridLayout.addWidget(self.btn_delete, 1, 0, 1, 2)

        self.combo_activation = QComboBox(DenseLayer)
        self.combo_activation.addItem("")
        self.combo_activation.addItem("")
        self.combo_activation.addItem("")
        self.combo_activation.setObjectName(u"combo_activation")

        self.gridLayout.addWidget(self.combo_activation, 4, 1, 1, 1)

        self.spin_neurons = QSpinBox(DenseLayer)
        self.spin_neurons.setObjectName(u"spin_neurons")
        self.spin_neurons.setMinimum(1)
        self.spin_neurons.setMaximum(10000)

        self.gridLayout.addWidget(self.spin_neurons, 3, 1, 1, 1)

        self.lbl_activation = QLabel(DenseLayer)
        self.lbl_activation.setObjectName(u"lbl_activation")

        self.gridLayout.addWidget(self.lbl_activation, 4, 0, 1, 1)

        self.lbl_neurons = QLabel(DenseLayer)
        self.lbl_neurons.setObjectName(u"lbl_neurons")

        self.gridLayout.addWidget(self.lbl_neurons, 3, 0, 1, 1)

        self.cbx_flatten = QCheckBox(DenseLayer)
        self.cbx_flatten.setObjectName(u"cbx_flatten")

        self.gridLayout.addWidget(self.cbx_flatten, 2, 0, 1, 1)


        self.retranslateUi(DenseLayer)
        self.btn_delete.clicked.connect(DenseLayer.delete_layer)

        QMetaObject.connectSlotsByName(DenseLayer)
    # setupUi

    def retranslateUi(self, DenseLayer):
        DenseLayer.setWindowTitle(QCoreApplication.translate("DenseLayer", u"Form", None))
        self.combo_regularizer.setItemText(0, QCoreApplication.translate("DenseLayer", u"L1", None))
        self.combo_regularizer.setItemText(1, QCoreApplication.translate("DenseLayer", u"L2", None))
        self.combo_regularizer.setItemText(2, QCoreApplication.translate("DenseLayer", u"None", None))

        self.lbl_regularizer.setText(QCoreApplication.translate("DenseLayer", u"Regularizer ", None))
        self.lbl_name.setText(QCoreApplication.translate("DenseLayer", u"Dense", None))
        self.btn_delete.setText(QCoreApplication.translate("DenseLayer", u"Delete layer", None))
        self.combo_activation.setItemText(0, QCoreApplication.translate("DenseLayer", u"Sigmoid", None))
        self.combo_activation.setItemText(1, QCoreApplication.translate("DenseLayer", u"Tanh", None))
        self.combo_activation.setItemText(2, QCoreApplication.translate("DenseLayer", u"Relu", None))

        self.lbl_activation.setText(QCoreApplication.translate("DenseLayer", u"Activation", None))
        self.lbl_neurons.setText(QCoreApplication.translate("DenseLayer", u"Neurons", None))
        self.cbx_flatten.setText(QCoreApplication.translate("DenseLayer", u"Flatten", None))
    # retranslateUi

