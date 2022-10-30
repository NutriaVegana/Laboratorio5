#Jorge Arenas
#Diego Palma


from socket import *
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
    print("Recibo z2 de Cliente a servidor: 174")
    z2 = 174
    print("Calculo z = z2^x mod p")
    z = exponenciacion(z2, 3, p)
    print("El valor z comun es: ", z)


cipher = DES.new('12345678')
d_usuario = cipher.decrypt(c_usuario).strip()
d_password = cipher.decrypt(c_password).strip()
print ("El servidor descifra:")
print ("Usuario: " + d_usuario)
print ("Password: " + d_password)
f = open('mensajerecibido.txt','a')
f.write('\n' + d_password)
f.close()



direccionServidor= "localhost"
puertoServidor= 9099

#generamos un nuevo socket
socketServidor= socket(AF_INET, SOCK_STREAM)
#establecemos la conexion
socketServidor.bind( ( direccionServidor, puertoServidor))
socketServidor.listen()

while True:
    #establecemos la conexion
    socketConexion, addr = socketServidor.accept()
    print("Conectado con un cliente", addr)
    while True:
        #recibimos el mensaje del cliente
        mensajeRecibido= socketConexion.recv(4096).decode()
        print(mensajeRecibido)

        if mensajeRecibido== "Adios":
            break
        #mandamos mensaje al cliente
        socketConexion.send(input().encode())

    print("Descoonectado el cliente", addr)
    #cerramos conexion
    socketConexion.close()









