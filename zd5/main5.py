import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from task5 import Ui_MainWindow


class AntiplagiatApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_check.clicked.connect(self.check)
    
    def check(self):
        """Проверка текстов на антиплагиат"""
        text1 = self.text1.toPlainText().strip()
        text2 = self.text2.toPlainText().strip()
        
        # Проверка на пустые поля
        if not text1 or not text2:
            self.statusbar.showMessage("Введите оба текста!")
            self.statusbar.setStyleSheet("color: orange; font-weight: bold;")
            return
        
        # Разбиваем на строки, убираем пустые
        lines1 = [line.strip() for line in text1.split('\n') if line.strip()]
        lines2 = [line.strip() for line in text2.split('\n') if line.strip()]
        
        # Считаем совпадения
        matches = sum(1 for line in lines1 if line in lines2)
        
        # Процент совпадения
        percent = matches / len(lines1) if lines1 else 0
        threshold = self.spin_threshold.value()
        
        # Формируем сообщение
        msg = f"Совпадение: {percent*100:.1f}% (порог: {threshold*100:.0f}%)"
        
        # Вывод в StatusBar с цветом
        if percent >= threshold:
            self.statusbar.showMessage(f"Плагиат! {msg}")
            self.statusbar.setStyleSheet("color: red; font-weight: bold;")
        else:
            self.statusbar.showMessage(f"Уникально. {msg}")
            self.statusbar.setStyleSheet("color: green; font-weight: bold;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AntiplagiatApp()
    window.show()
    sys.exit(app.exec_())