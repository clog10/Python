
# Sockets

# Los programas utilizan sockets para comunicarse con otros programas, 
# que pueden estar situados en computadoras distintas.

# Un socket queda definido por la dirección IP de la máquina, el puerto 
# en el que escucha, y el protocolo que utiliza.
# 
# Los tipos y funciones necesarios para trabajar con sockets se encuentran en 
# Python en el módulo socket, como no podría ser de otra forma. 
# Los sockets se clasifican en sockets de flujo (socket.SOCK_STREAM) o sockets
# de datagramas (socket.SOCK_DGRAM) dependiendo de si el ser-vicio utiliza TCP, 
# que es orientado a conexión y fiable, o UDP, respec-tivamente. En este capítulo 
# sólo cubriremos los sockets de flujo, que cubren un 90% de las necesidades comunes.

# Para crear un socket se utiliza el constructor socket.socket() que puede tomar como 
# parámetros opcionales la familia, el tipo y el protocolo. Por defecto se utiliza la 
# familia AF_INET y el tipo SOCK_STREAM.

socket_s = socket.socket()

# Tenemos ahora que indicar en qué puerto se va a mantener a la escucha nuestro servidor 
# utilizando el método bind. Para sockets IP, como es nuestro caso, el argumento de bind
# es una tupla que contiene el host y el puerto. El host se puede dejar vacío, indicando 
# al método que puede utilizar cualquier nombre que esté disponible.

socket_s.bind(("localhost", 9999))

# Por último utilizamos listen para hacer que el socket acepte conexiones entrantes y 
# accept para comenzar a escuchar. El método listenrequiere de un parámetro que indica 
# el número de conexiones máximas que queremos aceptar; evidentemente, este valor debe 
# ser al menos 1.

socket_s.listen(10)

# El método accept se mantiene a la espera de conexiones entrantes, bloqueando la ejecución 
# hasta que llega un mensaje.

# Cuando llega un mensaje, accept desbloquea la ejecución, devolviendo un objeto socket que 
# representa la conexión del cliente y una tupla que contiene el host y puerto de dicha conexión.

socket_c, (host_c, puerto_c) = socket_s.accept()

# Una vez que tenemos este objeto socket podemos comunicarnos con el cliente a través suyo, 
# mediante los métodos recv y send (o recvfromy sendfrom en UDP) que permiten recibir o enviar 
# mensajes respectivamente. El método send toma como parámetros los datos a enviar, mientras que 
# el método recv toma como parámetro el número máximo de bytes a aceptar.

recibido = socket_c.recv(1024)
print("Recibido: ", recibio)
socket_c.send(recibido)


# Crear un cliente es aún más sencillo. Solo tenemos que crear el objeto socket, 
# utilizar el método connect para conectarnos al servidor y uti-lizar los métodos 
# send y recv que vimos anteriormente. El argumento de connect es una tupla con 
# host y puerto, exactamente igual que bind.

socket_c = socket.socket()
socket_c.connect(("localhost", 9999))
socket_c.send("hola")


# Veamos por último un ejemplo completo. En este ejemplo el cliente manda al servidor 
# cualquier mensaje que escriba el usuario y el servi-dor no hace más que repetir el 
# mensaje recibido. La ejecución termina cuando el usuario escribe quit.


# Servidor
import socket

s = socket.socket()
s.bind("localhost", 9999)
s.listen(1)
sc, addr = s.accept()

while True:      
    recibido = sc.recv(1024)      
    if recibido == "quit":         
        break      
    print("Recibido:", recibido)      
    sc.send(recibido)

print("adios")
sc.close()
s.close()


# Cliente
import socket  

s = socket.socket()  
s.connect("localhost", 9999)

while True:       
    mensaje = input(">")       
    s.send(mensaje)       
    if mensaje == "quit":           
    break  

print("adios") 
s.close()
