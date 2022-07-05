from tkinter import *
from ServoControl import Servomotor
from pyfirmata import Arduino, SERVO 
import time
# Dedos
menique = Servomotor( 3, 1)
anular  = Servomotor( 5, 2)
medio   = Servomotor( 6, 3)
indice  = Servomotor( 9, 4)
pulgar = Servomotor(10, 5)

def writeAngle1(angle):
  angle = pinkyScl.get()
  menique.setAngle(angle)

def writeAngle2(angle):
  angle = anularScl.get()
  anular.setAngle(angle)

def writeAngle3(angle):
  angle = medioScl.get()
  medio.setAngle(angle)

def writeAngle4(angle):
  angle = indiceScl.get()
  indice.setAngle(angle)

def writeAngle5(angle):
  angle = pulgarScl.get()
  pulgar.setAngle(angle)


app = Tk()
app.title('Protesis Robotica')
app.geometry('300x300')
app.resizable(False, False)

pulgarLbl = Label(text='Pulgar')
pulgarLbl.grid(row=0, column=0)
pulgarScl = Scale(app, from_=0, to=180, command=writeAngle5)
pulgarScl.grid(row=1, column=0)

indiceLbl = Label(text='Indice')
indiceLbl.grid(row=0, column=1)
indiceScl = Scale(app, from_=0, to=180, command=writeAngle4)
indiceScl.grid(row=1, column=1)

medioLbl = Label(text='Medio')
medioLbl.grid(row=0, column=2)
medioScl = Scale(app, from_=0, to=180, command=writeAngle3)
medioScl.grid(row=1, column=2)

anularLbl = Label(text='Anular')
anularLbl.grid(row=0, column=3)
anularScl = Scale(app, from_=0, to=180, command=writeAngle2)
anularScl.grid(row=1, column=3)

pinkyLbl = Label(text='Menique')
pinkyLbl.grid(row=0, column=4)
pinkyScl = Scale(app, from_=0, to=180, command=writeAngle1)
pinkyScl.grid(row=1, column=4)




app.mainloop()