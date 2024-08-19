import tkinter as tk

class Sudoku:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            for j in range(9):
                frame = tk.Frame(self.root, width=50, height=50, bg="white", borderwidth=1, relief="solid")
                frame.grid(row=i, column=j, padx=0, pady=0)
                
                entry = tk.Entry(frame, width=2, font=('Arial', 18), justify='center', bd=0, bg="white", fg="black")
                entry.pack(expand=True, fill=tk.BOTH)

        tk.Button(self.root, text="Restart").grid(row=9, column=0, columnspan=4, pady=5)
        tk.Button(self.root, text="New Game").grid(row=9, column=5, columnspan=4, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    gui = Sudoku(root)
    root.mainloop()