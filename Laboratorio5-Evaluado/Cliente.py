#Jorge Arenas
#Diego Palma

from socket import *
import sys
from random import randint
from Crypto.Cipher import DES

def exponenciacion(n, x, p):
    z = 1
    y = n % p
    while (x > 0):
        if ((x % 2) == 0):  # Si b es par
            y = (y * y) % p
            x = x / 2
        else:  # Si b es impar
            z = (z * y) % p
            x = x - 1
    return z

if __name__ == '__main__':
    n = 50
    p = 461
    z1 = exponenciacion(n, 3, p)
    print("Mi z1 de cliente es: ", z1)
    print("")


usuario =int(input("ingrese su nombre:  "))
password = int(input("Contraseña de 8 caracteres: "))
# creamos el cifrador con DES
cipher = DES.new('12345678')
# ciframos usuario y password
c_usuario = cipher.encrypt(usuario)
c_password = cipher.encrypt(password)
# enviamos credenciales (a la pantalla en este caso)
print ("El cliente envia:")
print ("Usuario: " + c_usuario)
print ("Password: " + c_password)

f = open('mensajeentrada.txt','a')
f.write('\n' + c_password)
f.close()



IPServidor= "localhost"
puertoServidor= 9099
socketCliente= socket(AF_INET, SOCK_STREAM)
socketCliente.connect((IPServidor, puertoServidor))

while True:

    #escribimos el mensaje
    mensaje= input()
    if mensaje !="adios":

        #enciamos mensaje
        socketCliente.send(mensaje.encode())
        #recibimos mensaje
        respuesta= socketCliente.recv(4096).decode()
        print(respuesta)

    else:
        socketCliente.send(mensaje.encode())
        #cerramos socket
        socketCliente.close()
        sys.exit()

#a cliente alice 
#b server  bob




    
