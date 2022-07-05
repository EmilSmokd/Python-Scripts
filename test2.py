from tkinter import *
from ServoControl import Servomotor
import time
# Dedos
menique = Servomotor( 3, 1)

def writeAngle1(angle):
  print(angle)
  angle = pinkyScl.get()
  menique.setAngle(angle)

app = Tk()
app.title('Protesis Robotica')
app.geometry('300x300')
app.resizable(False, False)

pinkyLbl = Label(text='Menique')
pinkyLbl.grid(row=0, column=4)
pinkyScl = Scale(app, from_=0, to=180, command=writeAngle1)
pinkyScl.grid(row=1, column=4)

app.mainloop()