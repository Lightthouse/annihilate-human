
from ready import QtWidgets, Ui_MainWindow
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setup_ui(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
