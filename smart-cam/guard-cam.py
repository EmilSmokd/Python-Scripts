import time
from LegControl import Servomotor, Led
from threading import Thread
import cv2
import numpy as np

def servoInstance():
  servo = Servomotor(0, 180, 1)
  servo.setFlags(1, 0)
  servo.getFlags()
  time.sleep(0.05)
  while True:
    if servo.flag1 == 1 and servo.flag2 == 0:
      servo = Servomotor(0, 180, 1)
      servo.servoCycle()
    servo.setFlags(0, 1)
    servo.getFlags()
    if servo.flag1 == 0 and servo.flag2 == 1:
      servo = Servomotor(179, 0, -1)
      servo.servoCycle()
    servo.setFlags(1, 0)
    servo.getFlags()

def camInstance():
  
  url = 'C:/opencv/haarcascades/'
  face_cascade = cv2.CascadeClassifier(url + 'haarcascade_frontalface_alt.xml')
  eyes_detection = cv2.CascadeClassifier(url + 'haarcascade_eye.xml')
  mouth_detection = cv2.CascadeClassifier(url + 'haarcascade_mcs_mouth.xml')

  video = cv2.VideoCapture(0)

  while video.isOpened():
      ret, frame = video.read()
      if frame is not None:
          gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
          face = face_cascade.detectMultiScale(gray, 1.35, 1)
          for (x, y, w, h) in face:
              cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
              roi_gray = gray[y:y + h, x:x + w]
              roi_color = frame[y:y + h, x:x + w]
              eyes = eyes_detection.detectMultiScale(roi_gray,1.3,2)
              mouths = mouth_detection.detectMultiScale(roi_gray,1.2,10)
              for (ex, ey, ew, eh) in eyes:
                  cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
              for(ex, ey, ew, eh) in mouths:
                  cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)
          cv2.imshow('Video', frame)
      if cv2.waitKey(1) & 0xFF == ord('q'):
          break 

  video.release()
  cv2.destroyAllWindows()


def ledInstance():
  indicador = Led(1)
  indicador.runStatus()



camThread = Thread(target=camInstance)
servoThread = Thread(target=servoInstance)
ledThread = Thread(target=ledInstance)

camThread.start()
servoThread.start()
ledThread.start()

camThread._stop()
servoThread._stop()
ledThread._stop()