from tkinter import *
calc=Tk()
calc.geometry("312x324")
calc.resizable(0,0)
calc.title("Calculator")
def btnclk(item):
    global expression
    expression=expression+str(item)
    input.set(expression)
def btnclr():
    global expression
    expression=""
    input.set("")
def btneql():
    global expression
    result=str(eval(expression))
    input.set(result)
    expression=""
    expression=""
    input=StringVar()
    frame=Frame(calc,width=320,height=52,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=2)
    frame.pack(side=TOP)
    input_field=Entry(frame,font=('aria',18,'bold'),textvariable=input,width=50,bg="#eee",bd=0,justify=RIGHT)
    input_field.grid(row=0,column=0)
    input_field.pack(ipady=10)
    btns_frame=Frame(calc,width=312,height=272.5,bg="gray")
    btns_frame.pack()
    
clr=Button(Frame,text='clr',fg='white',width=32,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:btnclr()).grid(row=0,column=o,columnspan=3,padx=1,pady=1)
btn1.grid(row=2,column=0)
btn2=Button(calc,text='2',fg='white',bg='gray',command=lambda:btnclk(2),height=1,width=7)
btn2.grid(row=2,column=1)
btn3=Button(calc,text='3',fg='white',bg='gray',command=lambda:btnclk(3),height=1,width=7)
btn3.grid(row=2,column=2)
btn4=Button(calc,text='4',fg='white',bg='gray',command=lambda:btnclk(4),height=1,width=7)
btn4.grid(row=3,column=0)
btn5=Button(calc,text='5',fg='white',bg='gray',command=lambda:btnclk(5),height=1,width=7)
btn5.grid(row=3,column=1)
btn6=Button(calc,text='6',fg='white',bg='gray',command=lambda:btnclk(6),height=1,width=7)
btn6.grid(row=3,column=2)
btn7=Button(calc,text='7',fg='white',bg='gray',command=lambda:btnclk(7),height=1,width=7)
btn7.grid(row=4,column=0)
btn8=Button(calc,text='8',fg='white',bg='gray',command=lambda:btnclk(8),height=1,width=7)
btn8.grid(row=4,column=1)
btn9=Button(calc,text='9',fg='white',bg='gray',command=lambda:btnclk(9),height=1,width=7)
btn9.grid(row=4,column=2)
btn0=Button(calc,text='0',fg='white',bg='gray',command=lambda:btnclk(0),height=1,width=7)
btn0.grid(row=5,column=0)
pls=Button(calc,text='+',fg='white',bg='gray',command=lambda:btnclk("+"),height=1,width=7)
pls.grid(row=5,column=3)
mins=Button(calc,text='-',fg='white',bg='gray',command=lambda:btnclk("-"),height=1,width=7)
mins.grid(row=3,column=3)
mul=Button(calc,text='*',fg='white',bg='gray',command=lambda:btnclk("*"),height=1,width=7)
mul.grid(row=4,column=3)
div=Button(calc,text='/',fg='white',bg='gray',command=lambda:btnclk("/"),height=1,width=7)
div.grid(row=2,column=3)
eql=Button(calc,text='=',fg='white',bg='gray',command=btnclk,height=1,width=7)
eql.grid(row=5,column=2)
clr=Button(calc,text='clr',fg='white',bg='gray',command=btnclr,height=1,width=7)
clr.grid(row=5,column=1)
decim=Button(calc,text='.',fg='white',bg='gray',command=lambda:btnclk('.'),height=1,width=7)
decim.grid(row=6,column=0)
calc.mainloop()
    