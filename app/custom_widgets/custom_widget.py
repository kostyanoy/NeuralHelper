from PySide6.QtCore import Signal
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QWidget, QMainWindow, QFrame, QLabel


# abstract widget class
class CustomWidget(QWidget):
    STATUS_BAR_MSG = 5000  # milli of showing message to user in status bar

    def __init__(self, ui, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if ui is not None:
            self.ui = ui  # ui of widget
            self.ui.setupUi(self)

    # get main window of app
    def get_main_window(self):
        # Navigate up the widget hierarchy until a QMainWindow instance is found
        parent_widget = self.parent()
        while parent_widget:
            if isinstance(parent_widget, QMainWindow):
                return parent_widget
            parent_widget = parent_widget.parent()

        return None

# vertical line
class VLine(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFrameShape(QFrame.Shape.VLine)
        self.setFrameShadow(QFrame.Shadow.Sunken)

# label that can react mouse clicks
class ClickableImageLabel(QLabel):
    clicked = Signal(int, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.image = None

    # set image to label
    def set_image(self, image: QImage):
        self.image = image
        self.setPixmap(QPixmap.fromImage(image))

    # get scale of image after fitting sizes
    def get_scale(self):
        return self.image.height() / self.pixmap().height()

    # process mouse click
    def mousePressEvent(self, event):
        if self.image is not None:
            position = event.pos() * self.get_scale()
            self.clicked.emit(position.x(), position.y())
