import keras.models
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QHBoxLayout
from keras import Sequential

from app.custom_widgets.layers import Layer


# metrics of training models
class Metric:
    def __init__(self, name: str, history_name: str, cbx):
        self.name = name  # shown name
        self.history_name = history_name  # keras name
        self.checkbox = cbx  # ui checkbox

        self.values = []  # stored values

    # is checked by user
    def is_active(self):
        return self.checkbox.isChecked()

    # adds to its stored values
    def add_from_history(self, history):
        self.values += history.history[self.history_name]

    # clears stored values
    def clear(self):
        self.values.clear()

    # add values to canvas
    def show(self, canvas):
        canvas.axes.plot(range(1, len(self.values) + 1), self.values, label=self.name)


# manages model for user
class ModelManager(QThread):
    message = Signal(str)
    finished = Signal()

    def __init__(self, main_window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_active = False  # is training
        self.main_window = main_window
        self.metrics = [
            Metric("Train Accuracy", "accuracy", main_window.ui.output_layer.ui.cbx_train_accuracy),
            Metric("Validation Accuracy", "val_accuracy", main_window.ui.output_layer.ui.cbx_val_accuracy),
            Metric("Train Loss", "loss", main_window.ui.output_layer.ui.cbx_train_loss),
            Metric("Validation Loss", "val_loss", main_window.ui.output_layer.ui.cbx_val_loss),
            Metric("AUC", "auc", main_window.ui.output_layer.ui.cbx_train_auc),
            Metric("AUC", "val_auc", main_window.ui.output_layer.ui.cbx_val_auc)
        ]

        self.data_module = None  # where take data
        self.model = None  # current model

    # generates model from user interactions
    def generate_model(self) -> bool:
        layer: QHBoxLayout = self.main_window.ui.layout_create_layers
        model = Sequential()

        for i in range(layer.count()):
            widget = layer.itemAt(i).widget()
            if not isinstance(widget, Layer):
                continue

            widget.add_to_model(model)

        self.model = model

        print(self.model.summary())  # short description
        return True

    # set data module
    def set_data(self, data_module):
        self.data_module = data_module

    # start training
    def run(self):
        # clear metrics if not continuing training
        if not self.main_window.ui.cbx_train_continue.isChecked():
            for m in self.metrics:
                m.clear()

        # set up
        self.is_active = True
        x_train, y_train, x_test, y_test, x_val, y_val = self.data_module.load_data()

        if x_val is None:
            x_val, y_val = x_test, y_test

        epochs = self.main_window.ui.spin_train_epochs.value()

        for i in range(epochs):
            if not self.is_active:
                break

            # show history
            history = self.model.fit(x_train, y_train,
                                     batch_size=self.main_window.ui.spin_train_batch.value(),
                                     epochs=1,
                                     validation_data=(x_val, y_val))
            self.draw_metrics(history)
            self.message.emit(
                f"Epoch {i + 1} / {epochs}: Validation accuracy: {round(history.history['val_accuracy'][0], 4)}")

        self.finished.emit()

    # show chosen metrics on graph
    def draw_metrics(self, history):
        canvas = self.main_window.get_metrics_graph()
        canvas.axes.clear()
        for m in self.metrics:
            if not m.is_active():
                continue
            m.add_from_history(history)
            m.show(canvas)
        canvas.axes.legend()
        canvas.draw()

    # stop training
    def stop(self):
        self.is_active = False

    # is model generated
    def have_model(self) -> bool:
        return self.model is not None

    # get current mdoel
    def get_model(self) -> Sequential:
        return self.model

    # load model from file
    def load_model(self, path):
        self.model = keras.models.load_model(path)
        print(self.model.summary())

    # save model to file
    def save_model(self, path):
        self.model.save(path)

    # give sample to model
    def sample(self, x):
        return self.model.predict(x)
