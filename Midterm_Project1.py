import tkinter as tk

# -------------------------
# Window setup
# -------------------------
root = tk.Tk()
root.title("Student Grade App")
root.geometry("400x400")

# -------------------------
# Variables
# -------------------------
scores = []


# -------------------------
# Functions
# -------------------------

# add score to list
def add_score():
    score = float(entry_score.get())
    scores.append(score)
    entry_score.delete(0, tk.END)
    label_output.config(text="Score added")


# calculate average and grade
def calculate():
    if len(scores) == 0:
        label_output.config(text="No scores entered")
        return

    total = 0
    for s in scores:
        total += s

    avg = total / len(scores)

    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"

    label_output.config(text="Average: " + str(round(avg, 2)) + "  Grade: " + grade)


# clear all scores
def clear():
    scores.clear()
    label_output.config(text="Data cleared")


# -------------------------
# GUI Widgets
# -------------------------

# title
tk.Label(root, text="Grade Calculator").pack()

# input
tk.Label(root, text="Enter Score:").pack()
entry_score = tk.Entry(root)
entry_score.pack()

# buttons
tk.Button(root, text="Add Score", command=add_score).pack()
tk.Button(root, text="Calculate", command=calculate).pack()
tk.Button(root, text="Clear", command=clear).pack()

# output
label_output = tk.Label(root, text="")
label_output.pack()

# -------------------------
root.mainloop()