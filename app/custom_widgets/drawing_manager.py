from PySide6.QtCore import Qt
from PySide6.QtGui import QImage
from PySide6.QtWidgets import QFileDialog

from app.custom_widgets.custom_widget import CustomWidget
from ui.drawing_manager import Ui_DrawingManager


# manage buttons and DrawPixels class
class DrawingManager(CustomWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(Ui_DrawingManager(), *args, **kwargs)

    # save image to file
    def save(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                              "PNG Files (*.png);;JPEG Files (*.jpg *.jpeg)")
        if path:
            if self.ui.draw_pixels.get_image().save(path):
                self.get_main_window().statusBar().showMessage("Image saved", self.STATUS_BAR_MSG)
            else:
                self.get_main_window().statusBar().showMessage("Error", self.STATUS_BAR_MSG)

    # load image from file
    def load(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
                                              "PNG Files (*.png);;JPEG Files (*.jpg *.jpeg)")
        if path:
            image = QImage()
            if image.load(path):
                self.ui.draw_pixels.set_image(image)
                self.get_main_window().statusBar().showMessage("Image loaded", self.STATUS_BAR_MSG)
            else:
                self.get_main_window().statusBar().showMessage("Error", self.STATUS_BAR_MSG)

    # fill white
    def clear(self):
        self.ui.draw_pixels.clear_image()

    # fill black
    def fill(self):
        self.ui.draw_pixels.fill_image()

    # get current image
    def get_image(self):
        return self.ui.draw_pixels.get_image().scaled(self.ui.spin_width.value(), self.ui.spin_height.value(),
                                                      mode=Qt.SmoothTransformation)
