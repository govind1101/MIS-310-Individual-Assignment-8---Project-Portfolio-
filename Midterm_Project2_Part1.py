from tkinter import *
from PIL import ImageTk, Image
import pandas as pd

# -------------------------
# Window setup
# -------------------------
root = Tk()
root.title('CCSU Mobile App')
root.geometry("600x500")   # slightly larger so text isn’t cut off
root.resizable(0, 0)
root.configure(bg='light blue')

# -------------------------
# Logo setup (same as given, fixed indentation)
# -------------------------
img = Image.open('transparent.PNG')

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

# Output label (bigger so text fits)
lb = Label(root, justify="left", bg="light blue", anchor="nw")
lb.place(x=50, y=160, width=500, height=300)

# -------------------------
# Button functions
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
# Buttons (horizontal)
# -------------------------
button1 = Button(root, text='Calendar', command=calender, bg="light green")
button1.place(x=50, y=120, width=100)

button2 = Button(root, text='Buildings', command=building, bg="light green")
button2.place(x=170, y=120, width=100)

button3 = Button(root, text='Faculty', command=faculty, bg="light green")
button3.place(x=290, y=120, width=100)

# -------------------------
root.mainloop()