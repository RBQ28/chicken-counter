import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from infer_yolo import run_yolo

class ChickenCounterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contador de Gallinas YOLO")
        self.setGeometry(100, 100, 800, 600)

        self.label = QLabel("Selecciona una imagen para contar gallinas", self)
        self.label.setAlignment(Qt.AlignCenter)

        self.img_label = QLabel(self)
        self.img_label.setAlignment(Qt.AlignCenter)
        self.img_label.setFixedSize(400, 400)

        self.result_label = QLabel("", self)
        self.result_label.setAlignment(Qt.AlignCenter)

        self.btn_select = QPushButton("Seleccionar Imagen", self)
        self.btn_select.clicked.connect(self.open_image)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.img_label)
        layout.addWidget(self.result_label)
        layout.addWidget(self.btn_select)
        self.setLayout(layout)

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecciona una imagen", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            pixmap = QPixmap(file_path)
            self.img_label.setPixmap(pixmap.scaled(self.img_label.size(), Qt.KeepAspectRatio))
            self.label.setText("Procesando...")
            QApplication.processEvents()

            count, out = run_yolo(file_path)
            self.result_label.setText(f"[YOLO] Gallinas detectadas: {count}")

            if out:
                out_pixmap = QPixmap(out)
                self.img_label.setPixmap(out_pixmap.scaled(self.img_label.size(), Qt.KeepAspectRatio))
            self.label.setText("Listo. Selecciona otra imagen si deseas.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChickenCounterApp()
    window.show()
    sys.exit(app.exec_())