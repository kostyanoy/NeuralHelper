import os

import numpy as np
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPixmap, QImage, QKeyEvent
from PySide6.QtWidgets import QFileDialog

from app.custom_widgets.custom_widget import CustomWidget
from ui.dataset_manager import Ui_DatasetManager
from utils.dataset import Dataset


# manage custom image datasets (and flat)
class DatasetManager(CustomWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(Ui_DatasetManager(), *args, **kwargs)
        self.cur_pos = None  # top-left corner of window
        self.cur_pixmap = None  # current image
        self.cur_zoomed_area = None  # current part of image
        self.dataset = None  # current dataset
        self.is_zoomed = False  # current zoom status
        self.same_size = self.ui.cbx_same_size.isChecked()  # if the height must be equal to width
        self.h = self.ui.spin_height.value()  # current height of window
        self.w = self.ui.spin_width.value()  # current width of window
        self.s = self.ui.spin_speed.value()  # current speed of moving window

        self.set_current_position(0, 0)

        self.ui.lbl_image.clicked.connect(self.set_current_position)

    # load image from file
    def load_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.jpeg)")
        if not path:
            return
        if self.is_zoomed:
            self.zoom()
        image = QImage(path).convertToFormat(QImage.Format_Grayscale8)
        self.image = image
        self.cur_pixmap = QPixmap.fromImage(image)
        self.ui.lbl_image.set_image(image)
        self.ui.spin_height.setMaximum(self.cur_pixmap.height())
        self.ui.spin_width.setMaximum(self.cur_pixmap.width())
        self.set_current_position(0, 0)
        self.resize_image()

    # set height of window
    def set_height(self, value):
        self.h = value

        if self.same_size:
            self.ui.spin_width.setValue(value)

        self.update_zoomed_area()

    # set width of window
    def set_width(self, value):
        self.w = value

        self.update_zoomed_area()

    # set speed of moving window
    def set_speed(self, value):
        self.s = value

    # set speed of moving window
    def set_same_size(self, value):
        self.same_size = bool(value)
        self.ui.spin_width.setEnabled(not value)
        self.ui.spin_width.setValue(self.h)

    # set amount of flat inputs
    def set_outputs(self):
        self.ui.fields_expected.set_inputs(self.ui.spin_ouputs.value())

    # set current window position
    def set_current_position(self, x, y):
        self.setFocus()  # make label-image process keyboard inputs

        if self.is_zoomed:
            return

        self.cur_pos = QPoint(x, y)
        self.check_position()

    # change current window position
    def move_current_position(self, x, y):
        if self.cur_zoomed_area is None:
            return

        self.cur_pos += QPoint(x, y) * self.s
        self.update_zoomed_area()

    # validate window position
    def check_position(self):
        x = self.cur_pos.x()
        y = self.cur_pos.y()
        if self.cur_pixmap is not None:
            x = max(0, min(x, self.cur_pixmap.width() - self.w))
            y = max(0, min(y, self.cur_pixmap.height() - self.w))

        self.cur_pos = QPoint(x, y)
        self.ui.lbl_position.setText(f"Current position: ({self.cur_pos.x()}, {self.cur_pos.y()})")

    # set zoomed status
    def zoom(self):
        if self.cur_pixmap is None:
            return

        self.setFocus()  # make label-image process keyboard inputs

        text = "Zoom in" if self.is_zoomed else "Zoom out"
        self.ui.btn_zoom.setText(text)

        self.is_zoomed = not self.is_zoomed
        self.update_zoomed_area()

    # change current zoomed area
    def update_zoomed_area(self):
        if self.cur_pixmap is None:
            return

        self.check_position()
        self.cur_zoomed_area = self.cur_pixmap.copy(self.cur_pos.x(), self.cur_pos.y(), self.w, self.h)

        self.resize_image()

    # fit sizes of app
    def resize_image(self):
        if self.cur_pixmap is None:
            return

        pixmap = self.cur_zoomed_area if self.is_zoomed else self.cur_pixmap

        scaled_pixmap = pixmap.scaled(
            self.ui.container.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
        )
        self.ui.lbl_image.setPixmap(scaled_pixmap)

    # process user resize action
    def resizeEvent(self, event):
        if self.cur_pixmap is not None:
            self.resize_image()

    # process user key press
    def keyPressEvent(self, event: QKeyEvent):
        if not self.is_zoomed:
            return

        key = event.key()

        if key == Qt.Key_Left:
            self.move_current_position(-1, 0)
        elif key == Qt.Key_Right:
            self.move_current_position(1, 0)
        elif key == Qt.Key_Up:
            self.move_current_position(0, -1)
        elif key == Qt.Key_Down:
            self.move_current_position(0, 1)
        elif key == Qt.Key_Enter or key == Qt.Key_Return:  # enter button is processing as return button
            if self.dataset is None:
                self.get_main_window().show_status("Choose dataset first")
                return

            x = self.get_image_sample()
            y = np.array(self.ui.fields_expected.get_inputs())

            self.dataset.add_sample(x, y)
            self.get_main_window().show_status(f"Added {self.dataset.get_count()} sample")
        else:
            super().keyPressEvent(event)

    # convert image to array
    def get_image_sample(self):
        image = self.cur_zoomed_area.toImage()

        # Convert QImage to NumPy array
        width = image.width()
        height = image.height()
        buffer = image.constBits()
        arr = np.frombuffer(buffer, dtype=np.uint8).reshape((height, width, 4))[:, :, 0]
        return np.array(arr)

    # create new dataset
    def create_dataset(self):
        self.dataset = Dataset()
        self.get_main_window().show_status("New dataset created")

    # choose dataset from directory
    def choose_dataset(self):
        path = QFileDialog.getExistingDirectory(self, "Choose directory of dataset")
        if not path:
            return
        self.dataset = Dataset.load_from_file(path)
        self.ui.btn_choose_dataset.setText(os.path.split(path)[1])

    # save dataset to directory
    def save_dataset(self):
        if self.dataset is None:
            self.get_main_window().show_status("Choose dataset first")
            return

        path = QFileDialog.getExistingDirectory(self, "Choose directory to save dataset")
        if not path:
            return

        self.dataset.save_to_file(path)
