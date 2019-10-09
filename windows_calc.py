import tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("250x400+300+200")  # height X width + left + top +
root.resizable(0, 0)  # boolean variables not toe resizable
root.title("My calculator")

# we wil decxlare a label that wil display on the side with south
# east of the windows that is the anchor property will be used for this
# the anchor property wiil suggest you where the label sholud display

var = ''
operator = ""
a = 0
multi_add = []


def btn_1_clicked():
    global var  # the global keyword is use to change the value of local keyword
    global multi_add
    var = var + "1"
    multi_add.append(var)
    print(multi_add)
    print(var)
    data.set(var)


def btn_2_clicked():
    global var
    var = var + "2"
    data.set(var)


def btn_3_clicked():
    global var
    var = var + "3"
    data.set(var)


def btn_4_clicked():
    global var
    var = var + "4"
    data.set(var)


def btn_5_clicked():
    global var
    var = var + "5"
    data.set(var)


def btn_6_clicked():
    global var
    var = var + "6"
    data.set(var)


def btn_7_clicked():
    global var
    var = var + "7"
    data.set(var)


def btn_8_clicked():
    global var
    var = var + "8"
    data.set(var)


def btn_9_clicked():
    global var
    var = var + "9"
    data.set(var)


def btn_0_clicked():
    global var
    var = var + "0"
    data.set(var)


############## *********** operators *************** ###############################
def btn_plus_clicked():
    global multi_add
    global a  # a=0
    global operator  # operators=''
    global var  # var='1'
    a = int(var)  # typcast var as integer and store in a=1
    print(a)
    operator = "+"
    print(operator)  # operators=+
    var = var + "+"  # 1+
    multi_add.append(var)
    print(multi_add)
    print(var)
    data.set(var)


def btn_minus_clicked():
    global a
    global operator
    global var
    a = int(var)
    operator = "-"
    var = var + "-"
    data.set(var)


def btn_mul_clicked():
    global a
    global operator
    global var
    a = int(var)
    operator = "*"
    var = var + "*"
    data.set(var)


def btn_div_clicked():
    global a
    global operator
    global var
    a = int(var)
    operator = "/"
    var = var + "/"
    data.set(var)


def btn_C_clicked():
    global a
    global operator
    global var
    a = 0
    var = ""
    operator = ""
    data.set(var)


