from math import pi


# Entrada estandar

# La forma más sencilla de obtener información por parte del usuario
# es mediante la función input. Esta función toma como parámetro
# una cadena a usar como prompt (es decir, como texto a mostrar al
# usuario pidiendo la entrada) y devuelve una cadena con los caracteres
# introducidos por el usuario hasta que pulsó la tecla Enter.

nombre = input("Como te llamas? ")
print("Encantado, " + nombre)

try:
    edad = input("Cuantos años tienes? ")
    dias = int(edad) * 365
    print("Has vivido " + str(dias) + " dias")
except ValueError:
    print("Eso no es un numero")

# Salida Estandar

print("Hola mundo")

# Los especificadores más sencillos están formados por el símbolo %
# seguido de una letra que indica el tipo con el que formatear el valor.

# %s = cadena
# %d = entero
# %o = octal
# %x = hexadecimal
# %f = real

# Se puede introducir un número entre el % y el carácter que indica el tipo 
# al que formatear, indicando el número mínimo de caracteres que queremos 
# que ocupe la cadena. Si el tamaño de la cadena resultante es menor que 
# este número, se añadirán espacios a la izquierda de la cadena. En el caso 
# de que el número sea negativo, ocurrirá exactamente lo mismo, sólo que 
# los espacios se añadirán a la derecha de la cadena.
print("%10s mundo" % "Hola")
print("%-10s mundo" % "Hola")

# En el caso de los reales es posible indicar la precisión a utilizar 
# precediendo la f de un punto seguido del número de decimales que queremos mostrar.
print("%.4f" % pi)

# La misma sintaxis se puede utilizar para indicar el número de caracteres 
# de la cadena que queremos mostrar
print("%.4s" % "hola mundo")


# Archivos

# Los ficheros en Python son objetos de tipo file creados mediante la función 
# open (abrir). Esta función toma como parámetros una cadena con la ruta al 
# fichero a abrir, que puede ser relativa o absoluta; una cadena opcional 
# indicando el modo de acceso (si no se especifica se accede en modo lectura) 
# y, por último, un entero opcional para especificar un tamaño de buffer 
# distinto del utilizado por defecto.

# El modo de acceso puede ser cualquier combinación lógica de los siguientes modos:

# ‘r’ : read, lectura. Abre el archivo en modo lectura. El archivo tiene que existir 
# previamente, en caso contrario se lanzará una excepción de tipo IOError.
# 
# ‘w’ : write, escritura. Abre el archivo en modo escritura. Si el archivo no existe 
# se crea. Si existe, sobreescribe el contenido.
# 
# ‘a’ : append, añadir. Abre el archivo en modo escritura. Se diferencia del modo ‘w’ en 
# que en este caso no se sobreescribe el contenido del archivo, sino que se comienza a 
# escribir al final del archivo.
# 
# ‘b’ : binary, binario.
# 
# ‘+’ : permite lectura y escritura simultáneas.
# 
# ‘U’ : universal newline, saltos de línea universales. Permite trabajar con archivos 
# que tengan un formato para los saltos de línea que no coincide con el de la plataforma 
# actual (en Windows se utiliza el caracter CR LF, en Unix LF y en Mac OS CR).


f = open("archivo.txt", "r")

# Una vez terminemos de trabajar con el archivo debemos cerrarlo utilizando el método close.

# Lectura de archivos

# Para la lectura de archivos se utilizan los métodos read, readline y realines.

completo = f.read()
print(completo)


g = open("archivo2.txt", "r")

while True:      
    linea = g.readline()    
    print(linea)
    if (not linea): 
        break      

# Escritura de archivos

# Para la escritura de archivos se utilizan los método write y writelines. 
# Mientras el primero funciona escribiendo en el archivo una cadena de texto 
# que toma como parámetro, el segundo toma como parámetro una lista de cadenas 
# de texto indicando las líneas que queremos escribir en el fichero.

h = open("archivo3.txt", "w")
h.write("Clog10")

i = open("archivo4.txt", "w")
i.writelines(["Hola", "Mundo"])

