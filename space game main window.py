from tkinter import *
import tkinter as tk

def new_win():
    win = Toplevel(root)
    label1 = Label(win, text="Text in up window", font = 20)
    label1.pack

def exit_app():
    root.destroy()
    
root = tk.Tk()

main_menu = Menu(root)
root.configure(menu=main_menu)

first_item = Menu(main_menu)
main_menu.add_cascade(label="File", menu=first_item)
first_item.add_command(label="New", command=new_win)
first_item.add_command(label="Load", )
first_item.add_command(label="Save", )
first_item.add_command(label="Exit", command=exit_app)

#створення фреймів
right_frame = Frame(root)
right_frame.pack()

top_frame = Frame(root)
top_frame.pack()

c1 = Canvas(root, width=800, height=600, bg="silver")
c1.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

#створення кнопок
button1 = Button(top_frame, text="Game", fg="blue")
button2 = Button(top_frame, text="Space", fg="blue")
button3 = Button(top_frame, text="Planets", fg="green")
button4 = Button(top_frame, text="Design", fg="orange")
button5 = Button(bottom_frame, text="Space force", fg="green")
button6 = Button(bottom_frame, text="Races", fg="dark green")
button7 = Button(bottom_frame, text="Science", fg="red")
button8 = Button(bottom_frame, text="End of turn", fg="black")

#відображення кнопок
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)
button6.pack(side=LEFT)
button7.pack(side=LEFT)
button8.pack(side=LEFT)

root.mainloop()

