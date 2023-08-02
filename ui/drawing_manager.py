# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drawing_manager.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

from app.custom_widgets.draw_pixels import DrawPixels

class Ui_DrawingManager(object):
    def setupUi(self, DrawingManager):
        if not DrawingManager.objectName():
            DrawingManager.setObjectName(u"DrawingManager")
        DrawingManager.resize(517, 650)
        self.gridLayout_2 = QGridLayout(DrawingManager)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.spin_height = QSpinBox(DrawingManager)
        self.spin_height.setObjectName(u"spin_height")
        self.spin_height.setMinimum(1)
        self.spin_height.setMaximum(1000)
        self.spin_height.setValue(28)

        self.gridLayout_2.addWidget(self.spin_height, 0, 1, 1, 1)

        self.container = QFrame(DrawingManager)
        self.container.setObjectName(u"container")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())
        self.container.setSizePolicy(sizePolicy)
        self.container.setStyleSheet(u"")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.container)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.draw_pixels = DrawPixels(self.container)
        self.draw_pixels.setObjectName(u"draw_pixels")
        sizePolicy.setHeightForWidth(self.draw_pixels.sizePolicy().hasHeightForWidth())
        self.draw_pixels.setSizePolicy(sizePolicy)
        self.draw_pixels.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.draw_pixels, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.container, 5, 0, 1, 3)

        self.lbl_width = QLabel(DrawingManager)
        self.lbl_width.setObjectName(u"lbl_width")

        self.gridLayout_2.addWidget(self.lbl_width, 0, 0, 1, 1)

        self.btn_save = QPushButton(DrawingManager)
        self.btn_save.setObjectName(u"btn_save")

        self.gridLayout_2.addWidget(self.btn_save, 1, 2, 1, 1)

        self.spin_width = QSpinBox(DrawingManager)
        self.spin_width.setObjectName(u"spin_width")
        self.spin_width.setMinimum(1)
        self.spin_width.setMaximum(1000)
        self.spin_width.setValue(28)

        self.gridLayout_2.addWidget(self.spin_width, 1, 1, 1, 1)

        self.lbl_height = QLabel(DrawingManager)
        self.lbl_height.setObjectName(u"lbl_height")

        self.gridLayout_2.addWidget(self.lbl_height, 1, 0, 1, 1)

        self.btn_load = QPushButton(DrawingManager)
        self.btn_load.setObjectName(u"btn_load")

        self.gridLayout_2.addWidget(self.btn_load, 0, 2, 1, 1)

        self.btn_clear = QPushButton(DrawingManager)
        self.btn_clear.setObjectName(u"btn_clear")

        self.gridLayout_2.addWidget(self.btn_clear, 2, 2, 1, 1)

        self.label = QLabel(DrawingManager)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.spin_thickness = QSpinBox(DrawingManager)
        self.spin_thickness.setObjectName(u"spin_thickness")
        self.spin_thickness.setMinimum(1)
        self.spin_thickness.setMaximum(50)
        self.spin_thickness.setValue(20)

        self.gridLayout_2.addWidget(self.spin_thickness, 2, 1, 1, 1)

        self.btn_fill = QPushButton(DrawingManager)
        self.btn_fill.setObjectName(u"btn_fill")

        self.gridLayout_2.addWidget(self.btn_fill, 3, 2, 1, 1)


        self.retranslateUi(DrawingManager)
        self.btn_clear.clicked.connect(DrawingManager.clear)
        self.btn_load.clicked.connect(DrawingManager.load)
        self.btn_save.clicked.connect(DrawingManager.save)
        self.spin_height.valueChanged.connect(self.draw_pixels.set_height)
        self.spin_thickness.valueChanged.connect(self.draw_pixels.set_thickness)
        self.spin_width.valueChanged.connect(self.draw_pixels.set_width)
        self.btn_fill.clicked.connect(DrawingManager.fill)

        QMetaObject.connectSlotsByName(DrawingManager)
    # setupUi

    def retranslateUi(self, DrawingManager):
        DrawingManager.setWindowTitle(QCoreApplication.translate("DrawingManager", u"Form", None))
        self.lbl_width.setText(QCoreApplication.translate("DrawingManager", u"Width", None))
        self.btn_save.setText(QCoreApplication.translate("DrawingManager", u"Save Image", None))
        self.lbl_height.setText(QCoreApplication.translate("DrawingManager", u"Height", None))
        self.btn_load.setText(QCoreApplication.translate("DrawingManager", u"Load Image", None))
        self.btn_clear.setText(QCoreApplication.translate("DrawingManager", u"Clear", None))
        self.label.setText(QCoreApplication.translate("DrawingManager", u"Thickness", None))
        self.btn_fill.setText(QCoreApplication.translate("DrawingManager", u"Fill", None))
    # retranslateUi

