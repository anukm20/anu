from tkinter import *
expression=""
def press(num):
    global expression
    expression=expression+str(num)
    input_text.set(expression)
def btnclr():
    global expression
    expression=""
    input_text.set("")
def btneql():
    global expression
    result=str(eval(expression))
    input_text.set(result)
    expression=""
    expression=""
    input_text=StringVar()
    frame=Frame(calc,width=320,height=52,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=2)
    frame.pack(side=TOP)
    

calc=Tk()
calc.title("calculator")


btn1=Button(calc,text='1',fg='white',bg='gray')
btn1.grid(row=2,column=0)
btn2=Button(calc,text='2',fg='white',bg='gray')
btn2.grid(row=2,column=1)
btn3=Button(calc,text='3',fg='white',bg='gray')
btn3.grid(row=2,column=2)
btn4=Button(calc,text='4',fg='white',bg='gray')
btn4.grid(row=3,column=0)
btn5=Button(calc,text='5',fg='white',bg='gray')
btn5.grid(row=3,column=1)
btn6=Button(calc,text='6',fg='white',bg='gray')
btn6.grid(row=3,column=2)
btn7=Button(calc,text='7',fg='white',bg='gray')
btn7.grid(row=4,column=0)
btn8=Button(calc,text='8',fg='white',bg='gray')
btn8.grid(row=4,column=1)
btn9=Button(calc,text='9',fg='white',bg='gray')
btn9.grid(row=4,column=2)
btn0=Button(calc,text='0',fg='white',bg='gray')
btn0.grid(row=5,column=0)
pls=Button(calc,text='+',fg='white',bg='gray')
pls.grid(row=5,column=3)
mins=Button(calc,text='-',fg='white',bg='gray')
mins.grid(row=3,column=3)
mul=Button(calc,text='*',fg='white',bg='gray')
mul.grid(row=4,column=3)
div=Button(calc,text='/',fg='white',bg='gray')
div.grid(row=2,column=3)
eql=Button(calc,text='=',fg='white',bg='gray')
eql.grid(row=5,column=2)
clr=Button(calc,text='clr',fg='white',bg='gray')
clr.grid(row=5,column=1)
decim=Button(calc,text='.',fg='white',bg='gray')
decim.grid(row=6,column=0)
calc.mainloop()