import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, PhotoImage

def simplex(ind,c, A, b):
    m, n = len(A), len(A[0])
    tableau = [row[:] + [0] * (m + 1) + [b_val] for row, b_val in zip(A, b)]
    tableau.append(c[:] + [0] * (m + 2))
    for i in range(m):
        tableau[i][n + i] = 1
    basic_vari_index = list(range(n + 1, n + m + 1))

    while min(tableau[-1][:-1]) < 0:
        pivot_col = tableau[-1][:-1].index(min(tableau[-1][:-1]))
        ratios = [(tableau[i][-1] / tableau[i][pivot_col], i) for i in range(m) if tableau[i][pivot_col] > 0]
        if not ratios:
            return None, None
        pivot_row = min(ratios)[1]
        pivot_element = tableau[pivot_row][pivot_col]
        tableau[pivot_row] = [x / pivot_element for x in tableau[pivot_row]]
        basic_vari_index[pivot_row] = pivot_col + 1
        for i in range(len(tableau)):
            if i != pivot_row:
                ratio = tableau[i][pivot_col]
                tableau[i] = [tableau[i][j] - ratio * tableau[pivot_row][j] for j in range(len(tableau[i]))]

    b_final = [tableau[i][-1] for i in range(m)]
    solution = [0] * (m + n + 1)
    for i in range(len(basic_vari_index)):
        solution[basic_vari_index[i]] = b_final[i]

    x_result=solution[1:n + 1]
    y_result=ind*tableau[-1][-1]

    for i in range(m):
        lhs = sum(A[i][j] * x_result[j] for j in range(n))
        if lhs - b[i] > 1e-8:
            return None, None

    return x_result, y_result

root = tk.Tk()
root.title("Linear Programming Solver (Simplex Method)")

# Top input section
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

tk.Label(top_frame, text="Objective:").grid(row=0, column=0, padx=5)
objective_var = tk.StringVar(value="max")
objective_menu = ttk.Combobox(top_frame, textvariable=objective_var, values=["min", "max"], width=5, state="readonly")
objective_menu.grid(row=0, column=1, padx=5)

tk.Label(top_frame, text="Number of variables (n):").grid(row=0, column=2, padx=5)
entry_n = tk.Entry(top_frame, width=5)
entry_n.grid(row=0, column=3, padx=5)

tk.Label(top_frame, text="Number of constraints (m):").grid(row=0, column=4, padx=5)
entry_m = tk.Entry(top_frame, width=5)
entry_m.grid(row=0, column=5, padx=5)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

entries_obj = []
entries_con = []
entries_rhs = []
entries_bounds = []

result_frame = None
result_text = None

def draw_dashed_separator(parent):
    canvas = tk.Canvas(parent, height=2, bg="white", highlightthickness=0)
    canvas.pack(fill='x', pady=5)
    canvas.create_line(0, 1, 1000, 1, dash=(4, 4), fill="gray")