def btn_equal_clicked():
    sum_list = []
    global a
    global operator
    global var
    global multi_add
    var2 = var
    if operator == "+":
        for i in range(len(multi_add)):
            print("sum_list")
            sum_list.append(multi_add[i])
            print(sum_list)

        x = int((var2.split("+")[1]))
        c = a + x
        data.set(c)
        var = str(c)

    elif operator == "-":
        x = int((var2.split("-")[1]))
        c = a - x
        data.set(c)
        var = str(c)

    elif operator == "*":
        x = int((var2.split("*")[1]))
        c = a * x
        data.set(c)
        var = str(c)

    elif operator == "/":
        x = int((var2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "math Error")
            a = 0
            var = ""
            data.set(var)
        else:
            c = a / x
            d = round(c, 4)

            data.set(d)
            var = str(d)


data = StringVar()  # variables for our label whichis actualy atinker variables

lable = Label(
    root,
    text='lable',
    anchor='se'
    , bg="#282C34",
    font=("Verdana", 22),
    textvariable=data,
    fg='#ffffff'
)

# lable.config(fg="#ffffff")
lable.pack(expand=True, fill='both')
""" NOW MAKE A FRAME WHICH WILL ACT AS A ROW FOR OUR
CALC AND JUST ATTACHE IT WITH A ROOT ELEMEN"""

btn_row1 = Frame(root, bg="#ffffff")
btn_row2 = Frame(root)
btn_row3 = Frame(root)
btn_row4 = Frame(root)
# now decide the Frame geometry THIS PACK geometry CAN BE USED TO
# OVERLAP THE BUTTON WITH LABELS/TEXT
""" NOw JUST USE OF PACK geometry """

btn_row1.pack(expand=True, fill='both')
btn_row2.pack(expand=True, fill="both")
btn_row3.pack(expand=True, fill="both")
btn_row4.pack(expand=True, fill="both")

# now wil create button for our calculator

btn1 = Button(
    btn_row1,  # this the parent ELEMENT for this button
    text="1",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_1_clicked
)

btn2 = Button(
    btn_row1,  # this the parent ELEMEN for this button
    text="2",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_2_clicked
)

btn3 = Button(
    btn_row1,  # this the parent ELEMEN for this button
    text="3",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_3_clicked
)

btn4 = Button(
    btn_row1,  # this the parent ELEMEN for this button
    text="+",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_plus_clicked

)
four_btn_in_one_row = (btn1, btn2, btn3, btn4)
"""one frame will consist of a four button """
# now just make this button to pack inside the frame
# btn1.pack(side=LEFT,expand=True,fill='both')# the new button wil be
# #arrange to the left side of this button
# btn2.pack(side=LEFT,expand=True,fill='both')#
for i in four_btn_in_one_row:
    i.pack(side=LEFT, expand=True, fill='both')
"""now the arguments
1.expand the my frame in both direction automatically if thers is a space
left to be expand
2. the tow fram will expand automatically in both direction to take up their plcaes
 """
# btn3.pack(side=LEFT,expand=True,fill='both')#
# btn4.pack(side=LEFT,expand=True,fill='both')#


# now create a button 3 rows
# for i in range(5,9):
#     btn="btn{}".format(i)
#     btn=Button(btn_row2,text=i,font=("Verdana",22))
#     btn.pack(side=LEFT,expand=True,fill='both')
#     print(btn)


btn5 = Button(
    btn_row2,  # this the parent ELEMEN for this button
    text="4",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_4_clicked
)

btn6 = Button(
    btn_row2,  # this the parent ELEMEN for this button
    text="5",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_5_clicked
)

btn7 = Button(
    btn_row2,  # this the parent ELEMEN for this button
    text="6",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_6_clicked
)

btn8 = Button(
    btn_row2,  # this the parent ELEMEN for this button
    text="-",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_minus_clicked
)
btn5.pack(side=LEFT, expand=True, fill='both')
btn6.pack(side=LEFT, expand=True, fill='both')
btn7.pack(side=LEFT, expand=True, fill='both')
btn8.pack(side=LEFT, expand=True, fill='both')

btn9 = Button(
    btn_row3,  # this the parent ELEMEN for this button
    text="7",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_7_clicked
)

btn10 = Button(
    btn_row3,  # this the parent ELEMEN for this button
    text="8",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_8_clicked
)

btn11 = Button(
    btn_row3,  # this the parent ELEMEN for this button
    text="9",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_9_clicked
)

btn12 = Button(
    btn_row3,  # this the parent ELEMEN for this button
    text="*",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_mul_clicked
)
btn9.pack(side=LEFT, expand=True, fill='both')
btn10.pack(side=LEFT, expand=True, fill='both')
btn11.pack(side=LEFT, expand=True, fill='both')
btn12.pack(side=LEFT, expand=True, fill='both')

btn13 = Button(
    btn_row4,  # this the parent ELEMEN for this button
    text="C",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_C_clicked
)

btn14 = Button(
    btn_row4,  # this the parent ELEMEN for this button
    text="0",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_0_clicked
)

btn15 = Button(
    btn_row4,  # this the parent ELEMEN for this button
    text="=",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_equal_clicked
)

btn16 = Button(
    btn_row4,  # this the parent ELEMEN for this button
    text="/",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_div_clicked
)

btn13.pack(side=LEFT, expand=True, fill='both')
btn14.pack(side=LEFT, expand=True, fill='both')
btn15.pack(side=LEFT, expand=True, fill='both')
btn16.pack(side=LEFT, expand=True, fill='both')

root.mainloop()
