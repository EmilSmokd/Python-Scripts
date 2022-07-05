------------------------------------
def caminarTodo1():
  inicio1, fin = 50, 130
  while True:
    vec1 = [3, 6, 9, 11]
    obj1 = Servomotor(12, 2000)
    obj1.servoCycle4Patas(vec1,90, inicio1,-3)
    obj1.servoCycle4Patas(vec1, inicio1, fin, 3)
    obj1.servoCycle4Patas(vec1, fin, 90, -3)
-------------------------------------
  
----------------------------------------------------------------