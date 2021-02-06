# La programación funcional es un paradigma en el que la programación
# se basa casi en su totalidad en funciones, entendiendo el concepto de
# función según su definición matemática, y no como los simples subprogramas
# de los lenguajes imperativos que hemos visto hasta ahora.

# En los lenguajes funcionales puros un programa consiste exclusivamente en
# la aplicación de distintas funciones a un valor de entrada para obtener un
# valor de salida.
#
# Python, sin ser un lenguaje puramente funcional incluye varias características
# tomadas de los lenguajes funcionales como son las funciones de orden superior
# o las funciones lambda (funciones anónimas)

# Funciones de Orden superior

# El concepto de funciones de orden superior se refiere al uso de fun-ciones como
# si de un valor cualquiera se tratara, posibilitando el pasar funciones como
# parámetros de otras funciones o devolver funciones como valor de retorno.


def saludar(lang):
    def saludar_es():
        print("Hola")

    def saludar_en():
        print("Hi")

    def saludar_fr():
        print("Salut")

    lang_func = {"es": saludar_es,
                 "en": saludar_en,
                 "fr": saludar_fr}
    return lang_func[lang]


# En este caso el primer par de paréntesis indica los parámetros de la función saludar,
# y el segundo par, los de la función devuelta por saludar.
saludar("fr")()


f = saludar("en")
f()


# Iteraciones de orden superior sobre listas

# map(function, sequence[, sequence, ...])
def cuadrado(n):
    return n ** 2


g = [1, 2, 3]
l2 = map(cuadrado, g)
print("elevando al cuadrado usando map")
for elemento in l2:
    print(elemento)

# filter(function, sequence)


def es_par(n):
    return (n % 2.0 == 0)


h = [1, 2, 3, 4, 5, 6]
l3 = filter(es_par, h)
print("filtrando usando filter")
for elemento in l3:
    print(elemento)


# reduce(function, sequence[, initial])

def sumar(x, y):
    result = x + y
    print(f"{x} + {y} = {result}")
    return result


def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value


i = [1, 2, 3]
l4 = reduce(sumar, i)
print("sumando valores de una lista con reduce")
print(l4)


# Funciones lambda

# El operador lambda sirve para crear funciones anónimas en línea.
#  Al ser funciones anónimas, es decir, sin nombre, estas no podrán
# ser referen-ciadas más tarde.

j = [1, 2, 3, 4, 5, 6]
l5 = filter(lambda n: n % 2.0 == 0, j)
for elemento in l5:
    print(elemento)


# Comprensión de listas

# susituyendo map
l6 = [n ** 2 for n in g]

# sustituyendo filter
l7 = [n for n in h if n % 2.0 == 0]

# Anidación de for
print("anidando for")
k = [0, 1, 2, 3]
m = ["a", "b"]
n = []
for s in m:
    for v in k:
        if v > 0:
            n.append(s * v)
            print(n)


# Generadores

# Un generador es una clase especial de función que genera valores sobre los que iterar.
# Para devolver el siguiente valor sobre el que iterar se utiliza la palabra clave yield
# en lugar de return. Veamos por ejemplo un generador que devuelva números de n a m con
# un salto s.


def mi_generador(n, m, s):
    while(n <= m):
        yield n
        n += s


print("generador")
for n in mi_generador(0, 5, 1):
    print(n)


# Decoradores

# Un decorador no es es mas que una función que recibe una función como parámetro y devuelve
# otra función como resultado. Por ejem-plo podríamos querer añadir la funcionalidad de que
# se imprimiera el nombre de la función llamada por motivos de depuración:

def mi_decorador(funcion):
    def nueva(*args):
        print("Llamada a la funcion", funcion.__name__)
        retorno = funcion(*args)
        return retorno
    return nueva


def imp(cadena):
    print(cadena)


mi_decorador(imp)("hola")