def on_define():
    global entries_obj, entries_con, entries_rhs, entries_bounds
    for widget in input_frame.winfo_children():
        widget.destroy()

    try:
        n = int(entry_n.get())
        m = int(entry_m.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integers for number of variables and constraints.")
        return


    entries_obj = []
    entries_con = []
    entries_rhs = []
    entries_bounds = []

    # Objective function
    tk.Label(input_frame, text="Objective Function:").pack(anchor='w')
    obj_frame = tk.Frame(input_frame)
    obj_frame.pack()
    for j in range(n):
        e = tk.Entry(obj_frame, width=6)
        e.insert(0, "0")
        e.grid(row=0, column=2 * j)
        if j < n - 1:
            tk.Label(obj_frame, text=f"x{j + 1}+").grid(row=0, column=2 * j + 1)
        else:
            tk.Label(obj_frame, text=f"x{j + 1}").grid(row=0, column=2 * j + 1)
        entries_obj.append(e)

    draw_dashed_separator(input_frame)

    # Constraints
    tk.Label(input_frame, text="Constraints:").pack(anchor='w')
    for i in range(m):
        con_frame = tk.Frame(input_frame)
        con_frame.pack()
        row_entries = []
        for j in range(n):
            e = tk.Entry(con_frame, width=6)
            e.insert(0, "0")
            e.grid(row=0, column=2 * j)
            if j < n - 1:
                tk.Label(con_frame, text=f"x{j + 1}+").grid(row=0, column=2 * j + 1)
            else:
                tk.Label(con_frame, text=f"x{j + 1}").grid(row=0, column=2 * j + 1)
            row_entries.append(e)

        tk.Label(con_frame, text="≤").grid(row=0, column=2 * n)
        b_entry = tk.Entry(con_frame, width=6)
        b_entry.insert(0, "0")
        b_entry.grid(row=0, column=2 * n + 1)
        entries_con.append(row_entries)
        entries_rhs.append(b_entry)
    draw_dashed_separator(input_frame)

    # Variable bounds
    tk.Label(input_frame, text="Variable Bounds:").pack(anchor='w')
    bounds_frame = tk.Frame(input_frame)
    bounds_frame.pack()
    for j in range(n):
        lower = tk.Entry(bounds_frame, width=6)
        lower.insert(0, "-inf")
        lower.grid(row=0, column=5 * j)
        tk.Label(bounds_frame, text=f"≤ x{j + 1} ≤").grid(row=0, column=5 * j + 1)
        upper = tk.Entry(bounds_frame, width=6)
        upper.insert(0, "inf")
        upper.grid(row=0, column=5 * j + 2)
        entries_bounds.append((lower, upper))
        if j < n - 1:
            tk.Label(bounds_frame, text="|").grid(row=0, column=5 * j + 3)

    middle_frame = tk.Frame(root)
    middle_frame.pack(side='bottom', fill='x', pady=10, padx=10)

    img = PhotoImage(file='docs/J-MTS.png')
    img_label = tk.Label(middle_frame, image=img)
    img_label.image = img
    img_label.pack(side='left')

    solve_button = tk.Button(middle_frame, width=8, height=2, text="Solve", command=solve)
    solve_button.pack(side='right')

def solve():
    global result_frame, result_text

    try:
        c = [float(e.get()) for e in entries_obj]
        A = [[float(e.get()) for e in row] for row in entries_con]
        b = [float(e.get()) for e in entries_rhs]
        if objective_var.get() == "max":
            c = [-x for x in c]  # Convert max to min
            ind = 1
        else:
            ind=-1

        n = len(entries_obj)
        # Add bounds as constraints
        for j in range(n):
            lower_str = entries_bounds[j][0].get()
            upper_str = entries_bounds[j][1].get()

            # Convert bounds to float if possible
            try:
                lower = float(lower_str)
                # -x_j <= -lower
                row = [0] * n
                row[j] = -1
                A.append(row)
                b.append(-lower)
            except ValueError:
                pass  # Treat as -inf

            try:
                upper = float(upper_str)
                # x_j <= upper
                row = [0] * n
                row[j] = 1
                A.append(row)
                b.append(upper)
            except ValueError:
                pass  # Treat as inf

        x_opt, f_opt = simplex(ind,c, A, b)

        if result_frame is None:
            result_frame = tk.Frame(root)
            result_frame.pack(fill='both', expand=True, padx=10, pady=10)
            result_text = tk.Text(result_frame, height=12, wrap='word')
            result_text.pack(fill='both', expand=True)

        result_text.config(state='normal')
        result_text.delete('1.0', tk.END)

        if x_opt is None:
            result_text.insert(tk.END, "No feasible solution.\n\n")
        else:
            result_text.insert(tk.END, f"Optimal solution (x): {x_opt}\n")
            result_text.insert(tk.END, f"Optimal objective value: {f_opt}\n\n")

        result_text.insert(tk.END, "Objective coefficients (c):\n")
        result_text.insert(tk.END, f"{c}\n\n")

        result_text.insert(tk.END, "Constraint matrix (A):\n")
        for row in A:
            result_text.insert(tk.END, f"{row}\n")
        result_text.insert(tk.END, f"\nRight-hand side vector (b):\n{b}\n\n")

        result_text.config(state='disabled')

    except Exception as e:
        messagebox.showerror("Error", str(e))

define_button = tk.Button(top_frame, text="Define", command=on_define, width=5, height=1,bg="cyan")
define_button.grid(row=0, column=6, padx=10)

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', pady=5)

root.mainloop()
