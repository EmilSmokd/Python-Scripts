from tkinter import *
from ServoControl import Servomotor

###########
#Pines
p1 = Servomotor( 3, 1)
p2 = Servomotor( 5, 2)
p3 = Servomotor( 6, 3)
p4 = Servomotor( 9, 4)
p5 = Servomotor(10, 5)
p6 = Servomotor(11, 6)
patas = [ p1, p2, p3, p4, p5, p6 ]
############
#Funciones##
############
def servoCenter():
  for x in patas:
    x.setAngle(90)

def writeAngle1():
  angle = lbl_1_entry.get()
  p1.setAngle(angle)
  print(angle)
def writeAngle2():
  angle = lbl_2_entry.get()
  p2.setAngle(angle)
  print(angle)
def writeAngle3():
  angle = lbl_3_entry.get()
  p3.setAngle(angle)
  print(angle)
def writeAngle4():
  angle = lbl_4_entry.get()
  p4.setAngle(angle)
  print(angle)
def writeAngle5():
  angle = lbl_5_entry.get()
  p5.setAngle(angle)
  print(angle)
def writeAngle6():
  angle = lbl_6_entry.get()
  p6.setAngle(angle)
  print(angle)
############
##Interfaz##
############

app = Tk()
app.title("Servo Controller")
app.geometry('500x250')

lbl_1 = Label(text='Pata 1')
lbl_1.grid(row=0, column=0, padx=(5,5), pady=(25,5), sticky='w')
lbl_1_entry = Entry(app)
lbl_1_entry.grid(row=0, column=1, padx=(5,5), pady=(25,5), sticky='w')
lbl_1_btn = Button(app, text='set', command=writeAngle1)
lbl_1_btn.grid(row=0, column=2, padx=(10,30), pady=(25,5), sticky='w')

lbl_2 = Label(text='Pata 2')
lbl_2.grid(row=0, column=3, padx=(5,5), pady=(25,5), sticky='w')
lbl_2_entry = Entry(app)
lbl_2_entry.grid(row=0, column=4, padx=(5,5), pady=(25,5), sticky='w')
lbl_2_btn = Button(app, text='set', command=writeAngle2)
lbl_2_btn.grid(row=0, column=5, padx=(10,30), pady=(25,5), sticky='w')

lbl_3 = Label(text='Pata 3')
lbl_3.grid(row=1, column=0, padx=(5,5), pady=(25,5), sticky='w')
lbl_3_entry = Entry(app)
lbl_3_entry.grid(row=1, column=1, padx=(5,5), pady=(25,5), sticky='w')
lbl_3_btn = Button(app, text='set', command=writeAngle3)
lbl_3_btn.grid(row=1, column=2, padx=(10,30), pady=(25,5), sticky='w')

lbl_4 = Label(text='Pata 4')
lbl_4.grid(row=1, column=3, padx=(5,5), pady=(25,5), sticky='w')
lbl_4_entry = Entry(app)
lbl_4_entry.grid(row=1, column=4, padx=(5,5), pady=(25,5), sticky='w')
lbl_4_btn = Button(app, text='set', command=writeAngle4)
lbl_4_btn.grid(row=1, column=5, padx=(10,30), pady=(25,5), sticky='w')

lbl_5 = Label(text='Pata 5')
lbl_5.grid(row=2, column=0, padx=(5,5), pady=(25,5), sticky='w')
lbl_5_entry = Entry(app)
lbl_5_entry.grid(row=2, column=1, padx=(5,5), pady=(25,5), sticky='w')
lbl_5_btn = Button(app, text='set', command=writeAngle5)
lbl_5_btn.grid(row=2, column=2, padx=(10,30), pady=(25,5), sticky='w')

lbl_6 = Label(text='Pata 6')
lbl_6.grid(row=2, column=3, padx=(5,5), pady=(25,5), sticky='w')
lbl_6_entry = Entry(app)
lbl_6_entry.grid(row=2, column=4, padx=(5,5), pady=(25,5), sticky='w')
lbl_6_btn = Button(app, text='set', command=writeAngle6)
lbl_6_btn.grid(row=2, column=5, padx=(10,30), pady=(25,5), sticky='w')

btnAvanzar = Button(app, text="Avance")
btnAvanzar.grid(row=3, column=0)
btnRetroceso = Button(app, text="Retroceso")
btnRetroceso.grid(row=3, column=1)
btnDetener = Button(app, text="Detener")
btnDetener.grid(row=3, column=2)


servoCenter()
app.mainloop() 