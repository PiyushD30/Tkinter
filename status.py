from tkinter import *
from PIL import ImageTk, Image

global i
i = 0

root = Tk()

root.title("Daldom")
root.iconbitmap("lady.ico")

cris = ImageTk.PhotoImage(Image.open("./images/cristiano.jpg"))
steph = ImageTk.PhotoImage(Image.open("./images/steph.jpg"))
jordan = ImageTk.PhotoImage(Image.open("./images/jordan.jpg"))
virat = ImageTk.PhotoImage(Image.open("./images/virat.webp"))
novak = ImageTk.PhotoImage(Image.open("./images/novak.jpeg"))


image_list = [cris, steph, virat, jordan, novak]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN)


def Next(img_no):
    global myLabel
    myLabel.grid_forget()
    myLabel = Label(image=image_list[img_no - 1])
    next = Button(root, text="Next", command=lambda: Next(img_no + 1))
    previous = Button(root, text="Previous", command=lambda: Next(img_no - 1))
    status = Label(
        root,
        text="Image " + str(img_no) + " of " + str(len(image_list)),
        bd=1,
        relief=SUNKEN,
    )
    status.grid(row=2, column=0, columnspan=3, pady=10, sticky=W + E)

    if img_no == 5:
        myLabel = Label(image=image_list[4])
        myLabel.grid(row=0, column=0, columnspan=3)
        next = Button(root, text="Next", state= DISABLED)

    if img_no == 1:
        myLabel = Label(image=image_list[0])
        myLabel.grid(row=0, column=0, columnspan=3)
        previous = Button(root, text="Previous", state= DISABLED)

    next.grid(row=1, column=2)
    previous.grid(row=1, column=0)
    quit.grid(row=1, column=1)
    myLabel.grid(row=0, column=0, columnspan=3)


def Previous(img_no):
    global myLabel
    myLabel.grid_forget()
    myLabel = Label(image=image_list[img_no - 1])
    next = Button(root, text="Next", command=lambda: Next(img_no + 1))
    previous = Button(root, text="Previous", command=lambda: Next(img_no - 1))
    status = Label(
        root,
        text="Image " + str(img_no) + " of " + str(len(image_list)),
        bd=1,
        relief=SUNKEN,
    )
    status.grid(row=2, column=0, columnspan=3, pady=10, sticky=W + E)
    if img_no == 1:
        myLabel = Label(image=image_list[0])
        myLabel.grid(row=0, column=0, columnspan=3)
        previous = Button(root, text="Previous", state=DISABLED)

    if img_no == 5:
        myLabel = Label(image=image_list[4])
        myLabel.grid(row=0, column=0, columnspan=3)
        next = Button(root, text="Next", state=DISABLED)

    next.grid(row=1, column=2)
    previous.grid(row=1, column=0)
    quit.grid(row=1, column=1)
    myLabel.grid(row=0, column=0, columnspan=3)


next = Button(root, text="Next", command=lambda: Next(2))
previous = Button(root, text="Previous", state=DISABLED)
quit = Button(root, text="Exit", command=root.quit)

myLabel = Label(image=image_list[i])
myLabel.grid(row=0, column=0, columnspan=3)

next.grid(row=1, column=2, pady=10)
previous.grid(row=1, column=0)
quit.grid(row=1, column=1)

status.grid(row=2, column=0, columnspan=3, pady=10, sticky=W + E)

root.mainloop()
