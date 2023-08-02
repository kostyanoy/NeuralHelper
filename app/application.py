import os

import numpy as np
from PySide6.QtGui import QImage
from PySide6.QtWidgets import QMainWindow, QFileDialog

from app.custom_widgets.custom_widget import VLine
from app.custom_widgets.layers import DenseLayer, DropoutLayer, Conv2DLayer, MaxpoolingLayer, LSTMLayer
from app.custom_widgets.matplotlib_widget import MatplotlibWidget
from ui.main_window import Ui_MainWindow
from utils import importer
from utils.model_manager import ModelManager


# main application
class App(QMainWindow):
    STATUS_BAR_MSG = 5000  # milli of showing message to user in status bar
    PYTHON_TRAIN_ATTRS = ["load_data"]  # required methods in train file
    REPR_ATTRS = ["represent"]  # required methods in represent file
    LAYERS = {
        "Dense": DenseLayer,
        "Dropout": DropoutLayer,
        "Conv2D": Conv2DLayer,
        "Maxpooling": MaxpoolingLayer,
        "LSTM": LSTMLayer,
    }  # possible layers

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.is_training = False  # if model is currently training

        self.model_manager = ModelManager(self)
        self.model_manager.message.connect(self.show_status)
        self.model_manager.finished.connect(self.train_stop)

        self.train_file = None
        self.represent_file = None

    # show message in status bar for STATUS_BAR_MSG mls
    def show_status(self, msg: str):
        self.statusBar().showMessage(msg, self.STATUS_BAR_MSG)

    # get graph widget
    def get_metrics_graph(self) -> MatplotlibWidget:
        return self.ui.plot_train_metrics

    # add layer and separate line
    def create_add_layer(self):
        layer = self.ui.layout_create_layers
        indx = layer.count() - 3
        layer.insertWidget(indx, VLine())

        curText = self.ui.combo_add_type.currentText()

        layer.insertWidget(indx, self.LAYERS[curText]())

    # generate model from user interactive
    def train_generate_model(self):
        suc = self.model_manager.generate_model()
        if suc:
            self.show_status("Model generated")
        else:
            self.show_status("Something wrong with model")

    # start and stop training model
    def train_start(self):
        if not self.model_manager.have_model():
            self.show_status("Create model first")
            return
        if self.train_file is None:
            self.show_status("Choose train file")
            return

        if self.is_training:
            self.model_manager.stop()  # model stop when it is ready
        else:
            self.is_training = True
            self.ui.btn_train_start.setText("Stop")
            self.show_status("Training in progress...")

            self.model_manager.set_data(self.train_file)
            self.model_manager.start()

    # stop training after current epoch
    def train_stop(self):
        self.is_training = False
        self.ui.btn_train_start.setText("Start")

    # choose file with training data
    def train_choose_data(self):
        file, _ = QFileDialog.getOpenFileName(self, "Choose train data", "",
                                              f"(*{self.ui.combo_train_file.currentText()})")
        if not file:
            return
        module = importer.import_by_path(file)
        msg, suc = importer.check_module_vars(module, self.PYTHON_TRAIN_ATTRS)
        if suc:
            self.train_file = module
            self.ui.btn_train_file.setText(os.path.split(file)[1])
        self.show_status(msg)

    # set flat inputs
    def use_set_inputs(self):
        inputs = self.ui.spin_use_set_inputs.value()
        self.ui.inputs_use_flat.set_inputs(inputs)

    # choose .py file that can format output of model
    def use_choose_represent_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Choose represent file", "",
                                              f"(*.py)")
        if not file:
            return
        module = importer.import_by_path(file)
        msg, suc = importer.check_module_vars(module, self.REPR_ATTRS)
        if suc:
            self.represent_file = module
            self.ui.btn_use_file.setText(os.path.split(file)[1])
        self.show_status(msg)

    # give sample generated by user to model
    def use_predict_sample(self):
        if not self.model_manager.have_model():
            self.show_status("Create model first")
            return
        if self.represent_file is None:
            self.show_status("Choose represent file")
            return

        tab = self.ui.tab_use_type
        # choose image or flat type
        x = self.get_image_sample() if tab.currentIndex() == 0 else self.get_flat_sample()

        try:
            p = self.model_manager.sample(x)

            self.ui.lbl_use_result.setText(self.represent_file.represent(p))
        except ValueError:
            self.show_status("Input didn't match model's expectations")

    # image to numpy array
    def get_image_sample(self):
        image = self.ui.drawing_manager.get_image()
        incoming_image = image.convertToFormat(QImage.Format_Grayscale8)
        width = incoming_image.width()
        height = incoming_image.height()
        ptr = incoming_image.constBits()
        x = np.frombuffer(ptr, np.uint8).reshape((1, height, width)) / 255
        return x

    # get flat inputs
    def get_flat_sample(self):
        return self.ui.inputs_use_flat.get_inputs()

    # load model from file
    def menu_load_model(self):
        file, _ = QFileDialog.getOpenFileName(self, "Choose save file", "",
                                              f"(*.keras);;(*.h5)")
        if not file:
            return

        self.model_manager.load_model(file)
        self.show_status("Model loaded")

    # save model to file
    def menu_save_model(self):
        if not self.model_manager.have_model():
            self.show_status("Create model first")
            return

        file, _ = QFileDialog.getSaveFileName(self, "Choose save file", "",
                                              f"(*.keras);;(*.h5)")
        if not file:
            return
        self.model_manager.save_model(file)
        self.show_status("Model saved")
