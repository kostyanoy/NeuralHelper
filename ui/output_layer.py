# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'output_layer.ui'
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
    QLabel, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_OutputLayer(object):
    def setupUi(self, OutputLayer):
        if not OutputLayer.objectName():
            OutputLayer.setObjectName(u"OutputLayer")
        OutputLayer.resize(218, 275)
        self.gridLayout = QGridLayout(OutputLayer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_neurons = QLabel(OutputLayer)
        self.lbl_neurons.setObjectName(u"lbl_neurons")

        self.gridLayout.addWidget(self.lbl_neurons, 1, 0, 1, 1)

        self.spin_neurons = QSpinBox(OutputLayer)
        self.spin_neurons.setObjectName(u"spin_neurons")
        self.spin_neurons.setMinimum(1)
        self.spin_neurons.setMaximum(10000)

        self.gridLayout.addWidget(self.spin_neurons, 1, 1, 1, 1)

        self.lbl_activation = QLabel(OutputLayer)
        self.lbl_activation.setObjectName(u"lbl_activation")

        self.gridLayout.addWidget(self.lbl_activation, 2, 0, 1, 1)

        self.combo_activation = QComboBox(OutputLayer)
        self.combo_activation.addItem("")
        self.combo_activation.addItem("")
        self.combo_activation.addItem("")
        self.combo_activation.addItem("")
        self.combo_activation.addItem("")
        self.combo_activation.setObjectName(u"combo_activation")

        self.gridLayout.addWidget(self.combo_activation, 2, 1, 1, 1)

        self.lbl_optimizer = QLabel(OutputLayer)
        self.lbl_optimizer.setObjectName(u"lbl_optimizer")

        self.gridLayout.addWidget(self.lbl_optimizer, 3, 0, 1, 1)

        self.combo_optimizer = QComboBox(OutputLayer)
        self.combo_optimizer.addItem("")
        self.combo_optimizer.setObjectName(u"combo_optimizer")

        self.gridLayout.addWidget(self.combo_optimizer, 3, 1, 1, 1)

        self.lbl_loss = QLabel(OutputLayer)
        self.lbl_loss.setObjectName(u"lbl_loss")

        self.gridLayout.addWidget(self.lbl_loss, 4, 0, 1, 1)

        self.combo_loss = QComboBox(OutputLayer)
        self.combo_loss.addItem("")
        self.combo_loss.addItem("")
        self.combo_loss.setObjectName(u"combo_loss")

        self.gridLayout.addWidget(self.combo_loss, 4, 1, 1, 1)

        self.lbl_metrics = QLabel(OutputLayer)
        self.lbl_metrics.setObjectName(u"lbl_metrics")

        self.gridLayout.addWidget(self.lbl_metrics, 5, 0, 1, 1)

        self.layout_metrics = QVBoxLayout()
        self.layout_metrics.setObjectName(u"layout_metrics")
        self.cbx_train_accuracy = QCheckBox(OutputLayer)
        self.cbx_train_accuracy.setObjectName(u"cbx_train_accuracy")

        self.layout_metrics.addWidget(self.cbx_train_accuracy)

        self.cbx_val_accuracy = QCheckBox(OutputLayer)
        self.cbx_val_accuracy.setObjectName(u"cbx_val_accuracy")

        self.layout_metrics.addWidget(self.cbx_val_accuracy)

        self.cbx_train_loss = QCheckBox(OutputLayer)
        self.cbx_train_loss.setObjectName(u"cbx_train_loss")

        self.layout_metrics.addWidget(self.cbx_train_loss)

        self.cbx_val_loss = QCheckBox(OutputLayer)
        self.cbx_val_loss.setObjectName(u"cbx_val_loss")

        self.layout_metrics.addWidget(self.cbx_val_loss)

        self.cbx_train_auc = QCheckBox(OutputLayer)
        self.cbx_train_auc.setObjectName(u"cbx_train_auc")

        self.layout_metrics.addWidget(self.cbx_train_auc)

        self.cbx_val_auc = QCheckBox(OutputLayer)
        self.cbx_val_auc.setObjectName(u"cbx_val_auc")

        self.layout_metrics.addWidget(self.cbx_val_auc)


        self.gridLayout.addLayout(self.layout_metrics, 5, 1, 1, 1)

        self.lbl_name = QLabel(OutputLayer)
        self.lbl_name.setObjectName(u"lbl_name")

        self.gridLayout.addWidget(self.lbl_name, 0, 0, 1, 2, Qt.AlignHCenter|Qt.AlignTop)


        self.retranslateUi(OutputLayer)

        QMetaObject.connectSlotsByName(OutputLayer)
    # setupUi

    def retranslateUi(self, OutputLayer):
        OutputLayer.setWindowTitle(QCoreApplication.translate("OutputLayer", u"Form", None))
        self.lbl_neurons.setText(QCoreApplication.translate("OutputLayer", u"Neurons", None))
        self.lbl_activation.setText(QCoreApplication.translate("OutputLayer", u"Activation", None))
        self.combo_activation.setItemText(0, QCoreApplication.translate("OutputLayer", u"Softmax", None))
        self.combo_activation.setItemText(1, QCoreApplication.translate("OutputLayer", u"Tanh", None))
        self.combo_activation.setItemText(2, QCoreApplication.translate("OutputLayer", u"Sigmoid", None))
        self.combo_activation.setItemText(3, QCoreApplication.translate("OutputLayer", u"Linear", None))
        self.combo_activation.setItemText(4, QCoreApplication.translate("OutputLayer", u"Relu", None))

        self.lbl_optimizer.setText(QCoreApplication.translate("OutputLayer", u"Optimizer", None))
        self.combo_optimizer.setItemText(0, QCoreApplication.translate("OutputLayer", u"Adam", None))

        self.lbl_loss.setText(QCoreApplication.translate("OutputLayer", u"Loss", None))
        self.combo_loss.setItemText(0, QCoreApplication.translate("OutputLayer", u"Categorical crossentropy", None))
        self.combo_loss.setItemText(1, QCoreApplication.translate("OutputLayer", u"MSE", None))

        self.lbl_metrics.setText(QCoreApplication.translate("OutputLayer", u"Metrics", None))
        self.cbx_train_accuracy.setText(QCoreApplication.translate("OutputLayer", u"Train Accuracy", None))
        self.cbx_val_accuracy.setText(QCoreApplication.translate("OutputLayer", u"Validation Accuracy", None))
        self.cbx_train_loss.setText(QCoreApplication.translate("OutputLayer", u"Train Loss", None))
        self.cbx_val_loss.setText(QCoreApplication.translate("OutputLayer", u"Validation Loss", None))
        self.cbx_train_auc.setText(QCoreApplication.translate("OutputLayer", u"Training AUC", None))
        self.cbx_val_auc.setText(QCoreApplication.translate("OutputLayer", u"Validation AUC", None))
        self.lbl_name.setText(QCoreApplication.translate("OutputLayer", u"Output", None))
    # retranslateUi

