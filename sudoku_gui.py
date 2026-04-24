import tkinter as tk
from tkinter import messagebox

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver Pro")
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        
        self.vcmd = (self.root.register(self.validate_entry), '%P')
        
        self.create_grid()
        
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        self.solve_button = tk.Button(button_frame, text="Resolver", command=self.solve_and_display, 
                                 font=('Arial', 12, 'bold'), bg="#4caf50", fg="white", padx=15)
        self.solve_button.grid(row=0, column=0, padx=10)

        self.clear_button = tk.Button(button_frame, text="Limpar", command=self.clear_board, 
                                 font=('Arial', 12, 'bold'), bg="#f44336", fg="white", padx=15)
        self.clear_button.grid(row=0, column=1, padx=10)

    def validate_entry(self, P):
        if P == "" or (len(P) == 1 and P.isdigit() and P != '0'):
            return True
        return False

    def create_grid(self):
        # O segredo do visual "limpo" é usar bg='black' no frame e padx/pady zero onde não queremos bordas extras
        main_frame = tk.Frame(self.root, bg='black', bd=2)
        main_frame.pack(pady=20, padx=20)

        for row in range(9):
            for col in range(9):
                sf_row, sf_col = row // 3, col // 3
                # Define a cor de fundo original
                bg_color = "white" if (sf_row + sf_col) % 2 == 0 else "#f0f0f0"
                
                # Criamos um frame interno de 1px de espessura para fazer a borda de cada célula
                # mas aumentamos o destaque nos limites 3x3
                p_x = (2, 1) if col % 3 == 0 and col != 0 else 1
                p_y = (2, 1) if row % 3 == 0 and row != 0 else 1

                # Padding externo no grid cria a ilusão das linhas grossas
                entry = tk.Entry(main_frame, width=2, font=('Arial', 24),
                                 justify='center', bg=bg_color, bd=0, # bd=0 remove a borda interna
                                 relief="flat", insertontime=0, 
                                 validate='key', validatecommand=self.vcmd)
                
                # Usamos padx/pady diferenciados para as divisões 3x3
                entry.grid(row=row, column=col, 
                           padx=(2 if col % 3 == 0 and col != 0 else 1, 0),
                           pady=(2 if row % 3 == 0 and row != 0 else 1, 0), 
                           sticky="nsew")
                
                self.cells[row][col] = entry
                
                entry.bind('<KeyPress>', lambda e, r=row, c=col: self.handle_keys(e, r, c))
                entry.bind('<FocusIn>', lambda e, r=row, c=col: self.highlight(r, c))
                entry.bind('<FocusOut>', lambda e, r=row, c=col: self.unhighlight(r, c))

    def highlight(self, row, col):
        # Amarelo destaque preenchendo tudo
        self.cells[row][col].config(bg="#fff9c4") 

    def unhighlight(self, row, col):
        sf_row, sf_col = row // 3, col // 3
        orig_bg = "white" if (sf_row + sf_col) % 2 == 0 else "#f0f0f0"
        self.cells[row][col].config(bg=orig_bg)

    def handle_keys(self, event, row, col):
        key = event.keysym
        if key == 'Up': self.cells[(row - 1) % 9][col].focus_set()
        elif key == 'Down': self.cells[(row + 1) % 9][col].focus_set()
        elif key == 'Left': self.cells[row][(col - 1) % 9].focus_set()
        elif key == 'Right': self.cells[row][(col + 1) % 9].focus_set()
        elif key == 'BackSpace':
            self.cells[row][col].delete(0, tk.END)

    def clear_board(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
                self.cells[row][col].config(fg='black')

    def get_board(self):
        board = []
        for row in range(9):
            current_row = []
            for col in range(9):
                val = self.cells[row][col].get()
                if val == "":
                    current_row.append(0)
                    self.cells[row][col].config(fg='blue') 
                else:
                    current_row.append(int(val))
                    self.cells[row][col].config(fg='black')
            board.append(current_row)
        return board

    def display_solution(self, board):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].get() == "":
                    self.cells[row][col].insert(0, str(board[row][col]))

    def is_valid(self, board, r, c, num):
        for i in range(9):
            if board[r][i] == num or board[i][c] == num: return False
        sr, sc = (r // 3) * 3, (c // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[sr + i][sc + j] == num: return False
        return True

    def solve_backtracking(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    for num in range(1, 10):
                        if self.is_valid(board, r, c, num):
                            board[r][c] = num
                            if self.solve_backtracking(board): return True
                            board[r][c] = 0
                    return False
        return True

    def solve_and_display(self):
        board = self.get_board()
        if self.solve_backtracking(board):
            self.display_solution(board)
        else:
            messagebox.showinfo("Sudoku", "Sem solução!")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#e0e0e0")
    # Um pouco mais largo para acomodar o visual novo
    root.geometry("480x620")
    app = SudokuSolverGUI(root)
    root.mainloop()