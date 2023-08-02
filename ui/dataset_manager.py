# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataset_manager.ui'
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

from app.custom_widgets.custom_widget import ClickableImageLabel
from app.custom_widgets.fields_creator import FieldsCreator

class Ui_DatasetManager(object):
    def setupUi(self, DatasetManager):
        if not DatasetManager.objectName():
            DatasetManager.setObjectName(u"DatasetManager")
        DatasetManager.resize(840, 696)
        self.gridLayout = QGridLayout(DatasetManager)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_height = QLabel(DatasetManager)
        self.lbl_height.setObjectName(u"lbl_height")

        self.gridLayout.addWidget(self.lbl_height, 0, 1, 1, 1)

        self.btn_create_dataset = QPushButton(DatasetManager)
        self.btn_create_dataset.setObjectName(u"btn_create_dataset")

        self.gridLayout.addWidget(self.btn_create_dataset, 0, 3, 1, 1)

        self.btn_choose_dataset = QPushButton(DatasetManager)
        self.btn_choose_dataset.setObjectName(u"btn_choose_dataset")

        self.gridLayout.addWidget(self.btn_choose_dataset, 1, 3, 1, 1)

        self.btn_save_dataset = QPushButton(DatasetManager)
        self.btn_save_dataset.setObjectName(u"btn_save_dataset")

        self.gridLayout.addWidget(self.btn_save_dataset, 2, 3, 1, 1)

        self.btn_choose_image = QPushButton(DatasetManager)
        self.btn_choose_image.setObjectName(u"btn_choose_image")

        self.gridLayout.addWidget(self.btn_choose_image, 4, 1, 1, 1)

        self.spin_ouputs = QSpinBox(DatasetManager)
        self.spin_ouputs.setObjectName(u"spin_ouputs")
        self.spin_ouputs.setMinimum(1)
        self.spin_ouputs.setMaximum(1000)

        self.gridLayout.addWidget(self.spin_ouputs, 3, 3, 1, 1)

        self.btn_set_outputs = QPushButton(DatasetManager)
        self.btn_set_outputs.setObjectName(u"btn_set_outputs")

        self.gridLayout.addWidget(self.btn_set_outputs, 4, 3, 1, 1)

        self.cbx_same_size = QCheckBox(DatasetManager)
        self.cbx_same_size.setObjectName(u"cbx_same_size")

        self.gridLayout.addWidget(self.cbx_same_size, 3, 1, 1, 1)

        self.lbl_width = QLabel(DatasetManager)
        self.lbl_width.setObjectName(u"lbl_width")

        self.gridLayout.addWidget(self.lbl_width, 1, 1, 1, 1)

        self.btn_zoom = QPushButton(DatasetManager)
        self.btn_zoom.setObjectName(u"btn_zoom")

        self.gridLayout.addWidget(self.btn_zoom, 4, 2, 1, 1)

        self.spin_height = QSpinBox(DatasetManager)
        self.spin_height.setObjectName(u"spin_height")
        self.spin_height.setMinimum(1)
        self.spin_height.setMaximum(10000)
        self.spin_height.setValue(5)

        self.gridLayout.addWidget(self.spin_height, 0, 2, 1, 1)

        self.spin_width = QSpinBox(DatasetManager)
        self.spin_width.setObjectName(u"spin_width")
        self.spin_width.setMinimum(1)
        self.spin_width.setMaximum(10000)
        self.spin_width.setValue(5)

        self.gridLayout.addWidget(self.spin_width, 1, 2, 1, 1)

        self.spin_speed = QSpinBox(DatasetManager)
        self.spin_speed.setObjectName(u"spin_speed")
        self.spin_speed.setMinimum(1)
        self.spin_speed.setMaximum(1000)

        self.gridLayout.addWidget(self.spin_speed, 2, 2, 1, 1)

        self.lbl_speed = QLabel(DatasetManager)
        self.lbl_speed.setObjectName(u"lbl_speed")

        self.gridLayout.addWidget(self.lbl_speed, 2, 1, 1, 1)

        self.lbl_position = QLabel(DatasetManager)
        self.lbl_position.setObjectName(u"lbl_position")

        self.gridLayout.addWidget(self.lbl_position, 3, 2, 1, 1)

        self.container = QWidget(DatasetManager)
        self.container.setObjectName(u"container")
        self.gridLayout_2 = QGridLayout(self.container)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_image = ClickableImageLabel(self.container)
        self.lbl_image.setObjectName(u"lbl_image")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_image.sizePolicy().hasHeightForWidth())
        self.lbl_image.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lbl_image, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout.addWidget(self.container, 5, 1, 1, 2)

        self.fields_expected = FieldsCreator(DatasetManager)
        self.fields_expected.setObjectName(u"fields_expected")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fields_expected.sizePolicy().hasHeightForWidth())
        self.fields_expected.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.fields_expected, 5, 3, 1, 1)


        self.retranslateUi(DatasetManager)
        self.btn_choose_image.clicked.connect(DatasetManager.load_image)
        self.btn_set_outputs.clicked.connect(DatasetManager.set_outputs)
        self.spin_height.valueChanged.connect(DatasetManager.set_height)
        self.spin_speed.valueChanged.connect(DatasetManager.set_speed)
        self.cbx_same_size.stateChanged.connect(DatasetManager.set_same_size)
        self.btn_zoom.clicked.connect(DatasetManager.zoom)
        self.spin_width.valueChanged.connect(DatasetManager.set_width)
        self.btn_choose_dataset.clicked.connect(DatasetManager.choose_dataset)
        self.btn_create_dataset.clicked.connect(DatasetManager.create_dataset)
        self.btn_save_dataset.clicked.connect(DatasetManager.save_dataset)

        QMetaObject.connectSlotsByName(DatasetManager)
    # setupUi

    def retranslateUi(self, DatasetManager):
        DatasetManager.setWindowTitle(QCoreApplication.translate("DatasetManager", u"Form", None))
        self.lbl_height.setText(QCoreApplication.translate("DatasetManager", u"Height", None))
        self.btn_create_dataset.setText(QCoreApplication.translate("DatasetManager", u"Create dataset", None))
        self.btn_choose_dataset.setText(QCoreApplication.translate("DatasetManager", u"Choose dataset", None))
        self.btn_save_dataset.setText(QCoreApplication.translate("DatasetManager", u"Save dataset", None))
        self.btn_choose_image.setText(QCoreApplication.translate("DatasetManager", u"Choose image", None))
        self.btn_set_outputs.setText(QCoreApplication.translate("DatasetManager", u"Set number of outputs", None))
        self.cbx_same_size.setText(QCoreApplication.translate("DatasetManager", u"Same", None))
        self.lbl_width.setText(QCoreApplication.translate("DatasetManager", u"Width", None))
        self.btn_zoom.setText(QCoreApplication.translate("DatasetManager", u"Zoom in", None))
        self.lbl_speed.setText(QCoreApplication.translate("DatasetManager", u"Moving speed", None))
        self.lbl_position.setText(QCoreApplication.translate("DatasetManager", u"Current position:", None))
        self.lbl_image.setText(QCoreApplication.translate("DatasetManager", u"Image placeholder", None))
    # retranslateUi

