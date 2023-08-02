from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QImage, QPainter, QColor, QPen

from app.custom_widgets.custom_widget import CustomWidget


# allow draw on image and pixelate it
class DrawPixels(CustomWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(None, *args, **kwargs)
        self.h = 28  # height of image
        self.w = 28  # width of image
        self.thick = 20  # thickness of line
        self.image = QImage(self.parent().width(), self.parent().height(),
                            QImage.Format_RGB32)  # image to store the drawing
        self.image.fill(Qt.white)  # fill the image with a white background
        self.last_pos = QPoint()  # last recorded position of the cursor
        self.resize_image()

    # override of base method to redraw everything
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)  # draw the image on the widget

    # process user mouse click
    def mousePressEvent(self, event):
        if event.button() in [Qt.LeftButton, Qt.RightButton]:
            self.last_pos = event.position()  # update the last recorded position

    # process user mouse move
    def mouseMoveEvent(self, event):
        pen = QPen(Qt.black, self.thick, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        if event.buttons() & Qt.RightButton:
            pen.setColor(QColor("white"))

        if event.buttons() in [Qt.LeftButton, Qt.RightButton]:
            painter = QPainter(self.image)
            painter.setPen(pen)
            painter.drawLine(self.last_pos, event.position())  # Draw a line between the last and current positions
            self.last_pos = event.position()  # Update the last recorded position
            self.update()  # Trigger a repaint of the widget

    # process user mouse release
    def mouseReleaseEvent(self, event):
        if event.button() in [Qt.LeftButton, Qt.RightButton]:
            self.resize_image()

    # process user resize window
    def resizeEvent(self, event):
        self.resize_image()

    # resize image and pixelate
    def resize_image(self):
        scaled_image = self.image.scaled(self.w, self.h, mode=Qt.SmoothTransformation)
        self.image = scaled_image.scaled(self.parent().width(), self.parent().height())
        # grayscale_image = scaled_image.convertToFormat(QImage.Format_Grayscale8)
        self.update()
        # Print the pixel values of the grayscale image
        # for y in range(grayscale_image.height()):
        #     for x in range(grayscale_image.width()):
        #         pixel_value = QColor(grayscale_image.pixel(x, y)).value()
        #         print(pixel_value, end=' ')
        #     print()
        # Save the image or perform any other desired operations

    # set current image
    def set_image(self, image):
        self.image = image
        self.resize_image()

    # get current image (not scaled)
    def get_image(self):
        return self.image

    # fill white
    def clear_image(self):
        self.image.fill(Qt.white)
        self.resize_image()

    # fill black
    def fill_image(self):
        self.image.fill(Qt.black)
        self.resize_image()

    # set current height
    def set_height(self, value):
        self.h = value

    # set current width
    def set_width(self, value):
        self.w = value

    # set current thickness of line
    def set_thickness(self, value):
        self.thick = value
