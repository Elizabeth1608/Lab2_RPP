import sys
from PyQt5.QtWidgets import QApplication, QWidget
from task4 import Ui_Form


class NimGame(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_new.clicked.connect(self.new_game)
        self.btn_take.clicked.connect(self.player_move)
        self.stones = 0
    
    def new_game(self):
        """Начать новую игру с N камней"""
        try:
            self.stones = int(self.line_n.text())
            if self.stones < 5:
                self.label_msg.setText("Минимум 5 камней!")
                return
            self.label_count.setText(f"Камней: {self.stones}")
            self.label_msg.setText("Ваш ход!")
        except:
            self.label_msg.setText("Введите число!")
    
    def player_move(self):
        """Ход игрока"""
        if self.stones == 0:
            self.label_msg.setText("Начните новую игру!")
            return
        
        try:
            take = int(self.line_take.text())
        except:
            self.label_msg.setText("Введите число 1-3!")
            return
        
        # Проверка ошибочных значений
        if take < 1 or take > 3:
            self.label_msg.setText("Можно брать 1-3 камня!")
            return
        if take > self.stones:
            self.label_msg.setText(f"В куче только {self.stones}!")
            return
        
        # Игрок берёт камни
        self.stones -= take
        self.label_count.setText(f"Камней: {self.stones}")
        
        # Проверка окончания
        if self.stones == 0:
            self.label_msg.setText("ВЫ ВЫИГРАЛИ! 🎉")
            return
        
        # Ход ИИ
        self.computer_move()
    
    def computer_move(self):
        """Ход ИИ (выигрышная стратегия)"""
        # Оставляем после хода N % 4 == 1
        take = (self.stones - 1) % 4
        if take == 0:
            take = 1  # Не можем выиграть берём 1
        
        self.stones -= take
        self.label_count.setText(f"Камней: {self.stones}")
        
        if self.stones == 0:
            self.label_msg.setText(f"ИИ взял {take}. ВЫ ПРОИГРАЛИ 💻")
        else:
            self.label_msg.setText(f"ИИ взял {take}. Ваш ход!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NimGame()
    window.show()
    sys.exit(app.exec_())