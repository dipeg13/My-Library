from tkinter import *
import math

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0,column=0,columnspan=7,padx=10,pady=10)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_equal():
    if flag == "addition":
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num + float(second_number))
    if flag == "subtraction":
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num - float(second_number))
    if flag == "multiplication":
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num * float(second_number))
    if flag == "division":
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num / float(second_number))
    if flag == "square root":
        e.insert(0, math.sqrt(f_num))
    if flag == "factorial":
        e.insert(0, math.factorial(f_num))
    if flag == "ln":
        e.insert(0, math.log(f_num))
    if flag == "x^3":
        e.insert(0, f_num ** 3)
    if flag == "sin":
        e.insert(0, math.sin(f_num))
    if flag == "e^x":
        e.insert(0, math.exp(f_num))
    if flag == "cos":
        e.insert(0, math.cos(f_num))
    if flag == "tan":
        e.insert(0, math.tan(f_num))
    if flag == "x^y":
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num ** float(second_number))
    if flag == "cot":
        e.insert(0, math.cot(f_num))
    if flag == "sinh":
        e.insert(0, math.sinh(f_num))
    if flag == "cosh":
        e.insert(0, math.cosh(f_num))
    if flag == "tanh":
        e.insert(0, math.tanh(f_num))
    if flag == "pi^x":
        e.insert(0, math.pi ** f_num)
    if flag == "arctan":
        e.insert(0, math.atan(f_num))

def button_add():
    first_number = e.get()
    global f_num
    global flag
    flag = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global flag
    flag = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global flag
    flag = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global flag
    flag = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_square_root():
    first_number = e.get()
    global f_num
    global flag
    flag = "square root"
    f_num = float(first_number)
    e.delete(0, END)

def button_factorial():
    first_number = e.get()
    global f_num
    global flag
    flag = "factorial"
    f_num = float(first_number)
    e.delete(0, END)

def button_ln():
    first_number = e.get()
    global f_num
    global flag
    flag = "ln"
    f_num = float(first_number)
    e.delete(0, END)

def button_cubic_power():
    first_number = e.get()
    global f_num
    global flag
    flag = "x^3"
    f_num = float(first_number)
    e.delete(0, END)

def button_sin():
    first_number = e.get()
    global f_num
    global flag
    flag = "sin"
    f_num = float(first_number)
    e.delete(0, END)

def button_e_powered_x():
    first_number = e.get()
    global f_num
    global flag
    flag = "e^x"
    f_num = float(first_number)
    e.delete(0, END)

def button_cos():
    first_number = e.get()
    global f_num
    global flag
    flag = "cos"
    f_num = float(first_number)
    e.delete(0, END)

def button_tan():
    first_number = e.get()
    global f_num
    global flag
    flag = "tan"
    f_num = float(first_number)
    e.delete(0, END)

def button_x_powered_y():
    first_number = e.get()
    global f_num
    global flag
    flag = "x^y"
    f_num = float(first_number)
    e.delete(0, END)

def button_cot():
    first_number = e.get()
    global f_num
    global flag
    flag = "cot"
    f_num = float(first_number)
    e.delete(0, END)

def button_sinh():
    first_number = e.get()
    global f_num
    global flag
    flag = "sinh"
    f_num = float(first_number)
    e.delete(0, END)

def button_pi_powered_x():
    first_number = e.get()
    global f_num
    global flag
    flag = "pi^x"
    f_num = float(first_number)
    e.delete(0, END)

def button_cosh():
    first_number = e.get()
    global f_num
    global flag
    flag = "cosh"
    f_num = float(first_number)
    e.delete(0, END)

def button_tanh():
    first_number = e.get()
    global f_num
    global flag
    flag = "tanh"
    f_num = float(first_number)
    e.delete(0, END)

def button_arctan():
    first_number = e.get()
    global f_num
    global flag
    flag = "arctan"
    f_num = float(first_number)
    e.delete(0, END)



button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)
button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_clear = Button(root, text="Clear", padx=40, pady=160, command=button_clear)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)
button_square_root = Button(root, text="sqrt", padx=40, pady=20, command=button_square_root)
button_cubic_power = Button(root, text="x^3", padx=40, pady=20, command=button_cubic_power)
button_cos = Button(root, text="cos(x)", padx=40, pady=20, command=button_cos)
button_cot = Button(root, text="cot(x)", padx=40, pady=20, command=button_cot)
button_cosh = Button(root, text="cosh(x)", padx=40, pady=20, command=button_cosh)
button_factorial = Button(root, text="x!", padx=40, pady=20, command=button_factorial)
button_sin = Button(root, text="sin(x)", padx=40, pady=20, command=button_sin)
button_tan = Button(root, text="tan(x)", padx=40, pady=20, command=button_tan)
button_sinh = Button(root, text="sinh(x)", padx=40, pady=20, command=button_sinh)
button_tanh = Button(root, text="tanh(x)", padx=40, pady=20, command=button_tanh)
button_ln = Button(root, text="ln(x)", padx=40, pady=20, command=button_ln)
button_e_powered_x = Button(root, text="e^x", padx=40, pady=20, command=button_e_powered_x)
button_x_powered_y = Button(root, text="x^y", padx=40, pady=20, command=button_x_powered_y)
button_pi_powered_x = Button(root, text="π^x", padx=40, pady=20, command=button_pi_powered_x)
button_arctan = Button(root, text="arctan(x)", padx=40, pady=20, command=button_arctan)



button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

button_subtract.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)

button_clear.grid(row=1, column=3, rowspan=5)

button_square_root.grid(row=1, column=4)
button_factorial.grid(row=1, column=5)
button_ln.grid(row=1, column=6)

button_cubic_power.grid(row=2, column=4)
button_sin.grid(row=2, column=5)
button_e_powered_x.grid(row=2, column=6)

button_cos.grid(row=3, column=4)
button_tan.grid(row=3, column=5)
button_x_powered_y.grid(row=3, column=6)

button_cot.grid(row=4, column=4)
button_sinh.grid(row=4, column=5)
button_pi_powered_x.grid(row=4, column=6)

button_cosh.grid(row=5, column=4)
button_tanh.grid(row=5, column=5)
button_arctan.grid(row=5, column=6)


root.resizable(width=False, height=False)
