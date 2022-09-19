import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QPalette, QColor


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Виселица")
        self.resize(440, 730)
        self.setFixedSize(self.size())

        self.greeting = QLabel(
            "          Добро пожаловать в игру 'Виселица'\n       Вам будет представлено слово, первая\nи "
            "последняя буквы которого будут отображены.\n      Необходимо отгадать оставшиеся буквы.\n"
            "                                  Удачи!",
            self)
        self.greeting.move(94, 40)

        self.condition = QLabel("Выберите тему и сложность", self)
        self.condition.move(143, 150)

        self.theme = QPushButton("Тема", self)
        self.theme.setStyleSheet('QPushButton {background-color: #F5F5F5}')
        self.theme.move(50, 180)
        self.theme.clicked.connect(self.evt_theme_clicked)

        self.plus_pic = QLabel(self)
        self.plus_pic.move(132, 185)
        self.plus_pic.resize(15, 15)

        self.plus_pic_pic = QPixmap("hangmen/plus.png")
        self.plus_pic.setPixmap(self.plus_pic_pic)

        self.complexity = QPushButton("Сложность", self)
        self.complexity.setStyleSheet('QPushButton {background-color: #F5F5F5}')
        self.complexity.move(155, 180)

        self.complexity.clicked.connect(self.evt_complexity_clicked)

        self.strelka_pic = QLabel(self)
        self.strelka_pic.move(235, 172)
        self.strelka_pic.resize(40, 40)

        self.strelka_pic_pic = QPixmap("hangmen/strelka.png")

        self.strelka_pic.setPixmap(self.strelka_pic_pic)

        self.slovo_choice = QPushButton("Сгенерировать слово", self)
        self.slovo_choice.setStyleSheet('QPushButton {background-color: #F5F5F5}')
        self.slovo_choice.move(280, 180)
        self.slovo_choice.clicked.connect(self.evt_slovo_choice_clicked)

        self.start = QPushButton("Начать игру!", self)
        self.start.setStyleSheet('QPushButton {background-color: #FFF0F5}')
        self.start.move(165, 230)
        self.start.resize(100, 40)
        self.start.clicked.connect(self.evt_start_clicked)

        self.chosen_theme, self.chosen_complexity = "", ""

        self.chosen_theme2, self.chosen_complexity2 = "", ""

        self.word = ""

        self.wrong_choices, self.wrong_choices_all = 0, 0

        self.second_letter_check = 0  # верно ли введена вторая буква
        self.third_letter_check = 0  # верно ли введена третья буква
        self.fourth_letter_check = 0  # верно ли введена четвертая буква
        self.choose_word_check = 0  # счетчик верно введенных букв

        self.hgm_pic = QLabel(self)
        self.hgm_pic.move(90, 350)
        self.hgm_pic.resize(260, 240)

        self.hgm0 = QPixmap("hangmen/pic0.png")
        self.hgm1 = QPixmap("hangmen/pic1.png")
        self.hgm2 = QPixmap("hangmen/pic2.png")
        self.hgm3 = QPixmap("hangmen/pic3.PNG")
        self.hgm4 = QPixmap("hangmen/pic4.PNG")
        self.hgm5 = QPixmap("hangmen/pic5.PNG")

    def evt_start_clicked(self):
        if len(self.word) == 3:
            self.evt_start_clicked_add()
            self.choose_word1()
        elif len(self.word) == 4:
            self.evt_start_clicked_add()
            self.choose_word2()
        elif len(self.word) == 5:
            self.evt_start_clicked_add()
            self.choose_word3()
        elif self.word == "":
            QMessageBox.critical(self, "Внимание", "Заполните необходимую информацию!")

    def evt_start_clicked_add(self):
        self.theme.setEnabled(False)
        self.complexity.setEnabled(False)
        self.slovo_choice.setEnabled(False)
        self.start.setEnabled(False)

        self.hgm_pic.setPixmap(self.hgm0)
        self.hgm_pic.show()

    def evt_theme_clicked(self):
        themes = ["Животные", "Еда", "Дом", "Тело"]

        self.chosen_theme, was_chosen1 = QInputDialog.getItem(self, "Темы", "Выберите интересующую вас тему", themes,
                                                              editable=False)
        if was_chosen1:
            QMessageBox.information(self, "Тема", "Вы выбрали тему " + "'" + self.chosen_theme + "'")
            self.theme.setText(self.chosen_theme)
            self.chosen_theme2 = self.chosen_theme
        else:
            QMessageBox.critical(self, "Отменено", "Вы отказались выбирать тему")

    def evt_complexity_clicked(self):
        complexities = ["Легко", "Средне", "Сложно"]
        self.chosen_complexity, was_chosen2 = QInputDialog.getItem(self, "Сложность", "Выберите сложность слов",
                                                                   complexities, editable=False)
        if was_chosen2:
            QMessageBox.information(self, "Сложность", "Вы выбрали сложность " + "'" + self.chosen_complexity + "'")
            self.complexity.setText(self.chosen_complexity)
            self.chosen_complexity2 = self.chosen_complexity
        else:
            QMessageBox.critical(self, "Отменено", "Вы отказались выбирать сложность")

    def evt_slovo_choice_clicked(self):
        if self.chosen_theme2 == "Животные" and self.chosen_complexity2 == "Легко":
            self.chosen_theme2 = ["вол", "бык", "лев", "лис"]
        elif self.chosen_theme2 == "Животные" and self.chosen_complexity2 == "Средне":
            self.chosen_theme2 = ["лось", "морж", "бобр", "рысь", "барс", "лань", "лама"]
        else:
            if self.chosen_theme2 == "Животные" and self.chosen_complexity2 == "Сложно":
                self.chosen_theme2 = ["белка", "крыса", "ягуар", "хомяк", "лемур", "коала"]

        if self.chosen_theme2 == "Еда" and self.chosen_complexity2 == "Легко":
            self.chosen_theme2 = ["сок", "чай", "лук", "киш", "соя", "суп", "уха"]
        elif self.chosen_theme2 == "Еда" and self.chosen_complexity2 == "Средне":
            self.chosen_theme2 = ["торт", "кофе", "борщ", "морс"]
        else:
            if self.chosen_theme2 == "Еда" and self.chosen_complexity2 == "Сложно":
                self.chosen_theme2 = ["кефир", "пицца", "салат", "чипсы", "батат", "кимчи", "хумус"]

        if self.chosen_theme2 == "Дом" and self.chosen_complexity2 == "Легко":
            self.chosen_theme2 = ["дом", "газ", "пол"]
        elif self.chosen_theme2 == "Дом" and self.chosen_complexity2 == "Средне":
            self.chosen_theme2 = ["свет", "окно", "софа", "стул", "стол"]
        else:
            if self.chosen_theme2 == "Дом" and self.chosen_complexity2 == "Сложно":
                self.chosen_theme2 = ["дверь", "диван", "ковер"]

        if self.chosen_theme2 == "Тело" and self.chosen_complexity2 == "Легко":
            self.chosen_theme2 = ["ухо", "нос", "рот"]
        elif self.chosen_theme2 == "Тело" and self.chosen_complexity2 == "Средне":
            self.chosen_theme2 = ["язык", "нога", "рука", "глаз", "кожа"]
        else:
            if self.chosen_theme2 == "Тело" and self.chosen_complexity2 == "Сложно":
                self.chosen_theme2 = ["живот", "стопа", "палец", "скулы"]

        if self.chosen_theme2 != "" and self.chosen_complexity2 != "":
            self.word = random.choice(self.chosen_theme2)
            if len(self.word) == 3:
                self.wrong_choices_all = 1
            elif len(self.word) == 4:
                self.wrong_choices_all = 2
            elif len(self.word) == 5:
                self.wrong_choices_all = 3
        elif self.chosen_theme2 == "" and self.chosen_complexity2 != "":
            QMessageBox.critical(self, "Внимание", "Вы не выбрали тему!")
        elif self.chosen_complexity2 == "" and self.chosen_theme2 != "":
            QMessageBox.critical(self, "Внимание", "Вы не указали сложность!")
        elif self.chosen_complexity2 == "" and self.chosen_theme2 == "":
            QMessageBox.critical(self, "Внимание", "Вы не выбрали тему и не указали сложность!")

    def choose_word1(self):
        self.note = QLabel("Поскольку вы выбрали легкие слова, допускается только одна ошибка.", self)
        self.note.move(35, 310)
        self.note.show()

        self.letter_first = QLabel(self.word[0].upper(), self)
        self.letter_first.move(182, 620)
        self.letter_first.show()

        self.letter_2 = QLineEdit(self)
        self.letter_2.setMaxLength(1)
        self.letter_2.move(212, 620)
        self.letter_2.resize(15, 15)
        self.letter_2.show()

        self.letter_2.editingFinished.connect(self.evt_letter_2_clicked)

        self.letter_last = QLabel(self.word[-1].upper(), self)
        self.letter_last.move(252, 620)
        self.letter_last.show()

        self.enter_letter = QPushButton("Ввести букву", self)
        self.enter_letter.setStyleSheet('QPushButton {background-color: #FFF5EE}')
        self.enter_letter.move(184, 670)
        self.enter_letter.show()

    def choose_word2(self):
        self.note = QLabel("Поскольку вы выбрали средние слова, допускаются только две ошибки.", self)
        self.note.move(35, 310)
        self.note.show()

        self.letter_first = QLabel(self.word[0].upper(), self)
        self.letter_first.move(190, 600)
        self.letter_first.show()

        self.letter_2 = QLineEdit(self)
        self.letter_2.setMaxLength(1)
        self.letter_2.move(205, 600)
        self.letter_2.resize(15, 15)
        self.letter_2.show()
        self.letter_2.editingFinished.connect(self.evt_letter_2_clicked)

        self.letter_3 = QLineEdit(self)
        self.letter_3.setMaxLength(1)
        self.letter_3.move(227, 600)
        self.letter_3.resize(15, 15)
        self.letter_3.show()
        self.letter_3.editingFinished.connect(self.evt_letter_3_clicked)

        self.letter_last = QLabel(self.word[-1].upper(), self)
        self.letter_last.move(250, 600)
        self.letter_last.show()

        self.enter_letter = QPushButton("Ввести букву", self)
        self.enter_letter.setStyleSheet('QPushButton {background-color: #FFF5EE}')
        self.enter_letter.move(186, 650)
        self.enter_letter.show()

    def choose_word3(self):
        self.note = QLabel("Поскольку вы выбрали сложные слова, допускаются три ошибки.", self)
        self.note.move(50, 310)
        self.note.show()

        self.letter_first = QLabel(self.word[0].upper(), self)
        self.letter_first.move(184, 600)
        self.letter_first.show()

        self.letter_2 = QLineEdit(self)
        self.letter_2.setMaxLength(1)
        self.letter_2.move(195, 600)
        self.letter_2.resize(15, 15)
        self.letter_2.show()
        self.letter_2.editingFinished.connect(self.evt_letter_2_clicked)

        self.letter_3 = QLineEdit(self)
        self.letter_3.setMaxLength(1)
        self.letter_3.move(213, 600)
        self.letter_3.resize(15, 15)
        self.letter_3.show()
        self.letter_3.editingFinished.connect(self.evt_letter_3_clicked)

        self.letter_4 = QLineEdit(self)
        self.letter_4.setMaxLength(1)
        self.letter_4.move(231, 600)
        self.letter_4.resize(15, 15)
        self.letter_4.show()
        self.letter_4.editingFinished.connect(self.evt_letter_4_clicked)

        self.letter_last = QLabel(self.word[-1].upper(), self)
        self.letter_last.move(250, 600)
        self.letter_last.show()

        self.enter_letter = QPushButton("Ввести букву", self)
        self.enter_letter.setStyleSheet('QPushButton {background-color: #FFF5EE}')
        self.enter_letter.move(183, 650)
        self.enter_letter.show()

    def evt_letter_2_clicked(self):
        letter_2_value = self.letter_2.text()
        if letter_2_value not in "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЫЭЮЯ":
            QMessageBox.information(self, "Внимание", "Доступно введение только букв из русского алфавита!")
            self.letter_2.clear()
        elif letter_2_value == self.word[1]:
            self.choose_word_check += 1
            self.second_letter_check = 1
            self.letter_2.clear()
            self.letter_2.hide()
            if len(self.word) == 4:
                self.letter__2 = QLabel(self.word[1].upper(), self)
                self.letter__2.move(210, 600)
                self.letter__2.show()
            if len(self.word) == 5:
                self.letter__2 = QLabel(self.word[1].upper(), self)
                self.letter__2.move(200, 600)
                self.letter__2.show()
            if len(self.word) == 3 and self.wrong_choices <= self.wrong_choices_all:
                self.letter__2 = QLabel(self.word[1].upper(), self)
                self.letter__2.move(218, 621)
                self.letter__2.show()
                self.you_won()
            elif len(self.word) == 4 and self.wrong_choices <= self.wrong_choices_all and self.choose_word_check == 2:
                self.you_won()
            elif len(self.word) == 5 and self.wrong_choices <= self.wrong_choices_all and self.choose_word_check == 3:
                self.you_won()
        else:
            if letter_2_value != "":
                if self.wrong_choices < self.wrong_choices_all:
                    self.wrong_choices += 1
                    self.letter_2.clear()
                    if self.wrong_choices == 1:
                        if len(self.word) == 3:
                            self.hgm_pic.setPixmap(self.hgm3)
                        elif len(self.word) == 4:
                            self.hgm_pic.setPixmap(self.hgm2)
                        elif len(self.word) == 5:
                            self.hgm_pic.setPixmap(self.hgm1)
                    elif self.wrong_choices == 2:
                        if len(self.word) == 4:
                            self.hgm_pic.setPixmap(self.hgm3)
                        elif len(self.word) == 5:
                            self.hgm_pic.setPixmap(self.hgm2)
                    elif self.wrong_choices == 3:
                        self.hgm_pic.setPixmap(self.hgm3)
                else:
                    self.letter_2.clear()
                    self.letter_2.setReadOnly(True)
                    if len(self.word) == 4:
                        if self.third_letter_check == 0:
                            self.letter_3.setReadOnly(True)
                    if len(self.word) == 5:
                        if self.third_letter_check == 0:
                            self.letter_3.setReadOnly(True)
                        if self.fourth_letter_check == 0:
                            self.letter_4.setReadOnly(True)
                    self.you_lost()

    def evt_letter_3_clicked(self):
        letter_3_value = self.letter_3.text()
        if letter_3_value not in "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЫЭЮЯ":
            QMessageBox.information(self, "Внимание", "Доступно введение только букв из русского алфавита!")
            self.letter_3.clear()
        elif letter_3_value == self.word[2]:
            self.letter_3.clear()
            self.letter_3.hide()
            self.choose_word_check += 1
            self.third_letter_check = 1
            if len(self.word) == 4:
                self.letter__3 = QLabel(self.word[2].upper(), self)
                self.letter__3.move(230, 600)
                self.letter__3.show()
            if len(self.word) == 5:
                self.letter__3 = QLabel(self.word[2].upper(), self)
                self.letter__3.move(214, 600)
                self.letter__3.show()
            if len(self.word) == 4 and self.wrong_choices <= self.wrong_choices_all and self.choose_word_check == 2:
                self.you_won()
            elif len(self.word) == 5 and self.wrong_choices <= self.wrong_choices_all and self.choose_word_check == 3:
                self.you_won()
        else:
            if letter_3_value != "":
                if self.wrong_choices < self.wrong_choices_all:
                    self.wrong_choices += 1
                    self.letter_3.clear()
                    if self.wrong_choices == 1:
                        if len(self.word) == 4:
                            self.hgm_pic.setPixmap(self.hgm2)
                        elif len(self.word) == 5:
                            self.hgm_pic.setPixmap(self.hgm1)
                    elif self.wrong_choices == 2:
                        if len(self.word) == 4:
                            self.hgm_pic.setPixmap(self.hgm3)
                        elif len(self.word) == 5:
                            self.hgm_pic.setPixmap(self.hgm2)
                    elif self.wrong_choices == 3:
                        self.hgm_pic.setPixmap(self.hgm3)
                else:
                    self.letter_3.clear()
                    self.letter_3.setReadOnly(True)
                    if len(self.word) == 4:
                        if self.second_letter_check == 0:
                            self.letter_2.setReadOnly(True)
                    if len(self.word) == 5:
                        if self.second_letter_check == 0:
                            self.letter_2.setReadOnly(True)
                        if self.fourth_letter_check == 0:
                            self.letter_4.setReadOnly(True)
                    self.you_lost()

    def evt_letter_4_clicked(self):
        letter_4_value = self.letter_4.text()
        if letter_4_value not in "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЫЭЮЯ":
            QMessageBox.information(self, "Внимание", "Доступно введение только букв из русского алфавита!")
            self.letter_4.clear()
        elif letter_4_value == self.word[3]:
            self.fourth_letter_check = 1
            self.letter_4.clear()
            self.letter_4.hide()
            self.letter__4 = QLabel(self.word[3].upper(), self)
            self.letter__4.move(230, 600)
            self.letter__4.show()
            self.letter_last.move(239, 600)
            self.choose_word_check += 1
            if self.wrong_choices <= self.wrong_choices_all and self.choose_word_check == 3:
                self.you_won()
        else:
            if letter_4_value != "":
                if self.wrong_choices < self.wrong_choices_all:
                    self.wrong_choices += 1
                    self.letter_4.clear()
                    if self.wrong_choices == 1:
                        self.hgm_pic.setPixmap(self.hgm1)
                    elif self.wrong_choices == 2:
                        self.hgm_pic.setPixmap(self.hgm2)
                    elif self.wrong_choices == 3:
                        self.hgm_pic.setPixmap(self.hgm3)
                else:
                    self.letter_4.clear()
                    self.letter_4.setReadOnly(True)
                    if self.second_letter_check == 0:
                        self.letter_2.setReadOnly(True)
                    if self.third_letter_check == 0:
                        self.letter_3.setReadOnly(True)
                    self.you_lost()

    def you_won(self):
        self.note.setText("ВЫ ВЫИГРАЛИ!")
        self.note.move(185, 310)
        self.hgm_pic.setPixmap(self.hgm5)
        self.start_again_btn()

    def you_lost(self):
        self.note.setText("ВЫ ПРОИГРАЛИ!")
        self.note.move(185, 310)
        self.hgm_pic.setPixmap(self.hgm4)
        self.start_again_btn()

    def start_again_btn(self):
        self.enter_letter.hide()
        self.start_again = QPushButton("Начать снова", self)
        self.start_again.setStyleSheet('QPushButton {background-color: #FFEFD5}')
        self.start_again.move(184, 670)
        self.start_again.show()
        self.start_again.clicked.connect(self.start_again_btn_clicked)

    def start_again_btn_clicked(self):
        self.start_again.hide()
        self.letter_first.hide()
        self.letter_last.hide()
        if len(self.word) == 3:
            if self.second_letter_check == 0:
                self.letter_2.hide()
        if len(self.word) == 4:
            if self.second_letter_check == 0:
                self.letter_2.hide()
            if self.third_letter_check == 0:
                self.letter_3.hide()
        if len(self.word) == 5:
            if self.second_letter_check == 0:
                self.letter_2.hide()
            if self.third_letter_check == 0:
                self.letter_3.hide()
            if self.fourth_letter_check == 0:
                self.letter_4.hide()
        self.additional_letters()
        self.second_letter_check = 0
        self.third_letter_check = 0
        self.fourth_letter_check = 0
        self.theme.setEnabled(True)
        self.complexity.setEnabled(True)
        self.slovo_choice.setEnabled(True)
        self.start.setEnabled(True)
        self.hgm_pic.hide()
        self.wrong_choices, self.wrong_choices_all = 0, 0
        self.choose_word_check = 0
        self.note.hide()
        self.chosen_theme2, self.chosen_complexity2 = "", ""
        self.theme.setText("Тема")
        self.complexity.setText("Сложность")
        self.word = ""

    def additional_letters(self):
        if self.second_letter_check == 1:
            self.letter__2.hide()
        if self.third_letter_check == 1:
            self.letter__3.hide()
        if self.fourth_letter_check == 1:
            self.letter__4.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    pal1 = dlgMain.palette()
    pal1.setColor(QPalette.Normal, QPalette.Window, QColor("#E6E6FA"))
    dlgMain.setPalette(pal1)
    dlgMain.show()
    sys.exit(app.exec_())
