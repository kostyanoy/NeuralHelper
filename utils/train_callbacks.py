from PySide6.QtWidgets import QMainWindow
from keras.callbacks import Callback


# show progress in status bar
class StatusBarCallback(Callback):
    def __init__(self, main_window: QMainWindow):
        super().__init__()
        self.main_window = main_window

    # def on_batch_end(self, batch, logs=None):
    #     self.main_window.statusBar().showMessage(f"Batch: {batch + 1}/{self.params['steps']}")

    # call when epoch ended to show the progress
    def on_epoch_end(self, epoch, logs=None):
        self.main_window.statusBar().showMessage(f"Epoch: {epoch + 1}/{self.params['epochs']}")
