import os
from datetime import datetime
from rembg import remove
import sys
from gui.window import BackgroundRemover

from PyQt6.QtWidgets import QApplication
class BackgroundRemoverApp():
    def __init__(self,input_folder,output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

    def process_images(self):
        today = datetime.now().strftime('%Y_%m_%d %H_%M_%S')
        processed_folder = os.path.join(self.output_folder, today)
        os.makedirs(processed_folder, exist_ok=True)

        for filename in os.listdir(self.input_folder):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(self.input_folder, filename)
                output_path = os.path.join(processed_folder, filename)
                self._remove_background(input_path, output_path)
                self._move_original(input_path, processed_folder)

    
    def _remove_background(self, input_p, output_p):
        with open(input_p, 'rb') as inp, open(output_p, 'wb') as out:
            background_output = remove(inp.read())
            out.write(background_output)

    def _move_original(self, input_p, destination_p):
        original_folder = os.path.join(destination_p, 'Originals')
        os.makedirs(original_folder, exist_ok=True)

        filename = os.path.basename(input_p)
        new_path = os.path.join(original_folder, filename)
        os.rename(input_p, new_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = BackgroundRemover()
    mainWindow.show()
    sys.exit(app.exec())