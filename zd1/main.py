import sys
from PyQt5.QtWidgets import QApplication, QWidget
from task1 import Ui_Form


class FlagApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw_flag)
    
    def draw_flag(self):
        result = []
        groups = [
            [self.radioButton, self.radioButton_2, self.radioButton_3],
            [self.radioButton_4, self.radioButton_5, self.radioButton_6],
            [self.radioButton_7, self.radioButton_8, self.radioButton_9]
        ]
        for group in groups:
            for rb in group:
                if rb.isChecked():
                    result.append(rb.text())
                    break
            else:
                result.append("?")
        
        self.label.setText(", ".join(result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlagApp()
    window.show()
    sys.exit(app.exec_())