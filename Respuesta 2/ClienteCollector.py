from xmlrpc.client import ServerProxy
import msvcrt

s = ServerProxy('http://localhost:20064', allow_none=True)

while True:
    print('')
    print('Garbage Collector')
    print('---------------------------------')
    print("|press (+) to run         |")
    print('---------------------------------')

    operador = input('get into ->  ')

    if s.isValid(operador):

        print(s.calc(operador))
    else:
        print('invalid key')
    
    print('')
    print("Press 'x' to exit...")
    print("Press any key to continue...")
    
    key = msvcrt.getwch()
    if key == 'x':
        exit()