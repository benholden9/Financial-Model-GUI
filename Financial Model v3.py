import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
        QMetaObject, QObject, QPoint, QRect,
        QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
        QFont, QFontDatabase, QGradient, QIcon,
        QImage, QKeySequence, QLinearGradient, QPainter,
        QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGraphicsView,
        QHBoxLayout, QHeaderView, QLabel, QLineEdit,
        QMainWindow, QPushButton, QScrollArea, QSizePolicy,
        QStatusBar, QTabWidget, QTableView, QTableWidget,
        QTableWidgetItem, QVBoxLayout, QWidget)

class AppDemo(QMainWindow):
    def __init__(self):
        super(AppDemo, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        ui_file = QFile('GUI v2.ui')
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open '{ui_file.fileName()}': {ui_file.errorString()}")
            sys.exit(-1)
        self.ui = loader.load(ui_file, self)
        ui_file.close()
        if not self.ui:
            print("Cannot load UI")
            sys.exit(-1)
        print("UI loaded successfully")
        button = self.ui.findChild(QPushButton, 'br_submit')
        if button:
            print(button.objectName())
        else:
            print("PushButton not found.")


        self.setCentralWidget(self.ui)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppDemo()
    window.show()
    sys.exit(app.exec())
