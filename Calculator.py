#Calculator

## Importing library
from tkinter import*

## creating functions


def button_input(number):
    """This Function helps in adding text in screen of calculator"""
    global inputs
    inputs = inputs+str(number)
    text_Input.set(inputs)

def clear_input():
    """ This function helps in clear the text from screen """
    global inputs
    inputs = ""
    text_Input.set(inputs)
    
def delete_last():
    """ This function helps in delete the last element of the text on screen """
    global inputs
    inputs = inputs[:-1]
    text_Input.set(inputs)
    
def equality():
    """ This function helps in calculation """
    global inputs
    if "÷" in inputs:
        inputs =inputs.replace("÷","/")
    if "^" in inputs:
        inputs=inputs.replace("^","**")
    if "x" in inputs:
        inputs=inputs.replace("x","*")
    try:
        ans = str(eval(inputs))
        text_Input.set(ans)
        inputs=ans
    except:
        text_Input.set("Asnwer Not define")
        inputs= ""
        
    
    
        
    
""" Now This is our main function"""   
calculator = Tk()
calculator.title("Calculator")
inputs = ""


text_Input = StringVar()

""" creating input window"""

textdisplay = Entry(calculator,font = ("arial",20,"bold"),textvariable = text_Input,bd = 30,cursor="tcross" ,xscrollcommand=10,
                    bg="Steelblue1", justify = 'right').grid(columnspan = 4)

"""creating different buttons"""

_7 = Button(calculator, padx =16,bd =6, fg = "black",font=('arial', 20,'bold'),bg="snow",
           text='7',command=lambda:button_input(7)).grid(row=1,column= 0)
_8 = Button(calculator, padx =16,bd =5, fg = "black",font=('arial', 20,'bold'),bg="snow",
           text='8',command=lambda:button_input(8)).grid(row=1,column= 1)
_9 = Button(calculator, padx =16,bd =5, fg = "black",font=('arial', 20,'bold'),bg="snow",
           text='9',command=lambda:button_input(9)).grid(row=1,column= 2)
_clear = Button(calculator, padx =14,bd =5, fg = "black",font=('arial', 20,'bold'),bg="snow",
           text='C',command = lambda:clear_input()).grid(row=1,column= 3)
_4 = Button(calculator, padx =16,bd =5, fg = "black",font=('arial', 20,'bold'),bg="snow",
           text='4',command=lambda:button_input(4)).grid(row=2,column= 0)
_5 = Button(calculator, padx =16,bd =5, fg = "black",font=('arial', 20,'bold'),bg="snow",
           text='5',command=lambda:button_input(5)).grid(row=2,column= 1)
_6 = Button(calculator, padx =16,bd =5, fg = "black",font=('arial', 20,'bold'),bg="snow",
           text='6',command=lambda:button_input(6)).grid(row=2,column= 2)
_dev = Button(calculator, padx =16,bd =5, fg = "black",font=('arial', 20,'bold'),bg="Royalblue1",
           text='÷',command=lambda:button_input("÷")).grid(row=2,column= 3)
_1 = Button(calculator, padx =16,bd =5, fg = "black",font=('arial', 20,'bold'),bg="snow",
           text='1',command=lambda:button_input(1)).grid(row=3,column= 0)
_2 = Button(calculator, padx =16,bd =5, fg = "black",font=('arial', 20,'bold'),bg="snow",
           text='2',command=lambda:button_input(2)).grid(row=3,column= 1)
_3 = Button(calculator, padx =16,bd =5, fg = "black",font=('arial', 20,'bold'),bg="snow",
           text='3',command=lambda:button_input(3)).grid(row=3,column= 2)
_mul = Button(calculator, padx =17,bd =5, fg = "black",font=('arial', 19,'bold'),bg="Royalblue1",
           text='X',command=lambda:button_input("x")).grid(row=3,column= 3)
_dot = Button(calculator, padx =19,bd =5, fg = "black",font=('arial', 20,'bold'),bg="snow",
           text='.',command=lambda:button_input(".")).grid(row=4,column= 0)
_zero = Button(calculator, padx =16,bd =5, fg = "black",font=('arial', 20,'bold'),bg="snow",
           text='0',command=lambda:button_input(0)).grid(row=4,column= 1)
_2zero = Button(calculator, padx =12,bd =5, fg = "black",font=('arial', 18,'bold'),bg="snow",
           text='00',command=lambda:button_input("00")).grid(row=4,column= 2)
_plus = Button(calculator, padx =16,bd =5, fg = "black",font=('arial', 20,'bold'),bg="Royalblue1",
           text='+',command=lambda:button_input("+")).grid(row=4,column= 3)
_del = Button(calculator, padx =8,bd =5, fg = "black",font=('arial', 20),bg="Royalblue1",
           text="⌫",command=lambda:delete_last()).grid(row=5,column= 0)
_squre = Button(calculator, padx =12,bd =5, fg = "black",font=('arial', 20,'bold'),bg="Royalblue1",
           text='xʸ',command=lambda:button_input("^")).grid(row=5,column= 1)
_neg = Button(calculator, padx =19,bd =5, fg = "black",font=('arial', 20,'bold'),bg="Royalblue1",
           text='-',command=lambda:button_input("-")).grid(row=5,column= 2)
_equal = Button(calculator, padx =16,bd =5, fg = "black",font=('arial', 20,'bold'),bg="Royalblue1",
           text='=',command=lambda:equality()).grid(row=5,column= 3)


calculator.mainloop()
