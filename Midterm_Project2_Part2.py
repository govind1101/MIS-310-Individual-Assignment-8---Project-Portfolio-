from tkinter import *
from PIL import ImageTk, Image
import pandas as pd

# -------------------------
# Window setup
# -------------------------
root = Tk()
root.title('CCSU Mobile App')
root.geometry("700x500")
root.resizable(0, 0)
root.configure(bg='light blue')

# -------------------------
# Logo setup
# -------------------------
img = Image.open('logo1.PNG')

try:
    img = img.resize((100, 100), Image.Resampling.LANCZOS)
except AttributeError:
    img = img.resize((100, 100), Image.ANTIALIAS)

img = img.convert("RGBA")
data_img = img.getdata()

newData = []
for item in data_img:
    if item[:3] == (255, 255, 255):
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("transparent.png")

logo = Image.open("transparent.png")
logo = ImageTk.PhotoImage(logo)

logoLabel = Label(root, image=logo, bg='light blue')
logoLabel.place(x=10, y=10)

# -------------------------
# Load CSV
# -------------------------
data = pd.read_csv("examfile.csv")

# Output label
lb = Label(root, justify="left", bg="light blue", anchor="nw")
lb.place(x=50, y=160, width=600, height=300)

# -------------------------
# Original button functions
# -------------------------
def calender():
    df = pd.DataFrame(data, columns=['CalendarDate'])
    selected_rows = df[~df['CalendarDate'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))

def building():
    df = pd.DataFrame(data, columns=['Buildings'])
    selected_rows = df[~df['Buildings'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))

def faculty():
    df = pd.DataFrame(data, columns=['FacultyName'])
    selected_rows = df[~df['FacultyName'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))

# -------------------------
# NEW Part 2 functions
# -------------------------
def school_business():
    programs = [
        "Accounting",
        "Finance",
        "Management & Organization",
        "Marketing",
        "Management Information Systems (MIS)",
        "Business Analytics"
    ]
    lb.config(text="\n".join(programs))

def mis_department():
    courses = [
        "Intro to MIS",
        "Databases Management",
        "Systems Analysis & Design",
        "Business Analytics / Data Visualization",
        "Network and Information Security",
        "Project Management"
    ]
    lb.config(text="\n".join(courses))

# -------------------------
# Buttons (ALL horizontal)
# -------------------------
button1 = Button(root, text='Calendar', command=calender, bg="light green")
button1.place(x=20, y=120, width=100)

button2 = Button(root, text='Buildings', command=building, bg="light green")
button2.place(x=130, y=120, width=100)

button3 = Button(root, text='Faculty', command=faculty, bg="light green")
button3.place(x=240, y=120, width=100)

button4 = Button(root, text='School of Business', command=school_business, bg="light yellow")
button4.place(x=350, y=120, width=140)

button5 = Button(root, text='MIS Department', command=mis_department, bg="light cyan")
button5.place(x=500, y=120, width=150)

# -------------------------
root.mainloop()