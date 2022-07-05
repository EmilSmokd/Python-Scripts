from fileinput import close
from tkinter import *
from PIL import Image, ImageTk
import cv2

# app = Tk()
# app.title("Smart cam")
# app.configure(bg="#7195f0")




# serviceButton = Button(app, text='Start Service', command=lambda:[toggleText(), toggleLed()])
# serviceButton.pack()
cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()

  cv2.imshow('frame', frame)
  if cv2.waitKey(1) & 0xffFF ==ord('q'):
    break
cap.release()

# btnIniciar = Button(app, text="Iniciar", width=45, command=showVideo)
# btnIniciar.grid(column=0, row=0, padx=5, pady=5)

# btnFinalizar = Button(app, text="Finalizar", width=45, command=closeVideo)
# btnFinalizar.grid(column=1, row=0, padx=5, pady=5)

# lblVideo = Label(app)
# lblVideo.grid(column=0, row=1, columnspan=2)



# app.mainloop()