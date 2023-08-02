from PySide6.QtWidgets import QScrollArea, QGridLayout, QLabel, QLineEdit, QDoubleSpinBox, QWidget


# create flat fields for inputs
class FieldsCreator(QScrollArea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWidgetResizable(True)

        # Create a widget to hold the content
        self.content_widget = QWidget()
        self.content_layout = QGridLayout(self.content_widget)

        # Set the content widget as the scroll area's widget
        self.setWidget(self.content_widget)

    # set and create amount of inputs with labels
    def set_inputs(self, amount):
        layout = self.content_layout

        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        for i in range(amount):
            label = QLabel(f"{i + 1})")
            line = QLineEdit()
            spin = QDoubleSpinBox()
            spin.setMinimum(-10000)
            spin.setMaximum(10000)

            layout.addWidget(label, i, 0)
            layout.addWidget(line, i, 1)
            layout.addWidget(spin, i, 2)

    # get user inputs in fields
    def get_inputs(self):
        x = []
        layout = self.content_layout
        for i in range(layout.rowCount()):
            widget_item = layout.itemAtPosition(i, 2)
            if widget_item is not None:
                widget = widget_item.widget()
                x.append(widget.value())

        return x
