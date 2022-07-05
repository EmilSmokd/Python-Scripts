# from pyfirmata import Arduino, SERVO 
# from LegControl import Servomotor
from time import sleep, perf_counter
import sys
import threading
from threading import Thread
###############
###Variables###
###############
menu_options = {
  1: 'Establecer angulo',
  2: 'Avance',
  3: 'Retroceso',
  4: 'Opcion 4',
  5: 'Salir'
}

flagAvance = 0
flagRetroceso = 0
flagDetener = 0
flagSalir = 0

###############
###Funciones###
###############
def print_menu():
  for key in menu_options.keys():
    print (key, '--', menu_options[key])

def option1():
  print('Handle option \'Option 1\'')

def option2():
     print('Handle option \'Option 2\'')

def option3():
     print('Handle option \'Option 3\'')
###############
####Testing####
###############
def task(id):
    print(f'Starting the task {id}...')
    sleep(1)
    print(f'The task {id} completed')
###############
##-Triggers-###
###############
def flag1():
  while True:
    # walkThread = Thread(print('Avanzando'))
###############
###Main Loop###
###############
if __name__=='__main__':
    while(True):
        print_menu()
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')