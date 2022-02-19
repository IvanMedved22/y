from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout
import json
 
app = QApplication([])
    
'''��������� ����������'''
#��������� ���� ����������
notes_win = QWidget()
notes_win.setWindowTitle('����� �������')
notes_win.resize(900, 600)
 
#������� ���� ����������
list_notes_label = QLabel('������ �������')
list_notes = QListWidget()

button_note_create = QPushButton('������� �������') #���������� ���� � ����� "������� ��� �������"
button_note_del = QPushButton('������� �������')
button_note_save = QPushButton('��������� �������')
 
field_tag = QLineEdit('')
field_tag.setPlaceholderText('������� ���...')
field_text = QTextEdit()
button_tag_add = QPushButton('�������� � �������')
button_tag_del = QPushButton('��������� �� �������')
button_tag_search = QPushButton('������ ������� �� ����')

list_tags_label = QLabel('������ �����')
list_tags = QListWidget()
 
#������������ �������� �� ��������
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)
 
col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)
 
col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)
 
col_2.addLayout(row_3)
col_2.addLayout(row_4)
 
layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["�����"])
    list_tags.clear()
    list_tags.addItems(notes[key]["����"])    
    
def add_note():
    note_name, ok = QInputDialog.getText(notes_win, "�������� �������", "�������� �������")
    if ok and note_name != "":
        notes[note_name] = {"�����": "", "����": []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]["����"])
        print(notes)
        
def save_note():
    pass

def del_note():
    pass

def add_tag():
    pass

def del_tag():
    pass

def search_tag():
    pass

#������ ���������� 
list_notes.itemClicked.connect(show_note)
button_note_create.clicked.connect(add_note)
button_note_save.clicked.connect(save_note)
button_note_del.clicked.connect(del_note)
button_tag_add.clicked.connect(add_tag)
button_tag_del.clicked.connect(del_tag)
button_tag_search.clicked.connect(search_tag)

notes_win.show()
with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)
app.exec_()



