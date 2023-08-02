# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'conv2d_layer.ui'
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

class Ui_Conv2DLayer(object):
    def setupUi(self, Conv2DLayer):
        if not Conv2DLayer.objectName():
            Conv2DLayer.setObjectName(u"Conv2DLayer")
        Conv2DLayer.resize(193, 213)
        self.gridLayout = QGridLayout(Conv2DLayer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_strides = QLabel(Conv2DLayer)
        self.lbl_strides.setObjectName(u"lbl_strides")

        self.gridLayout.addWidget(self.lbl_strides, 4, 0, 1, 1)

        self.lbl_kernel = QLabel(Conv2DLayer)
        self.lbl_kernel.setObjectName(u"lbl_kernel")

        self.gridLayout.addWidget(self.lbl_kernel, 3, 0, 1, 1)

        self.spin_kernel = QSpinBox(Conv2DLayer)
        self.spin_kernel.setObjectName(u"spin_kernel")
        self.spin_kernel.setMinimum(1)
        self.spin_kernel.setMaximum(100)

        self.gridLayout.addWidget(self.spin_kernel, 3, 1, 1, 1)

        self.lbl_filters = QLabel(Conv2DLayer)
        self.lbl_filters.setObjectName(u"lbl_filters")

        self.gridLayout.addWidget(self.lbl_filters, 2, 0, 1, 1)

        self.spin_filters = QSpinBox(Conv2DLayer)
        self.spin_filters.setObjectName(u"spin_filters")
        self.spin_filters.setMinimum(1)
        self.spin_filters.setMaximum(10000)

        self.gridLayout.addWidget(self.spin_filters, 2, 1, 1, 1)

        self.spin_strides = QSpinBox(Conv2DLayer)
        self.spin_strides.setObjectName(u"spin_strides")
        self.spin_strides.setMinimum(1)
        self.spin_strides.setMaximum(100)

        self.gridLayout.addWidget(self.spin_strides, 4, 1, 1, 1)

        self.combo_activation = QComboBox(Conv2DLayer)
        self.combo_activation.addItem("")
        self.combo_activation.addItem("")
        self.combo_activation.addItem("")
        self.combo_activation.setObjectName(u"combo_activation")

        self.gridLayout.addWidget(self.combo_activation, 5, 1, 1, 1)

        self.lbl_activation = QLabel(Conv2DLayer)
        self.lbl_activation.setObjectName(u"lbl_activation")

        self.gridLayout.addWidget(self.lbl_activation, 5, 0, 1, 1)

        self.lbl_regularizer = QLabel(Conv2DLayer)
        self.lbl_regularizer.setObjectName(u"lbl_regularizer")
        self.lbl_regularizer.setEnabled(True)

        self.gridLayout.addWidget(self.lbl_regularizer, 6, 0, 1, 1)

        self.combo_regularizer = QComboBox(Conv2DLayer)
        self.combo_regularizer.addItem("")
        self.combo_regularizer.addItem("")
        self.combo_regularizer.addItem("")
        self.combo_regularizer.setObjectName(u"combo_regularizer")
        self.combo_regularizer.setEnabled(True)

        self.gridLayout.addWidget(self.combo_regularizer, 6, 1, 1, 1)

        self.lbl_name = QLabel(Conv2DLayer)
        self.lbl_name.setObjectName(u"lbl_name")

        self.gridLayout.addWidget(self.lbl_name, 0, 0, 1, 2, Qt.AlignHCenter|Qt.AlignTop)

        self.btn_delete = QPushButton(Conv2DLayer)
        self.btn_delete.setObjectName(u"btn_delete")

        self.gridLayout.addWidget(self.btn_delete, 1, 0, 1, 2)

        self.cbx_same_padding = QCheckBox(Conv2DLayer)
        self.cbx_same_padding.setObjectName(u"cbx_same_padding")

        self.gridLayout.addWidget(self.cbx_same_padding, 7, 0, 1, 2)


        self.retranslateUi(Conv2DLayer)
        self.btn_delete.clicked.connect(Conv2DLayer.delete_layer)

        QMetaObject.connectSlotsByName(Conv2DLayer)
    # setupUi

    def retranslateUi(self, Conv2DLayer):
        Conv2DLayer.setWindowTitle(QCoreApplication.translate("Conv2DLayer", u"Form", None))
        self.lbl_strides.setText(QCoreApplication.translate("Conv2DLayer", u"Strides", None))
        self.lbl_kernel.setText(QCoreApplication.translate("Conv2DLayer", u"Kernel", None))
        self.lbl_filters.setText(QCoreApplication.translate("Conv2DLayer", u"Filters", None))
        self.combo_activation.setItemText(0, QCoreApplication.translate("Conv2DLayer", u"Sigmoid", None))
        self.combo_activation.setItemText(1, QCoreApplication.translate("Conv2DLayer", u"Tanh", None))
        self.combo_activation.setItemText(2, QCoreApplication.translate("Conv2DLayer", u"Relu", None))

        self.lbl_activation.setText(QCoreApplication.translate("Conv2DLayer", u"Activation", None))
        self.lbl_regularizer.setText(QCoreApplication.translate("Conv2DLayer", u"Regularizer ", None))
        self.combo_regularizer.setItemText(0, QCoreApplication.translate("Conv2DLayer", u"L1", None))
        self.combo_regularizer.setItemText(1, QCoreApplication.translate("Conv2DLayer", u"L2", None))
        self.combo_regularizer.setItemText(2, QCoreApplication.translate("Conv2DLayer", u"None", None))

        self.lbl_name.setText(QCoreApplication.translate("Conv2DLayer", u"Conv2D", None))
        self.btn_delete.setText(QCoreApplication.translate("Conv2DLayer", u"Delete layer", None))
        self.cbx_same_padding.setText(QCoreApplication.translate("Conv2DLayer", u"Same padding", None))
    # retranslateUi

