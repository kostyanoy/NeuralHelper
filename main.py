import sys

from PySide6.QtWidgets import QApplication

from app.application import App


# main function to run project
def main():
    # Init application and run
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
