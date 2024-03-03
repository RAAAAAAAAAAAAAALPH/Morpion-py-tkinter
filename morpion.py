import tkinter as tk
import random

class Morpion:
    def __init__(self, root):
        self.root = root
        self.root.title("Morpion")

        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.buttons = [[None]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text=" ", font=('Arial', 30), width=5, height=2, 
                                                command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)
        
        self.status_label = tk.Label(root, text="Tour du joueur X", font=('Arial', 12))
        self.status_label.grid(row=3, columnspan=3)

    def on_button_click(self, i, j):
        if self.board[i][j] == " ":
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner():
                self.status_label.config(text=f"Le joueur {self.current_player} a gagné !")
                self.disable_buttons()
            elif self.check_board_full():
                self.status_label.config(text="Match nul !")
                self.disable_buttons()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Tour du joueur {self.current_player}")

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def check_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)


root = tk.Tk()
game = Morpion(root)
root.mainloop()
