from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog

class BackgroundRemover(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.label_input = QLabel("Seleccionar carpeta de entrada:")
        self.layout.addWidget(self.label_input)

        self.input_folder_button = QPushButton("Seleccionar")
        self.input_folder_button.clicked.connect(self.selectInputFolder)
        self.layout.addWidget(self.input_folder_button)

        self.label_output = QLabel("Seleccionar carpeta de salida:")
        self.layout.addWidget(self.label_output)

        self.output_folder_button = QPushButton("Seleccionar")
        self.output_folder_button.clicked.connect(self.selectOutputFolder)
        self.layout.addWidget(self.output_folder_button)

        self.process_button = QPushButton("Procesar Imágenes")
        self.process_button.clicked.connect(self.processImages)
        self.layout.addWidget(self.process_button)

        self.input_folder = ""
        self.output_folder = ""

    def selectInputFolder(self):
        self.input_folder = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta de entrada")
        self.label_input.setText(f"Carpeta de entrada seleccionada: {self.input_folder}")

    def selectOutputFolder(self):
        self.output_folder = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta de salida")
        self.label_output.setText(f"Carpeta de salida seleccionada: {self.output_folder}")

    def processImages(self):
        if not self.input_folder or not self.output_folder:
            return

        remover = BackgroundRemover(self.input_folder, self.output_folder)
        remover.process_images()
        self.label_input.setText("Seleccionar carpeta de entrada:")
        self.label_output.setText("Seleccionar carpeta de salida:")