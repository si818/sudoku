import tkinter as tk
import random

class Sudoku:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.grid = [[None for _ in range(9)] for _ in range(9)]
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.solution = [[None for _ in range(9)] for _ in range(9)]
        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        for i in range(9):
            for j in range(9):
                frame = tk.Frame(self.root, width=50, height=50, bg="white", borderwidth=1, relief="solid")
                frame.grid(row=i, column=j, padx=0, pady=0)
                
                self.entries[i][j] = tk.Entry(frame, width=2, font=('Arial', 18), justify='center', bd=0, bg="white", fg="black")
                self.entries[i][j].pack(expand=True, fill=tk.BOTH)
                self.entries[i][j].bind("<KeyRelease>", lambda event, x=i, y=j: self.check_input(x, y))

        tk.Button(self.root, text="Restart", command=self.restart_game).grid(row=9, column=0, columnspan=4, pady=5)
        tk.Button(self.root, text="New Game", command=self.new_game).grid(row=9, column=5, columnspan=4, pady=5)

    def check_input(self, x, y):
        user_input = self.entries[x][y].get()
        if not user_input.isdigit() or int(user_input) not in range(1, 10):
            self.entries[x][y].delete(0, tk.END)
        elif int(user_input) != self.solution[x][y]:
            self.entries[x][y].config(fg='red')
        else:
            self.entries[x][y].config(fg='black')

    def restart_game(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if self.grid[i][j] != 0:
                    self.entries[i][j].insert(0, self.grid[i][j])
                    self.entries[i][j].config(state='readonly')
                else:
                    self.entries[i][j].config(state='normal', fg='black')

    def new_game(self):
        self.grid = self.generate_sudoku()
        self.solution = [row[:] for row in self.grid]  # Copy for solution
        self.solve_sudoku(self.solution)
        self.restart_game()

    def generate_sudoku(self):
        base = 3
        side = base * base

        def pattern(r, c):
            return (base*(r % base)+r//base+c) % side

        def shuffle(s):
            return random.sample(s, len(s))

        rBase = range(base)
        rows = [g*base + r for g in shuffle(rBase) for r in shuffle(rBase)]
        cols = [g*base + c for g in shuffle(rBase) for c in shuffle(rBase)]
        nums = shuffle(range(1, base*base+1))

        board = [[nums[pattern(r, c)] for c in cols] for r in rows]

        squares = side*side
        no_of_empty_cells = squares * 3//4
        for p in random.sample(range(squares), no_of_empty_cells):
            board[p//side][p % side] = 0

        return board

    def solve_sudoku(self, board):
        empty = self.find_empty(board)
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.is_valid(board, num, row, col):
                board[row][col] = num
                if self.solve_sudoku(board):
                    return True
                board[row][col] = 0

        return False

    def is_valid(self, board, num, row, col):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        box_x = col // 3
        box_y = row // 3
        for i in range(box_y*3, box_y*3+3):
            for j in range(box_x*3, box_x*3+3):
                if board[i][j] == num:
                    return False

        return True

    def find_empty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

if __name__ == "__main__":
    root = tk.Tk()
    game = Sudoku(root)
    root.mainloop()