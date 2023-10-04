import playsound
from gtts import gTTS
import speech_recognition as sr #установила еще PyAudio

#from googletrans import Translator # взяла гугловский переводчик upd: он вообще не хочет работать... почитала об ошибке на стэке - перепробовала все, но не вышло. так что взяла просто другую библиотеку
from deep_translator import GoogleTranslator # по идее тот же самый гугл
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *


class MyHelper(QMainWindow):
    def __init__(self):
        super().__init__()

        self.lang = 'en'  #будем с английским
        self.translator = GoogleTranslator()

        self.setWindowTitle('MyПомощник')
        self.resize(800, 700)
        self.setWindowIcon(QtGui.QIcon('pic.png'))#картинка работает только если папку открыть всю

        # окошки
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        # поле для ввода текста
        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)
        
        #кнопки
        self.translate_button = QPushButton('попереводим!')
        self.translate_button.clicked.connect(self.translate)

        self.text_to_speech_button = QPushButton('как читается то, что тут написано')
        self.text_to_speech_button.clicked.connect(self.text_to_speech)

        self.translate_and_pronounce_my_text_button = QPushButton('переведи и прочитай, пожалйста')
        self.translate_and_pronounce_my_text_button.clicked.connect(self.translate_and_pronounce_my_text)   

        self.pronunciation_training_button = QPushButton('хочу поработать над произношением!')
        self.pronunciation_training_button.clicked.connect(self.pronunciation_training)

        self.layout.addWidget(self.translate_button)
        self.translate_button.setFont(QFont("Times", 10))
        self.layout.addWidget(self.text_to_speech_button)
        self.text_to_speech_button.setFont(QFont("Times", 10))
        self.layout.addWidget(self.translate_and_pronounce_my_text_button)
        self.translate_and_pronounce_my_text_button.setFont(QFont("Times", 10))
        self.layout.addWidget(self.pronunciation_training_button)
        self.pronunciation_training_button.setFont(QFont("Times", 10))
        
        self.table = QtWidgets.QLabel('', self)
        self.table.setFixedSize(800, 100)
        self.layout.addWidget(self.table)
        self.table.setFont(QFont("Times", 20))

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget) 


    def set_language(self, lang):
        self.lang = lang

    def translate(self, text):# должен уметь переводить - работает
        self.table.clear()#чтобы можно было use и дальше
        text = self.text_edit.toPlainText()
        self.table.setText(GoogleTranslator(source='auto', target=self.lang).translate(text))
        return GoogleTranslator(source='auto', target=self.lang).translate(text)
        #ну допустим переводит

    def text_to_speech(self, text):#2 должен уметь озвучивать написанное - работает #!не переводит, просто читает 
        self.table.clear()
        text = self.text_edit.toPlainText()
        tts = gTTS(text, lang=self.lang)
        tts.save('output.mp3')
        playsound.playsound('output.mp3')

    def translate_and_pronounce_my_text(self): #это уже переводит и читает - тоже работает
        self.table.clear()
        tts = gTTS(self.translate(self.text_edit.toPlainText()), lang=self.lang)
        tts.save('output.mp3')
        playsound.playsound('output.mp3')

    def pronunciation_training(self):#4 должен уметь тренировать произношение - это работает
        rec = sr.Recognizer()
        with sr.Microphone() as source:
            self.table.setText('произнесите текст...')
            audio = rec.listen(source)
            self.table.setText('я распознал вот это:' + ' ' + rec.recognize_google(audio, language=self.lang))
            if self.text_edit.toPlainText() == rec.recognize_google(audio, language=self.lang):
                self.table.setText('отлично! у вас неплохо получается ')
            else:
                self.table.setText('стоит еще поработать над произношением! вы произнесли' + ' ' +  rec.recognize_google(audio, language=self.lang) + ' ' +  'вместо {self.text_edit.toPlainText()}')
                    #что-то не получилось с f-строками





if __name__ == "__main__":
    app = QApplication(sys.argv)
    helper = MyHelper()
    helper.show()
    sys.exit(app.exec_())