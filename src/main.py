import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
from main_ui import Ui_MainWindow
from deep_translator import GoogleTranslator


class TranslatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.language_map = {
            "English": "en",
            "French": "fr",
            "Spanish": "es",
            "German": "de",
            "Hindi": "hi",
            "Arabic": "ar",
            "Chinese (Simplified)": "zh-CN",
            "Chinese (Traditional)": "zh-TW",
            "Japanese": "ja",
            "Korean": "ko",
            "Russian": "ru",
            "Portuguese": "pt",
            "Italian": "it",
            "Dutch": "nl",
            "Turkish": "tr",
            "Polish": "pl",
            "Swedish": "sv",
            "Greek": "el",
            "Hebrew": "he",
            "Vietnamese": "vi",
            "Indonesian": "id",
            "Thai": "th",
            "Bengali": "bn",
            "Tamil": "ta",
            "Telugu": "te",
            "Urdu": "ur",
            "Ukrainian": "uk",
            "Romanian": "ro",
            "Czech": "cs",
            "Hungarian": "hu",
            "Finnish": "fi",
            "Malay": "ms",
            "Slovak": "sk",
            "Bulgarian": "bg",
            "Croatian": "hr",
            "Danish": "da",
            "Norwegian": "no",
            "Serbian": "sr",
            "Filipino": "tl",
            "Persian (Farsi)": "fa"
        }

        self.rtl_languages = {"ar", "he", "fa", "ur"}

        self.ui.language_combo_box.addItems(self.language_map.keys())
        self.ui.translate_button.clicked.connect(self.translate)

        shortcut = QShortcut(QKeySequence("Ctrl+Return"), self.ui.input_text_edit)
        shortcut.activated.connect(self.translate)

        self.ui.attach_file_button.clicked.connect(self.attach_file)

    def attach_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;Word Documents (*.docx);;PDF Files (*.pdf);;All Files (*)")
        if file_path:
            try:
                with open (file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.ui.input_text_edit.setPlainText(content)
            except Exception as e:
                print(f"error reading file: {e}")

    def translate(self):
        text = self.ui.input_text_edit.toPlainText()
        if not text.strip():
            self.ui.output_text_edit.clear()
            return

        language = self.ui.language_combo_box.currentText()
        target_code = self.language_map[language]

        translated = GoogleTranslator(source='auto', target=target_code).translate(text)

        if target_code in self.rtl_languages:
            self.ui.output_text_edit.setLayoutDirection(Qt.RightToLeft)
        else:
            self.ui.output_text_edit.setLayoutDirection(Qt.LeftToRight)

        self.ui.output_text_edit.setPlainText(translated)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TranslatorApp()
    window.show()
    sys.exit(app.exec_())