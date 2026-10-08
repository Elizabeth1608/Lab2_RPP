import sys
from PyQt5.QtWidgets import QApplication, QWidget
from task2 import Ui_Form  # ← импорт из task2.py


class DiaryApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_add.clicked.connect(self.add_event)
    
    def add_event(self):
        name = self.line_name.text().strip()
        if not name:
            return  
        
        date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        time = self.time_edit.time().toString("HH:mm")
        
        event = f"{date} {time} — {name}"
        
        self.list_events.addItem(event)
        self.list_events.sortItems()
        
        self.line_name.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DiaryApp()
    window.show()
    sys.exit(app.exec_())