# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lstm_layer.ui'
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

class Ui_LSTMLayer(object):
    def setupUi(self, LSTMLayer):
        if not LSTMLayer.objectName():
            LSTMLayer.setObjectName(u"LSTMLayer")
        LSTMLayer.resize(524, 187)
        self.gridLayout = QGridLayout(LSTMLayer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_activation = QLabel(LSTMLayer)
        self.lbl_activation.setObjectName(u"lbl_activation")

        self.gridLayout.addWidget(self.lbl_activation, 3, 0, 1, 1)

        self.combo_regularizer = QComboBox(LSTMLayer)
        self.combo_regularizer.addItem("")
        self.combo_regularizer.addItem("")
        self.combo_regularizer.addItem("")
        self.combo_regularizer.setObjectName(u"combo_regularizer")
        self.combo_regularizer.setEnabled(True)

        self.gridLayout.addWidget(self.combo_regularizer, 5, 1, 1, 1)

        self.spin_units = QSpinBox(LSTMLayer)
        self.spin_units.setObjectName(u"spin_units")
        self.spin_units.setMinimum(1)
        self.spin_units.setMaximum(10000)

        self.gridLayout.addWidget(self.spin_units, 2, 1, 1, 1)

        self.combo_activation = QComboBox(LSTMLayer)
        self.combo_activation.addItem("")
        self.combo_activation.addItem("")
        self.combo_activation.addItem("")
        self.combo_activation.setObjectName(u"combo_activation")

        self.gridLayout.addWidget(self.combo_activation, 3, 1, 1, 1)

        self.lbl_regularizer = QLabel(LSTMLayer)
        self.lbl_regularizer.setObjectName(u"lbl_regularizer")
        self.lbl_regularizer.setEnabled(True)

        self.gridLayout.addWidget(self.lbl_regularizer, 5, 0, 1, 1)

        self.lbl_recurrent_activation = QLabel(LSTMLayer)
        self.lbl_recurrent_activation.setObjectName(u"lbl_recurrent_activation")

        self.gridLayout.addWidget(self.lbl_recurrent_activation, 4, 0, 1, 1)

        self.btn_delete = QPushButton(LSTMLayer)
        self.btn_delete.setObjectName(u"btn_delete")

        self.gridLayout.addWidget(self.btn_delete, 1, 0, 1, 2)

        self.lbl_units = QLabel(LSTMLayer)
        self.lbl_units.setObjectName(u"lbl_units")

        self.gridLayout.addWidget(self.lbl_units, 2, 0, 1, 1)

        self.lbl_name = QLabel(LSTMLayer)
        self.lbl_name.setObjectName(u"lbl_name")

        self.gridLayout.addWidget(self.lbl_name, 0, 0, 1, 2, Qt.AlignHCenter|Qt.AlignTop)

        self.combo_recurrent_activation = QComboBox(LSTMLayer)
        self.combo_recurrent_activation.addItem("")
        self.combo_recurrent_activation.addItem("")
        self.combo_recurrent_activation.addItem("")
        self.combo_recurrent_activation.setObjectName(u"combo_recurrent_activation")

        self.gridLayout.addWidget(self.combo_recurrent_activation, 4, 1, 1, 1)

        self.cbx_return_sequences = QCheckBox(LSTMLayer)
        self.cbx_return_sequences.setObjectName(u"cbx_return_sequences")

        self.gridLayout.addWidget(self.cbx_return_sequences, 6, 0, 1, 1)


        self.retranslateUi(LSTMLayer)
        self.btn_delete.clicked.connect(LSTMLayer.delete_layer)

        QMetaObject.connectSlotsByName(LSTMLayer)
    # setupUi

    def retranslateUi(self, LSTMLayer):
        LSTMLayer.setWindowTitle(QCoreApplication.translate("LSTMLayer", u"Form", None))
        self.lbl_activation.setText(QCoreApplication.translate("LSTMLayer", u"Activation", None))
        self.combo_regularizer.setItemText(0, QCoreApplication.translate("LSTMLayer", u"L1", None))
        self.combo_regularizer.setItemText(1, QCoreApplication.translate("LSTMLayer", u"L2", None))
        self.combo_regularizer.setItemText(2, QCoreApplication.translate("LSTMLayer", u"None", None))

        self.combo_activation.setItemText(0, QCoreApplication.translate("LSTMLayer", u"Sigmoid", None))
        self.combo_activation.setItemText(1, QCoreApplication.translate("LSTMLayer", u"Tanh", None))
        self.combo_activation.setItemText(2, QCoreApplication.translate("LSTMLayer", u"Relu", None))

        self.lbl_regularizer.setText(QCoreApplication.translate("LSTMLayer", u"Regularizer ", None))
        self.lbl_recurrent_activation.setText(QCoreApplication.translate("LSTMLayer", u"Recurrent activation", None))
        self.btn_delete.setText(QCoreApplication.translate("LSTMLayer", u"Delete layer", None))
        self.lbl_units.setText(QCoreApplication.translate("LSTMLayer", u"Units", None))
        self.lbl_name.setText(QCoreApplication.translate("LSTMLayer", u"LSTM", None))
        self.combo_recurrent_activation.setItemText(0, QCoreApplication.translate("LSTMLayer", u"Sigmoid", None))
        self.combo_recurrent_activation.setItemText(1, QCoreApplication.translate("LSTMLayer", u"Tanh", None))
        self.combo_recurrent_activation.setItemText(2, QCoreApplication.translate("LSTMLayer", u"Relu", None))

        self.cbx_return_sequences.setText(QCoreApplication.translate("LSTMLayer", u"Return sequences", None))
    # retranslateUi

