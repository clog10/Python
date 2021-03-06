import keyword
import math
import datetime
print(keyword.kwlist)

# Tipico Hola Mundo
print("Hello World")
# integer
a = 2
print(a)
print(type(a))
# integer
b = 68545413241658541654165741695874962
print(b)
print(type(b))
# Floating point
pi = 3.14
print(pi)
print(type(pi))
# String
c = "Alexis Posada"
print(c)
print(type(c))
# String
name = 'John Doe'
print(name)
print(type(name))
# Boolean
q = True
print(q)
print(type(q))
# # Empty value or  null  data  type
x = None
print(x)
print(type(x))

x, y, z = 1, 2, 3
print(x, y, z)

# listas
g = [1, 2, 3, 4, 5, 6, 7, 8, 9]
g[2] = 20
print(g)

# listas anidados
h = [1, 2, [7, 8, 9], 3, 4]
print(h)

h[2] = 3
print(h)

i = [True, 2, "Carlos", [1, 3], 5.5, False]
print(i)

# entrada de texto
texto = input("ingresa un texto\n")
print("Texto: " + texto)

k = input("ingresa un numero: ")
m = float(k) / 2
print(m)

# numeros complejos
n = 5 + 4j
print(n)

# secuencias y colecciones
o = reversed("Carlos")


p = {1: "uno", 2: "dos"}
print(p)

q = {"nombre": "Carlos", "apellido": "Loaeza"}
print(q)

# concidionales
r = 10
s = 5
if (r > s):
    print("es mayor")

t = '7'
if isinstance(t, int):
    t += 1
elif isinstance(t, str):
    t = int(t)
    t += 1
print(t)

# convertir entre tipos de datos
ab = '123'
cd = int(ab)
print(cd)

ef = '123.456'
gh = float(ef)
print(gh)

ij = 'Carlos'
kl = list(ij)
print(kl)
mn = set(ij)
(print(mn))
op = tuple(ij)
print(op)

# tipos de cadenas
normal = 'foo\nbar'
print(normal)
escaped = 'foo\\nbar'
print(escaped)
raw = r'foo\nbar'
print(raw)

# Ejemplos de tipos de datos inmutables:
# •int , long , float ,complex
# •str
# •bytes
# •tuple
# •frozenset
#
# Ejemplos de tipos dedatos mutables:
# •bytearray
# •list
# •set
# •dict

# Sacando raíz cuadrada
numero = input("dame un numero: ")
raiz = math.sqrt(float(numero))
print(raiz)

# definiendo funciones


def my_function():
    a = 2
    return a


print(my_function())

# respetar los espacios y sangrias asignados por el editor de código

# operador ternario
# resultado = valor_si if condicion else valor_no
opter = input("Introduce un número: ")
res = opter if (int(opter) > 50) else 0
print(res)

num1 = 10
num2 = 20
if num1 > num2:
    print(num1)
else:
    print(num2)


# Listas dinamicas
mixed_list = [1, 'abc', True, 2.34, None]
print(mixed_list[-1])
print(mixed_list[-4])

# agregando elemento al final de la lista
mixed_list.append("Sia")
print(mixed_list)

# Agregando elemento en el indice indicado
mixed_list.insert(1, "Nikki")
print(mixed_list)


# eliminando un elemento con determinado valor
mixed_list.remove(True)
print(mixed_list)


# obtener el indice del elemento con determinado valor
mixed_list.index('abc')

# contando la longitud de la lista
print(len(mixed_list))

# contando la ocurrencia de un elemento en la lista
listita = [1, 1, 1, 2, 3, 4]
print(listita.count(1))

# revirtiendo la lista
print(listita.reverse())

# recorriendo la lista
for element in listita:
    print(element)

# Tuplas (2 valores)
ip_address = ('10.20.30.40', 8080)

