# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpinBox, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

from app.custom_widgets.dataset_manager import DatasetManager
from app.custom_widgets.drawing_manager import DrawingManager
from app.custom_widgets.fields_creator import FieldsCreator
from app.custom_widgets.layers import (InputLayer, OutputLayer)
from app.custom_widgets.matplotlib_widget import MatplotlibWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(598, 509)
        self.action_save_model = QAction(MainWindow)
        self.action_save_model.setObjectName(u"action_save_model")
        self.action_load_model = QAction(MainWindow)
        self.action_load_model.setObjectName(u"action_load_model")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.layout_central = QGridLayout(self.central_widget)
        self.layout_central.setObjectName(u"layout_central")
        self.tab_model = QTabWidget(self.central_widget)
        self.tab_model.setObjectName(u"tab_model")
        self.tab_model.setDocumentMode(False)
        self.tab_model.setTabsClosable(False)
        self.create_model = QWidget()
        self.create_model.setObjectName(u"create_model")
        self.layout_create = QHBoxLayout(self.create_model)
        self.layout_create.setObjectName(u"layout_create")
        self.srcl_create_layers = QScrollArea(self.create_model)
        self.srcl_create_layers.setObjectName(u"srcl_create_layers")
        self.srcl_create_layers.setWidgetResizable(True)
        self.srcl_create_layers_content = QWidget()
        self.srcl_create_layers_content.setObjectName(u"srcl_create_layers_content")
        self.srcl_create_layers_content.setGeometry(QRect(0, 0, 554, 394))
        self.layout_create_layers = QHBoxLayout(self.srcl_create_layers_content)
        self.layout_create_layers.setObjectName(u"layout_create_layers")
        self.input_layer = InputLayer(self.srcl_create_layers_content)
        self.input_layer.setObjectName(u"input_layer")
        self.input_layer.setEnabled(True)

        self.layout_create_layers.addWidget(self.input_layer)

        self.line_2 = QFrame(self.srcl_create_layers_content)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.layout_create_layers.addWidget(self.line_2)

        self.layout_add = QGridLayout()
        self.layout_add.setObjectName(u"layout_add")
        self.btn_hidden_add = QPushButton(self.srcl_create_layers_content)
        self.btn_hidden_add.setObjectName(u"btn_hidden_add")

        self.layout_add.addWidget(self.btn_hidden_add, 0, 0, 1, 2, Qt.AlignTop)

        self.lbl_add_type = QLabel(self.srcl_create_layers_content)
        self.lbl_add_type.setObjectName(u"lbl_add_type")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_add_type.sizePolicy().hasHeightForWidth())
        self.lbl_add_type.setSizePolicy(sizePolicy)

        self.layout_add.addWidget(self.lbl_add_type, 1, 0, 1, 1)

        self.combo_add_type = QComboBox(self.srcl_create_layers_content)
        self.combo_add_type.addItem("")
        self.combo_add_type.addItem("")
        self.combo_add_type.addItem("")
        self.combo_add_type.addItem("")
        self.combo_add_type.addItem("")
        self.combo_add_type.setObjectName(u"combo_add_type")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.combo_add_type.sizePolicy().hasHeightForWidth())
        self.combo_add_type.setSizePolicy(sizePolicy1)
        self.combo_add_type.setMinimumSize(QSize(80, 0))

        self.layout_add.addWidget(self.combo_add_type, 1, 1, 1, 1)


        self.layout_create_layers.addLayout(self.layout_add)

        self.line_3 = QFrame(self.srcl_create_layers_content)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setFrameShape(QFrame.VLine)

        self.layout_create_layers.addWidget(self.line_3)

        self.output_layer = OutputLayer(self.srcl_create_layers_content)
        self.output_layer.setObjectName(u"output_layer")

        self.layout_create_layers.addWidget(self.output_layer)

        self.srcl_create_layers.setWidget(self.srcl_create_layers_content)

        self.layout_create.addWidget(self.srcl_create_layers)

        self.tab_model.addTab(self.create_model, "")
        self.train_model = QWidget()
        self.train_model.setObjectName(u"train_model")
        self.layout_train = QGridLayout(self.train_model)
        self.layout_train.setObjectName(u"layout_train")
        self.spin_train_batch = QSpinBox(self.train_model)
        self.spin_train_batch.setObjectName(u"spin_train_batch")
        self.spin_train_batch.setMinimum(1)
        self.spin_train_batch.setMaximum(1024)
        self.spin_train_batch.setValue(64)

        self.layout_train.addWidget(self.spin_train_batch, 5, 1, 1, 1)

        self.lbl_train_epochs = QLabel(self.train_model)
        self.lbl_train_epochs.setObjectName(u"lbl_train_epochs")

        self.layout_train.addWidget(self.lbl_train_epochs, 4, 0, 1, 1)

        self.lbl_train_file = QLabel(self.train_model)
        self.lbl_train_file.setObjectName(u"lbl_train_file")

        self.layout_train.addWidget(self.lbl_train_file, 0, 0, 1, 1)

        self.btn_train_file = QPushButton(self.train_model)
        self.btn_train_file.setObjectName(u"btn_train_file")

        self.layout_train.addWidget(self.btn_train_file, 1, 0, 1, 1)

        self.cbx_train_validation = QCheckBox(self.train_model)
        self.cbx_train_validation.setObjectName(u"cbx_train_validation")

        self.layout_train.addWidget(self.cbx_train_validation, 1, 1, 1, 1)

        self.btn_train_generate_model = QPushButton(self.train_model)
        self.btn_train_generate_model.setObjectName(u"btn_train_generate_model")

        self.layout_train.addWidget(self.btn_train_generate_model, 2, 0, 1, 2)

        self.lbl_train_batch = QLabel(self.train_model)
        self.lbl_train_batch.setObjectName(u"lbl_train_batch")

        self.layout_train.addWidget(self.lbl_train_batch, 5, 0, 1, 1)

        self.line_4 = QFrame(self.train_model)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.layout_train.addWidget(self.line_4, 0, 2, 8, 1)

        self.layout_train_metrics = QVBoxLayout()
        self.layout_train_metrics.setObjectName(u"layout_train_metrics")
        self.lbl_train_metrics = QLabel(self.train_model)
        self.lbl_train_metrics.setObjectName(u"lbl_train_metrics")

        self.layout_train_metrics.addWidget(self.lbl_train_metrics, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.plot_train_metrics = MatplotlibWidget(self.train_model)
        self.plot_train_metrics.setObjectName(u"plot_train_metrics")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plot_train_metrics.sizePolicy().hasHeightForWidth())
        self.plot_train_metrics.setSizePolicy(sizePolicy2)

        self.layout_train_metrics.addWidget(self.plot_train_metrics)


        self.layout_train.addLayout(self.layout_train_metrics, 0, 3, 8, 1)

        self.combo_train_file = QComboBox(self.train_model)
        self.combo_train_file.addItem("")
        self.combo_train_file.setObjectName(u"combo_train_file")

        self.layout_train.addWidget(self.combo_train_file, 0, 1, 1, 1)

        self.spin_train_epochs = QSpinBox(self.train_model)
        self.spin_train_epochs.setObjectName(u"spin_train_epochs")
        self.spin_train_epochs.setMinimum(1)
        self.spin_train_epochs.setMaximum(100)
        self.spin_train_epochs.setValue(5)

        self.layout_train.addWidget(self.spin_train_epochs, 4, 1, 1, 1)

        self.btn_train_start = QPushButton(self.train_model)
        self.btn_train_start.setObjectName(u"btn_train_start")

        self.layout_train.addWidget(self.btn_train_start, 7, 0, 1, 2)

        self.cbx_train_continue = QCheckBox(self.train_model)
        self.cbx_train_continue.setObjectName(u"cbx_train_continue")

        self.layout_train.addWidget(self.cbx_train_continue, 6, 0, 1, 1)

        self.tab_model.addTab(self.train_model, "")
        self.use_model = QWidget()
        self.use_model.setObjectName(u"use_model")
        self.layout_use = QGridLayout(self.use_model)
        self.layout_use.setObjectName(u"layout_use")
        self.btn_use_file = QPushButton(self.use_model)
        self.btn_use_file.setObjectName(u"btn_use_file")

        self.layout_use.addWidget(self.btn_use_file, 0, 3, 1, 1)

        self.btn_use_run = QPushButton(self.use_model)
        self.btn_use_run.setObjectName(u"btn_use_run")

        self.layout_use.addWidget(self.btn_use_run, 1, 3, 1, 1)

        self.tab_use_type = QTabWidget(self.use_model)
        self.tab_use_type.setObjectName(u"tab_use_type")
        self.tab_use_type.setDocumentMode(False)
        self.use_image = QWidget()
        self.use_image.setObjectName(u"use_image")
        self.layout_use_image = QGridLayout(self.use_image)
        self.layout_use_image.setObjectName(u"layout_use_image")
        self.drawing_manager = DrawingManager(self.use_image)
        self.drawing_manager.setObjectName(u"drawing_manager")

        self.layout_use_image.addWidget(self.drawing_manager, 0, 0, 1, 2)

        self.tab_use_type.addTab(self.use_image, "")
        self.use_flat = QWidget()
        self.use_flat.setObjectName(u"use_flat")
        self.layout_use_flat = QGridLayout(self.use_flat)
        self.layout_use_flat.setObjectName(u"layout_use_flat")
        self.btn_use_set_inputs = QPushButton(self.use_flat)
        self.btn_use_set_inputs.setObjectName(u"btn_use_set_inputs")

        self.layout_use_flat.addWidget(self.btn_use_set_inputs, 0, 0, 1, 1)

        self.spin_use_set_inputs = QSpinBox(self.use_flat)
        self.spin_use_set_inputs.setObjectName(u"spin_use_set_inputs")
        self.spin_use_set_inputs.setMinimum(1)
        self.spin_use_set_inputs.setValue(1)

        self.layout_use_flat.addWidget(self.spin_use_set_inputs, 0, 1, 1, 1)

        self.lbl_use_flat_name = QLabel(self.use_flat)
        self.lbl_use_flat_name.setObjectName(u"lbl_use_flat_name")

        self.layout_use_flat.addWidget(self.lbl_use_flat_name, 1, 0, 1, 1, Qt.AlignRight)

        self.lbl_use_flat_value = QLabel(self.use_flat)
        self.lbl_use_flat_value.setObjectName(u"lbl_use_flat_value")

        self.layout_use_flat.addWidget(self.lbl_use_flat_value, 1, 1, 1, 1, Qt.AlignRight)

        self.inputs_use_flat = FieldsCreator(self.use_flat)
        self.inputs_use_flat.setObjectName(u"inputs_use_flat")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.inputs_use_flat.sizePolicy().hasHeightForWidth())
        self.inputs_use_flat.setSizePolicy(sizePolicy3)

        self.layout_use_flat.addWidget(self.inputs_use_flat, 2, 0, 1, 2)

        self.tab_use_type.addTab(self.use_flat, "")

        self.layout_use.addWidget(self.tab_use_type, 0, 1, 3, 1)

        self.lbl_use_result = QLabel(self.use_model)
        self.lbl_use_result.setObjectName(u"lbl_use_result")

        self.layout_use.addWidget(self.lbl_use_result, 2, 3, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.tab_model.addTab(self.use_model, "")
        self.data = QWidget()
        self.data.setObjectName(u"data")
        self.gridLayout = QGridLayout(self.data)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = DatasetManager(self.data)
        self.widget.setObjectName(u"widget")

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.tab_model.addTab(self.data, "")

        self.layout_central.addWidget(self.tab_model, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 598, 26))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menu_file.addAction(self.action_save_model)
        self.menu_file.addAction(self.action_load_model)

        self.retranslateUi(MainWindow)
        self.btn_hidden_add.clicked.connect(MainWindow.create_add_layer)
        self.btn_train_file.clicked.connect(MainWindow.train_choose_data)
        self.btn_use_set_inputs.clicked.connect(MainWindow.use_set_inputs)
        self.btn_use_file.clicked.connect(MainWindow.use_choose_represent_file)
        self.btn_train_start.clicked.connect(MainWindow.train_start)
        self.btn_use_run.clicked.connect(MainWindow.use_predict_sample)
        self.btn_train_generate_model.clicked.connect(MainWindow.train_generate_model)
        self.action_load_model.triggered.connect(MainWindow.menu_load_model)
        self.action_save_model.triggered.connect(MainWindow.menu_save_model)

        self.tab_model.setCurrentIndex(0)
        self.tab_use_type.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Neural helper", None))
        self.action_save_model.setText(QCoreApplication.translate("MainWindow", u"Save model", None))
        self.action_load_model.setText(QCoreApplication.translate("MainWindow", u"Load model", None))
        self.btn_hidden_add.setText(QCoreApplication.translate("MainWindow", u"Add layer", None))
        self.lbl_add_type.setText(QCoreApplication.translate("MainWindow", u"Layer type", None))
        self.combo_add_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Dense", None))
        self.combo_add_type.setItemText(1, QCoreApplication.translate("MainWindow", u"LSTM", None))
        self.combo_add_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Dropout", None))
        self.combo_add_type.setItemText(3, QCoreApplication.translate("MainWindow", u"Conv2D", None))
        self.combo_add_type.setItemText(4, QCoreApplication.translate("MainWindow", u"Maxpooling", None))

        self.tab_model.setTabText(self.tab_model.indexOf(self.create_model), QCoreApplication.translate("MainWindow", u"Create model", None))
        self.lbl_train_epochs.setText(QCoreApplication.translate("MainWindow", u"Epochs", None))
        self.lbl_train_file.setText(QCoreApplication.translate("MainWindow", u"File type", None))
        self.btn_train_file.setText(QCoreApplication.translate("MainWindow", u"Choose train data file", None))
        self.cbx_train_validation.setText(QCoreApplication.translate("MainWindow", u"Have validation data", None))
        self.btn_train_generate_model.setText(QCoreApplication.translate("MainWindow", u"Generate model", None))
        self.lbl_train_batch.setText(QCoreApplication.translate("MainWindow", u"Batch size", None))
        self.lbl_train_metrics.setText(QCoreApplication.translate("MainWindow", u"Metrics", None))
        self.combo_train_file.setItemText(0, QCoreApplication.translate("MainWindow", u".py", None))

        self.btn_train_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.cbx_train_continue.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.tab_model.setTabText(self.tab_model.indexOf(self.train_model), QCoreApplication.translate("MainWindow", u"Train model", None))
        self.btn_use_file.setText(QCoreApplication.translate("MainWindow", u"Choose .py file to represent result", None))
        self.btn_use_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.tab_use_type.setTabText(self.tab_use_type.indexOf(self.use_image), QCoreApplication.translate("MainWindow", u"Image", None))
        self.btn_use_set_inputs.setText(QCoreApplication.translate("MainWindow", u"Set number of inputs", None))
        self.lbl_use_flat_name.setText(QCoreApplication.translate("MainWindow", u"Field name", None))
        self.lbl_use_flat_value.setText(QCoreApplication.translate("MainWindow", u"Field value", None))
        self.tab_use_type.setTabText(self.tab_use_type.indexOf(self.use_flat), QCoreApplication.translate("MainWindow", u"Flat", None))
        self.lbl_use_result.setText("")
        self.tab_model.setTabText(self.tab_model.indexOf(self.use_model), QCoreApplication.translate("MainWindow", u"Use model", None))
        self.tab_model.setTabText(self.tab_model.indexOf(self.data), QCoreApplication.translate("MainWindow", u"Dataset", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

