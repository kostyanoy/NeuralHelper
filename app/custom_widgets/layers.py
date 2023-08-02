from PySide6.QtWidgets import QLabel, QSpinBox
from keras import Input, regularizers
from keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Dropout, LSTM
from keras.metrics import AUC

from app.custom_widgets.custom_widget import CustomWidget
from ui.conv2d_layer import Ui_Conv2DLayer
from ui.dense_layer import Ui_DenseLayer
from ui.dropout_layer import Ui_DropoutLayer
from ui.input_layer import Ui_InputLayer
from ui.lstm_layer import Ui_LSTMLayer
from ui.maxpooling_layer import Ui_MaxpoolingLayer
from ui.output_layer import Ui_OutputLayer


# abstract layer class for neural network
class Layer(CustomWidget):
    ACTIVATION = {
        "Linear": "linear",
        "Sigmoid": "sigmoid",
        "Tanh": "tanh",
        "Relu": "relu",
        "Softmax": "softmax"
    }  # activation functions

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set activation options
        try:
            self.ui.combo_activation.clear()
            self.ui.combo_activation.addItems(self.ACTIVATION.keys())
        except AttributeError:  # if layer has not activation options
            pass

    # abstract method
    def add_to_model(self, model):
        pass


# abstract class for hidden layers
class HiddenLayer(Layer):
    REGULARIZER = {
        "L1": regularizers.l1(0.01),
        "L2": regularizers.l2(0.01),
        "None": None
    }  # possible regularizers
    PADDING = {
        True: "same",
        False: "valid"
    }  # padding options

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # delete layer from UI
    def delete_layer(self):
        layer = self.get_main_window().ui.layout_create_layers
        indx = layer.indexOf(self)
        line = layer.takeAt(indx + 1).widget()

        line.deleteLater()
        self.deleteLater()


class InputLayer(Layer):
    def __init__(self, *args, **kwargs):
        super().__init__(Ui_InputLayer(), *args, **kwargs)

        self.input_count = 1
        self.spin_boxes = [self.ui.spin_first_dimention]

    # add dimension to input
    def add_input(self):
        label = QLabel(f"{self.input_count + 1} dimension", self)
        spin = QSpinBox(self)
        spin.setMinimum(1)
        spin.setMaximum(10000)

        self.ui.layout_inputs.insertRow(self.input_count, label, spin)

        self.input_count += 1
        self.spin_boxes.append(spin)

    # remove dimension to input
    def delete_input(self):
        if self.input_count == 1:
            return
        self.ui.layout_inputs.removeRow(self.input_count - 1)
        self.input_count -= 1
        self.spin_boxes.pop()

    def add_to_model(self, model):
        dims = tuple(spin.value() for spin in self.spin_boxes)
        print(dims)
        model.add(Input(shape=dims))


class OutputLayer(HiddenLayer):
    OPTIMIZER = {
        "Adam": "adam",
    }  # possible optimizer options
    LOSS_FUNCTION = {
        "Categorical crossentropy": "categorical_crossentropy",
        "MSE": "mse"
    }  # possible loss function options
    METRICS = ["accuracy", AUC()]  # measured metrics

    def __init__(self, *args, **kwargs):
        super().__init__(Ui_OutputLayer(), *args, **kwargs)
        # set loss options
        self.ui.combo_loss.clear()
        self.ui.combo_loss.addItems(self.LOSS_FUNCTION.keys())
        # set optimizer options
        self.ui.combo_optimizer.clear()
        self.ui.combo_optimizer.addItems(self.OPTIMIZER.keys())

    def add_to_model(self, model):
        neurons = self.ui.spin_neurons.value()
        activation = self.ACTIVATION[self.ui.combo_activation.currentText()]
        optimizer = self.OPTIMIZER[self.ui.combo_optimizer.currentText()]
        loss = self.LOSS_FUNCTION[self.ui.combo_loss.currentText()]

        model.add(Flatten())  # flatten input so it fits
        model.add(Dense(neurons, activation=activation))
        model.compile(optimizer=optimizer,
                      loss=loss,
                      metrics=self.METRICS)


class DenseLayer(HiddenLayer):
    def __init__(self, *args, **kwargs):
        super().__init__(Ui_DenseLayer(), *args, **kwargs)

    def add_to_model(self, model):
        neurons = self.ui.spin_neurons.value()
        activation = self.ACTIVATION[self.ui.combo_activation.currentText()]
        regularizer = self.REGULARIZER[self.ui.combo_regularizer.currentText()]

        if self.ui.cbx_flatten.isChecked():
            model.add(Flatten())
        model.add(Dense(neurons, activation=activation, kernel_regularizer=regularizer))


class LSTMLayer(HiddenLayer):
    def __init__(self, *args, **kwargs):
        super().__init__(Ui_LSTMLayer(), *args, **kwargs)

    def add_to_model(self, model):
        units = self.ui.spin_units.value()
        rec_activation = self.ACTIVATION[self.ui.combo_recurrent_activation.currentText()]
        activation = self.ACTIVATION[self.ui.combo_activation.currentText()]
        regularizer = self.REGULARIZER[self.ui.combo_regularizer.currentText()]
        return_sequences = self.ui.cbx_return_sequences.isChecked()

        model.add(
            LSTM(units,
                 recurrent_activation=rec_activation,
                 activation=activation,
                 kernel_regularizer=regularizer,
                 return_sequences=return_sequences))


class Conv2DLayer(HiddenLayer):
    def __init__(self, *args, **kwargs):
        super().__init__(Ui_Conv2DLayer(), *args, **kwargs)

    def add_to_model(self, model):
        filters = self.ui.spin_filters.value()
        kernel = self.ui.spin_kernel.value()
        strides = self.ui.spin_strides.value()
        padding = self.PADDING[self.ui.cbx_same_padding.isChecked()]
        activation = self.ACTIVATION[self.ui.combo_activation.currentText()]
        regularizer = self.REGULARIZER[self.ui.combo_regularizer.currentText()]

        model.add(Conv2D(filters, kernel, strides, padding, activation=activation, kernel_regularizer=regularizer))


class MaxpoolingLayer(HiddenLayer):
    def __init__(self, *args, **kwargs):
        super().__init__(Ui_MaxpoolingLayer(), *args, **kwargs)

    def add_to_model(self, model):
        pool = self.ui.spin_pool.value()
        strides = self.ui.spin_strides.value()
        padding = self.PADDING[self.ui.cbx_same_padding.isChecked()]

        model.add(MaxPool2D(pool, strides, padding))


class DropoutLayer(HiddenLayer):
    def __init__(self, *args, **kwargs):
        super().__init__(Ui_DropoutLayer(), *args, **kwargs)

    def add_to_model(self, model):
        rate = self.ui.spin_dropout_rate.value()

        model.add(Dropout(rate))
