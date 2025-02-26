from PyQt5.QtWidgets import QApplication
app = QApplication([])
from main_window import *
from menu_window import *
import random
import time
class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right_ask = 0
    def right(self):
        self.count_ask += 1
        self.count_right_ask += 1
    def wrong(self):
        self.count_ask += 1

q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

radio_buttons = [r_btn1, r_btn2, r_btn3, r_btn4]
questions = [q1, q2, q3, q4]

def next_question():
    global current_question
    current_question = random.choice(questions)
    
    label_question.setText(current_question.question)
    label_correct.setText(current_question.answer)

    random.shuffle(radio_buttons)
    radio_buttons[0].setText(current_question.wrong_answer1)
    radio_buttons[1].setText(current_question.wrong_answer2)
    radio_buttons[2].setText(current_question.wrong_answer3)
    radio_buttons[3].setText(current_question.answer)

next_question()  

def check():
    radio_btn_group.setExclusive(False)
    for btn in radio_buttons:
        if btn.isChecked():
            if btn.text() == current_question.answer:
                label_correct_ans.setText('правильно')
                current_question.right()
                btn.setChecked(False)
            else:
                label_correct_ans.setText('неправильно')
                current_question.wrong()
                btn.setChecked(False)
            break
    radio_btn_group.setExclusive(True)

def click_ok():
    if btn_answer.text() == 'Відповісти':
        check()
        radio_group.hide()
        ans_group.show()
        btn_answer.setText('Далі')
    else:
        next_question()
        radio_group.show()
        ans_group.hide()
        btn_answer.setText('Відповісти')

btn_answer.clicked.connect(click_ok)

def rest():
    win_card.hide()
    minutes = box_sleep.value() #* 60
    time.sleep(minutes)
    win_card.show()
    
btn_sleep.clicked.connect(rest)

def menu_show():
    if current_question.count_ask == 0:
        c = 0
    else:
        c = current_question.count_right_ask / current_question.count_ask * 100
    text = f'Разів відповіли: {current_question.count_ask}\n' \
           f'Вірних відповідей: {current_question.count_right_ask}\n' \
           f'Успішність: {round(c,2)}%'
    lb_statistic.setText(text)
    win_card.hide()
    menu_win.show()

btn_menu.clicked.connect(menu_show)

def menu_back():
    menu_win.hide()
    win_card.show()

btn_back.clicked.connect(menu_back)

app.exec_()