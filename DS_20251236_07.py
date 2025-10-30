from tkinter import *

def draw_box():
    canvas.delete("all")
    canvas.create_rectangle(50, 50, 150, 150, fill="red")
    
def draw_circle():
    canvas.delete("all")
    canvas.create_oval(200, 80, 300, 180, fill="blue")
    
def draw_image():
    global img
    canvas.delete("all")
    
    img = PhotoImage(file="duksung.jpg")
    canvas.create_image(420, 420, anchor=NW, image=img)

def delete_all():
    canvas.delete("all")

root = Tk()
root.title("중간고사 7번")
root.geometry("420x440")

canvas = Canvas(root, width=400, height=320, bg="white")
canvas.pack()

shape_var = IntVar()
shape_var.set(1)

frame = Frame(root)
frame.pack(pady=10)


Button(frame, text="사각형", command=draw_box, bg="lightgray").pack(side="left", padx=10)
Button(frame, text="원", command=draw_circle, bg="lightgray").pack(side="left", padx=10)
Button(frame, text="그림", command=draw_image, bg="lightgray").pack(side="left", padx=10)
Button(frame, text="지우기", command=delete_all, bg="lightgray").pack(side="left", padx=10)

root.mainloop()