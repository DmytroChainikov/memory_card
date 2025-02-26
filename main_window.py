from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QSpinBox, QGroupBox, QButtonGroup
from PyQt5.QtCore import Qt
from random import shuffle


win_card = QWidget()
win_card.resize(600, 500)
win_card.setWindowTitle('Memory Card')
win_card.move(100,100)


btn_menu = QPushButton('Меню')

btn_sleep = QPushButton('Відпочити')
box_sleep = QSpinBox()
box_sleep.setValue(30)
label_sleep = QLabel('хвилин')

label_question = QLabel('Питання')

btn_answer = QPushButton('Відповісти')

radio_group = QGroupBox('Варіанти відповіді') # група радіокнопок
radio_btn_group = QButtonGroup() # самі кнопки

r_btn1 = QRadioButton('')
r_btn2 = QRadioButton('')
r_btn3 = QRadioButton('')
r_btn4 = QRadioButton('')
radio_btn_group.addButton(r_btn1)
radio_btn_group.addButton(r_btn2)
radio_btn_group.addButton(r_btn3)
radio_btn_group.addButton(r_btn4)

ans1_layout = QHBoxLayout()
ans2_layout = QVBoxLayout()
ans3_layout = QVBoxLayout()

ans2_layout.addWidget(r_btn1)
ans2_layout.addWidget(r_btn2)
ans3_layout.addWidget(r_btn3)
ans3_layout.addWidget(r_btn4)

ans1_layout.addLayout(ans2_layout)
ans1_layout.addLayout(ans3_layout)

radio_group.setLayout(ans1_layout)

ans_group = QGroupBox('Результат тесту')
label_correct_ans = QLabel('правильно') # правильно/неправильно
label_correct = QLabel('правильно')

result_layout = QVBoxLayout()
result_layout.addWidget(label_correct_ans, alignment=(Qt.AlignLeft | Qt.AlignTop))
result_layout.addWidget(label_correct, alignment=Qt.AlignHCenter, stretch=2)
ans_group.setLayout(result_layout)
ans_group.hide()

card_layout = QVBoxLayout()

line1_layout = QHBoxLayout()
line1_layout.addWidget(btn_menu)
line1_layout.addStretch(1)
line1_layout.addWidget(btn_sleep)
line1_layout.addWidget(box_sleep)
line1_layout.addWidget(label_sleep)

line2_layout = QHBoxLayout()
line2_layout.addWidget(label_question, alignment=Qt.AlignCenter)

line3_layout = QHBoxLayout()
line3_layout.addWidget(radio_group)
line3_layout.addWidget(ans_group)

line4_layout = QHBoxLayout()
line4_layout.addWidget(btn_answer)

card_layout.addLayout(line1_layout, stretch=1)
card_layout.addLayout(line2_layout, stretch=2)
card_layout.addLayout(line3_layout, stretch=8)
card_layout.addStretch(1)
card_layout.addLayout(line4_layout)
card_layout.addStretch(1)

win_card.setLayout(card_layout)
win_card.show()