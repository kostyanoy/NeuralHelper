import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')


# show matplotlib graph as widget
class MatplotlibWidget(FigureCanvas):
    def __init__(self, parent=None, xlabel='x', ylabel='y', title='Title'):
        super().__init__(Figure())

        self.setParent(parent)
        self.axes = self.figure.add_subplot(111)

        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)
        self.axes.set_title(title)
