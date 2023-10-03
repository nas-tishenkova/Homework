import sys
from PyQt5.QtWidgets import *
import spacy
nlp = spacy.load('ru_core_news_sm')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('морфопарсерчик')
        self.resize(800, 700)

        # окошки
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # поле для ввода текста
        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        # кнопка "parse"
        self.parse_button = QPushButton('попарсим!')
        self.parse_button.clicked.connect(self.parse_text)
        self.layout.addWidget(self.parse_button)

        # таблица для морфоразбора
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

    def parse_text(self):
        text = nlp(self.text_edit.toPlainText())

        self.table.clear()

        # установим ячейки
        self.table.setRowCount(len(text)+1)
        self.table.setColumnCount(4)

        # заполним табличку
        for token in text:
            self.table.setItem(0, 0, QTableWidgetItem('токен'))
            self.table.setItem(0, 1, QTableWidgetItem('лемма'))
            self.table.setItem(0, 2, QTableWidgetItem('часть речи'))
            self.table.setItem(0, 3, QTableWidgetItem('фичи'))
            self.table.setItem(token.i + 1, 0, QTableWidgetItem(token.text))
            self.table.setItem(token.i + 1, 1, QTableWidgetItem(token.lemma_))
            self.table.setItem(token.i + 1, 2, QTableWidgetItem(token.pos_))
            self.table.setItem(token.i + 1, 3, QTableWidgetItem(str(token.morph)))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())