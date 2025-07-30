import math
import tkinter as tk
from tkinter import messagebox
import random

class SudokuCell(tk.Entry):
    def __init__(self, master, row, col, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.row = row
        self.col = col
        self.grid(row=row, column=col, ipadx=5, ipady=5, padx=1, pady=1)
        self.configure(font=('Segoe UI', 16), justify='center', width=2, bg='#ffe6f2', bd=0)

class AnneSu11(tk.Tk):
    PUZZLES = [
        "53..7....6..195....98....6.8...6...34..8..6.7...2...6.6....28....419..5....8..79",
        "..3.2.6..9..3.5..1..18.64..81.29..7....8....4..17.69..98.47..8..1.5..9..4.2.3.."
    ]

    def __init__(self):
        super().__init__()
        self.title('AnneSu11')
        self.configure(bg='#ffc0cb')
        self.cells = []
        self.create_widgets()
        self.new_game()
        self.animate_bubble()

    def create_widgets(self):
        grid_frame = tk.Frame(self, bg='#ffb6c1', bd=4)
        grid_frame.pack(padx=10, pady=10)
        for r in range(9):
            row = []
            for c in range(9):
                cell = SudokuCell(grid_frame, r, c)
                row.append(cell)
            self.cells.append(row)

        button_frame = tk.Frame(self, bg='#ffc0cb')
        button_frame.pack(pady=5)
        tk.Button(button_frame, text='Nouveau', command=self.new_game, bg='#ffe6f2').grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text='Vérifier', command=self.check_board, bg='#ffe6f2').grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text='Aide', command=self.show_help, bg='#ffe6f2').grid(row=0, column=2, padx=5)

        # Canvas for Lys AI bubble
        self.canvas = tk.Canvas(self, width=100, height=100, bg='#ffc0cb', highlightthickness=0)
        self.canvas.pack(pady=5)
        self.bubble = self.canvas.create_oval(20, 20, 80, 80, outline='#ff69b4', width=2)
        # simple flower
        self.canvas.create_oval(45, 45, 55, 55, fill='#ff69b4', outline='')
        for angle in range(0, 360, 72):
            x = 50 + 15 * math.cos(math.radians(angle))
            y = 50 + 15 * math.sin(math.radians(angle))
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill='#ff69b4', outline='')
        self.bubble_delta = 1

    def new_game(self):
        puzzle = random.choice(self.PUZZLES)
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                val = puzzle[i*9 + j]
                if val == '.':
                    cell.delete(0, tk.END)
                    cell.config(state='normal', fg='black')
                else:
                    cell.delete(0, tk.END)
                    cell.insert(0, val)
                    cell.config(state='disabled', disabledforeground='black')

    def check_board(self):
        board = []
        for row in self.cells:
            board_row = []
            for cell in row:
                val = cell.get()
                if val == '':
                    messagebox.showinfo('AnneSu11', 'La grille n\u2019est pas complète')
                    return
                board_row.append(val)
            board.append(board_row)
        if self.is_valid(board):
            messagebox.showinfo('AnneSu11', 'Bravo, Sudoku terminé !')
        else:
            messagebox.showwarning('AnneSu11', 'Il y a des erreurs dans la grille.')

    def is_valid(self, board):
        for i in range(9):
            row = set()
            col = set()
            block = set()
            for j in range(9):
                r = board[i][j]
                c = board[j][i]
                br = board[3*(i//3) + j//3][3*(i%3) + j%3]
                if r in row or c in col or br in block:
                    return False
                row.add(r)
                col.add(c)
                block.add(br)
        return True

    def show_help(self):
        messagebox.showinfo('Aide', 'Remplissez la grille avec les nombres de 1 à 9 sans répétition sur chaque ligne, colonne et bloc 3x3.')

    def animate_bubble(self):
        x1, y1, x2, y2 = self.canvas.coords(self.bubble)
        if x1 <= 15 or x2 >= 85:
            self.bubble_delta *= -1
        self.canvas.move(self.bubble, self.bubble_delta, 0)
        self.after(50, self.animate_bubble)

if __name__ == '__main__':
    app = AnneSu11()
    app.mainloop()
