from tkinter import *


root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def enter(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def Clear():
    e.delete(0, END)


def Add():
    first_number = e.get()
    global f_num
    global math
    f_num = int(first_number)
    math = "ADD"
    e.delete(0, END)


def Sub():
    first_number = e.get()
    global f_num
    global math
    math = "SUB"
    f_num = int(first_number)
    e.delete(0, END)


def Mul():
    first_number = e.get()
    global f_num
    global math
    math = "MUL"
    f_num = int(first_number)
    e.delete(0, END)


def Div():
    first_number = e.get()
    global f_num
    global math
    math = "DIV"
    f_num = int(first_number)
    e.delete(0, END)


def Equal():
    second_number = e.get()
    global s_num
    s_num = int(second_number)
    e.delete(0, END)
    if math == "ADD":
        e.insert(0, int(f_num + s_num))
    elif math == "SUB":
        e.insert(0, int(f_num - s_num))
    elif math == "MUL":
        e.insert(0, int(f_num * s_num))
    elif math == "DIV":
        e.insert(0, int(f_num / s_num))


zero = Button(root, text="0", command=lambda: enter(0), padx=40, pady=20)
one = Button(root, text="1", command=lambda: enter(1), padx=40, pady=20)
two = Button(root, text="2", command=lambda: enter(2), padx=40, pady=20)
three = Button(root, text="3", command=lambda: enter(3), padx=40, pady=20)
four = Button(root, text="4", command=lambda: enter(4), padx=40, pady=20)
five = Button(root, text="5", command=lambda: enter(5), padx=40, pady=20)
six = Button(root, text="6", command=lambda: enter(6), padx=40, pady=20)
seven = Button(root, text="7", command=lambda: enter(7), padx=40, pady=20)
eight = Button(root, text="8", command=lambda: enter(8), padx=40, pady=20)
nine = Button(root, text="9", command=lambda: enter(9), padx=40, pady=20)
add = Button(root, text="+", command=Add, padx=39, pady=20)
sub = Button(root, text="-", command=Sub, padx=41, pady=20)
mul = Button(root, text="*", command=Mul, padx=41, pady=20)
div = Button(root, text="/", command=Div, padx=41, pady=20)
equal = Button(root, text="=", command=Equal, padx=86.5, pady=20)
clear = Button(root, text="clear", command=Clear, padx=78, pady=20)


one.grid(row=3, column=0)
two.grid(row=3, column=1)
three.grid(row=3, column=2)
four.grid(row=2, column=0)
five.grid(row=2, column=1)
six.grid(row=2, column=2)
seven.grid(row=1, column=0)
eight.grid(row=1, column=1)
nine.grid(row=1, column=2)
zero.grid(row=4, column=0)
add.grid(row=5, column=0)
sub.grid(row=5, column=1)
mul.grid(row=5, column=2)
div.grid(row=6, column=0)
clear.grid(row=4, column=1, columnspan=2)
equal.grid(row=6, column=1, columnspan=2)

root.mainloop()
