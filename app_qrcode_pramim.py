import sys
import qrcode
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PIL import Image
import io

class QRCodeGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.label = QLabel("Digite o conteúdo do QR Code:")
        self.layout.addWidget(self.label)

        self.qr_input = QLineEdit(self)
        self.layout.addWidget(self.qr_input)

        self.generate_button = QPushButton("Gerar QR Code", self)
        self.generate_button.clicked.connect(self.generate_qr_code)
        self.layout.addWidget(self.generate_button)

        self.qr_label = QLabel(self)
        self.layout.addWidget(self.qr_label)

        self.save_button = QPushButton("Salvar QR Code", self)
        self.save_button.clicked.connect(self.save_qr_code)
        self.layout.addWidget(self.save_button)
        self.save_button.setEnabled(False)  # Desabilitar botão de salvar até o QR Code ser gerado

        self.setLayout(self.layout)
        self.setWindowTitle("Gerador de QR Code")
        self.show()

    def generate_qr_code(self):
        data = self.qr_input.text()
        if data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            self.pil_image = img.convert('RGB')
            self.pil_image = self.pil_image.resize((500, 500)) 

            # Converter a imagem PIL para QImage
            buffer = io.BytesIO()
            self.pil_image.save(buffer, format="PNG")
            buffer.seek(0)
            image = QImage()
            image.loadFromData(buffer.getvalue())

            self.qpixmap = QPixmap.fromImage(image)
            self.qr_label.setPixmap(self.qpixmap)
            self.save_button.setEnabled(True)

    def save_qr_code(self):
        if self.qpixmap:
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(self, "Salvar QR Code", "", "PNG Files (*.png);;All Files (*)", options=options)
            if file_path:
                self.pil_image.save(file_path, "PNG")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRCodeGenerator()
    sys.exit(app.exec_())
