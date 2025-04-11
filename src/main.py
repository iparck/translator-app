from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut, QFileDialog
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt, pyqtSignal

import sys, time
import threading
import warnings
import json
from main_ui import Ui_MainWindow

try:
    from deep_translator import GoogleTranslator
except ImportError:
    print("Install 'deep-translator' for translation purposes")
    time.sleep(3)
    sys.exit()
try: 
    import speech_recognition as sr
    SPEECH_RECOGNITION_AVAILABLE = True
except ImportError:
    print("Install 'speech_recognition' for speech-to-text.")
    SPEECH_RECOGNITION_AVAILABLE = False
try:
    import pyttsx3
    PYTTSX3_AVAILABLE = True
except ImportError:
    print("Install 'pyttsx3' for text-to-speech.")
    PYTTSX3_AVAILABLE = False
try:
    import fitz
except Exception as e:
    print("Install the PyMuPDF library of python to read pdfs")
try:
    from docx import Document
except Exception as e:
    print("Install the python_docx library of python to read docx")

warnings.filterwarnings("ignore", category=DeprecationWarning)

class TranslatorApp(QMainWindow):
    speech_result_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        try:
            with open("languages.json", "r", encoding="utf-8") as f:
                self.language_map = json.load(f)
        except Exception as e:
            print("Failed to load language map. Using default.")
            self.language_map = {
                "English": "en",
                "French": "fr",
                "Spanish": "es",
                "German": "de",
                "Arabic": "ar",
                "Chinese (Simplified)": "zh-CN",
                "Japanese": "ja",
                "Portuguese": "pt",
                "Russian": "ru",
                "Hindi": "hi"
            }

        self.rtl_languages = {"ar", "he", "fa", "ur"}

        self.ui.language_combo_box.addItems(self.language_map.keys())
        self.ui.translate_button.clicked.connect(self.translate)

        shortcut = QShortcut(QKeySequence("Ctrl+Return"), self.ui.input_text_edit)
        shortcut.activated.connect(self.translate)

        self.ui.attach_file_button.clicked.connect(self.attach_file)

        if SPEECH_RECOGNITION_AVAILABLE:
            self.recognizer = sr.Recognizer()
            self.speech_result_signal.connect(self.display_speech_result)
            self.ui.speech_text_button.clicked.connect(self.speech_to_text)

        if PYTTSX3_AVAILABLE:
            self.engine = pyttsx3.init()
            self.ui.text_speech_button.clicked.connect(self.text_to_speech)



    def attach_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if file_path:
            try:
                with open (file_path, 'rb') as file:
                    if file_path.endswith(".pdf"):
                        try:
                            content = ""
                            doc = fitz.open(file_path)
                            for page in doc:
                                content += page.get_text()
                            self.ui.input_text_edit.setPlainText(content)
                        except Exception as e:
                            print(f"Error: {e}")
                    elif file_path.endswith(".docx"):
                        try:
                            doc = Document(file_path)
                            full_text = []
                            for para in doc.paragraphs:
                                full_text.append(para.text)
                            content = '\n'.join(full_text)

                            self.ui.input_text_edit.setPlainText(content)
                        except Exception as e:
                            print(f"Error: {e}")
                    else:
                        try:
                            content = file.read().decode('utf-8', errors='ignore')
                            self.ui.input_text_edit.setPlainText(content)

                        except Exception as e:
                            print(f"Error reading file: {e}")
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
    
    def speech_to_text(self):
        if not SPEECH_RECOGNITION_AVAILABLE:
            print("Speech recognition is not available.")
            return

        def run_speech():
            try:
                with sr.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)
                    content = self.recognizer.recognize_google(audio)
                    self.speech_result_signal.emit(content)
            except Exception as e:
                print("Voice input error:", e)

        threading.Thread(target=run_speech, daemon=True).start()

    def display_speech_result(self, text):
        self.ui.input_text_edit.setPlainText(text)

    def text_to_speech(self):
        if not PYTTSX3_AVAILABLE:
            print("Text-to-speech is not available.")
            return

        text = self.ui.output_text_edit.toPlainText().strip()
        if text:
            self.engine.say(text)
            self.engine.runAndWait()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TranslatorApp()
    window.show()
    sys.exit(app.exec_())