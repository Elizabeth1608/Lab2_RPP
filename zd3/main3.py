import sys
from PyQt5.QtWidgets import QApplication, QWidget
from task3 import Ui_Form


class NotebookApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_add.clicked.connect(self.add_contact)
    
    def add_contact(self):
        name = self.line_name.text().strip()
        phone = self.line_phone.text().strip()
        
        if not name or not phone:
            return
        contact = f"{name} {phone}"
        self.list_contacts.addItem(contact)
        self.line_name.clear()
        self.line_phone.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotebookApp()
    window.show()
    sys.exit(app.exec_())