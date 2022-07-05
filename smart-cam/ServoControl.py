 #libreria arduino
from numpy import angle
from pyfirmata import Arduino, SERVO 
import time
#puerto de comunicacion con arduino
board = Arduino('COM3')

#Arduino config
pin = 0
board.digital[pin].mode = SERVO

class Servomotor:

  module = 'Servomotor'
  angle = 0
  status = 0
  
  def __init__(self, number, pin):
    self.number = number
    self.pin = pin

  def mapCycle(self, start, stop, increment):
    self.start = start
    self.stop = stop
    self.increment = increment

  def servoCycle(self):
    for angle in range(self.start, self.stop, self.increment):
      board.digital[self.pin].write(angle)
      time.sleep(0.05)
    print('Log from: ', self.module)
    print('Successful cycle')
    return angle

  def setAngle(self, angle):
    self.angle = angle
    board.digital[self.pin].write(angle)
    time.sleep(0.05)
    print('Log from: ', self.module, ' memory')
    print('Angle memory set:', angle)

  def getAngle(self):
    print('Log from: ', self.module, ' memory')
    print('Angle memory:', self.angle)
    return angle
    
  def setFlags(self, flag1, flag2):
    self.flag1 = flag1
    self.flag2 = flag2
    print('Log from: ', self.module)
    print('Flags set:', flag1,' ', flag2)

  def getFlags(self):
    print('Log from: ', self.module)
    print('Flags retrieved:', self.flag1,' ', self.flag2)
    return self.flag1, self.flag2
  
  def setStatus(self, status):
    self.status = status
    print('Log from: ', self.module, ' memory')
    print('Status memory set:', status, ' memory')
  
  def getStatus(self):
    print('Log from: ', self.module)
    print('Status memory:', self.status)
    return self.status

##############################
# Memory driver code
# p1 = Servomotor('pata 1', 1)
# while True:
#   p1.setAngle(180)
#   time.sleep(0.3)
#   p1.setAngle(90)
#   time.sleep(0.3)
#   p1.setAngle(0)
#   time.sleep(0.3)  
###############################  
# Servomotor cycle driver code
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

# class Led:

#   module = 'Led RGB'

#   def __init__(self, status):
#     self.status = status

#   def runStatus(self):
#     if self.status == 1:
#       print('Log from: ', self.module)
#       print('Service Running')
#       board.digital[rojo].write(0)
#       board.digital[verde].write(1)
#       board.digital[azul].write(0)
#     elif self.status == 0:
#       print('Log from: ', self.module)
#       print('Service stopped')
#       board.digital[rojo].write(1)
#       board.digital[verde].write(0)
#       board.digital[azul].write(0)

# Driver Code
# while True:
#   indicador = Led(1)
#   indicador.runStatus()
#   time.sleep(0.05)
#   indicador = Led(0)
#   indicador.runStatus()
#   time.sleep(0.05)

# class angleMemory:
#   module = 'Angle Memory'

#   def __init__(self, leg):
#     self.leg = leg

#   def getAngle()
    
  