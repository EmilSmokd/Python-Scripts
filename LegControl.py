#libreria arduino
from pyfirmata import Arduino, SERVO 
import time
#puerto de comunicacion con arduino
board = Arduino('COM3')

#Arduino config
board.digital[11].mode = SERVO

rojo = 5
verde = 4
azul = 3


class Servomotor:

  module = 'Servomotor'
  angle = 0
  status = 0
  
  def __init__(self, start, stop, increment):
    self.start = start
    self.stop = stop
    self.increment = increment

  def servoCycle(self):
    for angle in range(self.start, self.stop, self.increment):
      board.digital[11].write(angle)
      time.sleep(0.05)
    print('Log from: ', self.module)
    print('Successful cycle')
    return angle

  def getFlags(self):
    print('Log from: ', self.module)
    print('Flags retrieved:', self.flag1,' ', self.flag2)
    return self.flag1, self.flag2
  
  def setFlags(self, flag1, flag2):
    self.flag1 = flag1
    self.flag2 = flag2
    print('Log from: ', self.module)
    print('Flags set:', flag1,' ', flag2)

  def getStatus(self):
    print('Log from: ', self.module)
    print('Status memory:', self.status)
    return self.status
  
  def setStatus(self, status):
    self.status = status
    print('Log from: ', self.module)
    print('Status memory set:', status)

# Driver Code
# servo = Servomotor(0, 180, 1)
# servo.setFlags(1, 0)
# servo.getFlags()
# servo.setStatus(1)
# servo.getStatus()
# while servo.status == 1:
#   while True:
#     if servo.flag1 == 1 and servo.flag2 == 0:
#       servo = Servomotor(0, 180, 1)
#       servo.servoCycle()
#     servo.setFlags(0, 1)
#     servo.getFlags()
#     if servo.flag1 == 0 and servo.flag2 == 1:
#       servo = Servomotor(179, 0, -1)
#       servo.servoCycle()
#     servo.setFlags(1, 0)
#     servo.getFlags()

class Led:

  module = 'Led RGB'

  def __init__(self, status):
    self.status = status

  def runStatus(self):
    if self.status == 1:
      print('Log from: ', self.module)
      print('Service Running')
      board.digital[rojo].write(0)
      board.digital[verde].write(1)
      board.digital[azul].write(0)
    elif self.status == 0:
      print('Log from: ', self.module)
      print('Service stopped')
      board.digital[rojo].write(1)
      board.digital[verde].write(0)
      board.digital[azul].write(0)

# Driver Code
# while True:
#   indicador = Led(1)
#   indicador.runStatus()
#   time.sleep(0.05)
#   indicador = Led(0)
#   indicador.runStatus()
#   time.sleep(0.05)

