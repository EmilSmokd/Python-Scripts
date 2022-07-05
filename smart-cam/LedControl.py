
rojo = 5
verde = 4
azul = 3


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