# Diccionarios {key: value}
estados = {
    'Aguascalientes': 'Aguascalientes',
    'Baja California': 'Mexicali',
    'Baja California Sur': 'La Paz',
    'Campeche': 'San Francisco de Campeche',
    'Chihuahua': 'Chihuahua',
    'Chiapas': 'Tuxtla Gutiérrez',
    'Coahuila de Zaragoza': 'Saltillo',
    'Colima': 'Colima',
    'Durango': 'Victoria de Durango',
    'Guanajuato': 'Guanajuato',
    'Guerrero': 'Chilpancingo de los Bravo',
    'Hidalgo': 'Pachuca de Soto',
    'Jalisco': 'Guadalajara',
    'México': 'Toluca de Lerdo',
    'Michoacán de Ocampo': 'Morelia',
    'Morelos': 'Cuernavaca',
    'Nayarit': 'Tepic',
    'Nuevo León': 'Monterrey',
    'Oaxaca': 'Oaxaca de Juárez',
    'Puebla': 'Puebla de Zaragoza',
    'Querétaro': 'Santiago de Querétaro',
    'Quintana Roo': 'Chetumal',
    'San Luis Potosí': 'San Luis Potosí',
    'Sinaloa': 'Culiacán Rosales',
    'Sonora': 'Hermosillo',
    'Tabasco': 'Villahermosa',
    'Tamaulipas': 'Ciudad Victoria',
    'Tlaxcala': 'Tlaxcala de Xicohténcatl',
    'Veracruz': 'Xalapa-Enríquez',
    'Yucatán': 'Mérida',
    'Zacatecas': 'Zacatecas',
    'México(País)': 'Ciudad de México(DF)'
}

# obteniendo un valor del diccionario
capital = estados['Oaxaca']
print(capital)

# Obteniendo valor respecto a su llave
for valor in estados.keys():
    print('{} is the capital of {}'.format(estados[valor], valor))

# conjuntos
first_names = {'Carlos', 'Jesus', 'Maria', "Rosalba"}

# construyendo un conjunto a partir de una lista
my_set = set(listita)
print(my_set)

# verificando la existencia de un elemento en un conjunto
nombre = 'Carlos'
if nombre in first_names:
    print("Existe: "+nombre)

# obteniendo fecha y hora actual
today = datetime.datetime.now()
print(str(today))

# Bucles

# bucle while
edad = 0
while edad < 18:
    edad = edad + 1
    print("Felicidades, tienes: " + str(edad))

# for
secuencia = ["uno", "dos", "tres"]
for elemento in secuencia:
    print(elemento)

# Continuamos con funciones


def mi_funcion2(param1, param2):
    # cadena que sirve para la documentación
    """Esta funcion imprime los dos valores pasados como parametros"""
    print(param1)
    print(param2)


mi_funcion2("hola", 2)


def imprimir(texto, veces=5):
    """Esta funcion imprime 5 veces el parametro dado"""
    print(veces * texto)


imprimir("hola")
# si se le indica otro valor, será este el que se utilice
imprimir("hola", 2)

# Para definir funciones con un número variable de argumentos
# coloca-mos un último parámetro para la función cuyo nombre
# debe preceder-se de un signo *


def varios(param1, param2, *otros):
    for val in otros:
        print(val)


varios(1, 2)
varios(1, 2, 3)
varios(1, 2, 3, 4)

# En el siguiente ejemplo se utiliza la función items de los
# diccionarios, que devuelve una lista con sus elementos, para
# imprimir los parámetros que contiene el diccionario.


def varios(param1, param2, **otros):
    for i in otros.items():
        print(i)


varios(1, 2, tercero=3)


# En este ejemplo se hace uso del método append de las listas.
# Un método no es más que una función que pertenece a un objeto,
# en este caso a una lista; y append, en concreto, sirve para añadir
# un elemento a una lista.

def f(x, y):
    x = x + 3
    y.append(23)
    print(x, y)


x = 22
y = [22]
f(x, y)
print(x, y)


# Veamos por último cómo devolver valores,
# para lo que se utiliza la palabra clave return

def sumar(x, y):
    return x + y


print(sumar(3, 2))

# También podríamos pasar varios valores que retornar a return


def f(x, y):
    return x * 2, y * 2


a, b = f(1, 2)

