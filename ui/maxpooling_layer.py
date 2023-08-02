# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maxpooling_layer.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_MaxpoolingLayer(object):
    def setupUi(self, MaxpoolingLayer):
        if not MaxpoolingLayer.objectName():
            MaxpoolingLayer.setObjectName(u"MaxpoolingLayer")
        MaxpoolingLayer.resize(124, 135)
        self.gridLayout = QGridLayout(MaxpoolingLayer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cbx_same_padding = QCheckBox(MaxpoolingLayer)
        self.cbx_same_padding.setObjectName(u"cbx_same_padding")

        self.gridLayout.addWidget(self.cbx_same_padding, 4, 0, 1, 2)

        self.lbl_pool_size = QLabel(MaxpoolingLayer)
        self.lbl_pool_size.setObjectName(u"lbl_pool_size")

        self.gridLayout.addWidget(self.lbl_pool_size, 2, 0, 1, 1)

        self.btn_delete = QPushButton(MaxpoolingLayer)
        self.btn_delete.setObjectName(u"btn_delete")

        self.gridLayout.addWidget(self.btn_delete, 1, 0, 1, 2)

        self.lbl_name = QLabel(MaxpoolingLayer)
        self.lbl_name.setObjectName(u"lbl_name")

        self.gridLayout.addWidget(self.lbl_name, 0, 0, 1, 2, Qt.AlignHCenter|Qt.AlignTop)

        self.spin_strides = QSpinBox(MaxpoolingLayer)
        self.spin_strides.setObjectName(u"spin_strides")
        self.spin_strides.setMinimum(1)
        self.spin_strides.setMaximum(100)

        self.gridLayout.addWidget(self.spin_strides, 3, 1, 1, 1)

        self.lbl_strides = QLabel(MaxpoolingLayer)
        self.lbl_strides.setObjectName(u"lbl_strides")

        self.gridLayout.addWidget(self.lbl_strides, 3, 0, 1, 1)

        self.spin_pool = QSpinBox(MaxpoolingLayer)
        self.spin_pool.setObjectName(u"spin_pool")
        self.spin_pool.setMinimum(1)
        self.spin_pool.setMaximum(10000)

        self.gridLayout.addWidget(self.spin_pool, 2, 1, 1, 1)


        self.retranslateUi(MaxpoolingLayer)
        self.btn_delete.clicked.connect(MaxpoolingLayer.delete_layer)

        QMetaObject.connectSlotsByName(MaxpoolingLayer)
    # setupUi

    def retranslateUi(self, MaxpoolingLayer):
        MaxpoolingLayer.setWindowTitle(QCoreApplication.translate("MaxpoolingLayer", u"Form", None))
        self.cbx_same_padding.setText(QCoreApplication.translate("MaxpoolingLayer", u"Same padding", None))
        self.lbl_pool_size.setText(QCoreApplication.translate("MaxpoolingLayer", u"Pool size", None))
        self.btn_delete.setText(QCoreApplication.translate("MaxpoolingLayer", u"Delete layer", None))
        self.lbl_name.setText(QCoreApplication.translate("MaxpoolingLayer", u"Maxpooling", None))
        self.lbl_strides.setText(QCoreApplication.translate("MaxpoolingLayer", u"Strides", None))
    # retranslateUi

