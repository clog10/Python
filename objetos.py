# En Python las clases se definen mediante la palabra clave class seguida
# del nombre de la clase, dos puntos (:) y a continuación, indentado, el
# cuerpo de la clase. Como en el caso de las funciones, si la primera línea
# del cuerpo se trata de una cadena de texto, esta será la cadena de
# documentación de la clase o docstring

class Coche:
    """Abstraccion de los objetos coche."""

    def __init__(self, gasolina):
        self.gasolina = gasolina
        print("Tenemos", gasolina, "litros")

    def arrancar(self):
        if self.gasolina > 0:
            print("Arranca")
        else:
            print("No arranca")

    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print("Quedan", self.gasolina, "litros")
        else:
            print("No se mueve")

# Para crear un objeto se escribiría el nombre de la clase seguido de cualquier
# parámetro que sea necesario entre paréntesis. Estos parámetros son los que se
# pasarán al método __init__, que como decíamos es el método que se llama al
# instanciar la clase


mi_coche = Coche(3)

# Ahora que ya hemos creado nuestro objeto, podemos acceder a sus atributos y
# métodos mediante la sintaxis objeto.atributo y objeto.metodo()
mi_coche.arrancar()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.arrancar()
print(mi_coche.gasolina)

# Herencia

# Superclase o clase Padre


class Instrumento:
    """Abstraccion de los objetos instumento."""

    def __init__(self, precio):
        self.precio = precio

    def tocar(self):
        print("Estamos tocando musica")

    def romper(self):
        print("Eso lo pagas tu")
        print("Son", self.precio, "$$$")

# Clase heredada o hija


class Guitarra(Instrumento):

    def __init__(self, precio, tipo_cuerdas):
        # Invocamos constructor de la clase Padre
        Instrumento.__init__(self, precio)
        # Nuevos atributos
        self.tipo_cuerdas = tipo_cuerdas

    def imprime(self):
        print("Precio: ", self.precio, ", Tipo de Cuerdas: ", self.tipo_cuerdas)


mi_guitarra = Guitarra(500, "metal")
mi_guitarra.imprime()

# Polimorfismo

# Python, al ser de tipado dinámico, no impone restricciones a los tipos que se
# le pueden pasar a una función, por ejemplo, más allá de que el objeto se comporte
# como se espera: si se va a llamar a un método f()del objeto pasado como parámetro,
# por ejemplo, evidentemente el objeto tendrá que contar con ese método. Por ese motivo,
# a diferencia de lenguajes de tipado estático como Java o C++, el polimorfismo en
# Python no es de gran importancia.


# Encapsulamiento

# En Python no existen los modificadores de acceso, y lo que se suele hacer es que el
# acceso a una variable o función viene determinado por su nombre: si el nombre comienza
# con dos guiones bajos (y no termina también con dos guiones bajos) se trata de una
# variable o función privada, en caso contrario es pública

class Fecha():
    def __init__(self):
        self.__dia = 1

    def getDia(self):
        return self.__dia

    def setDia(self, dia):
        if dia > 0 and dia < 31:
            self.__dia = dia
        else:
            print("Error")

    # Declaración de metodo privado con 2 guiones bajos
    # Al intentar llamarlo Python lanzará una excepción quejándose de que no existe,
    # (evidentemente existe, pero no lo podemos ver porque es privado)
    def __privado(self):
        print("fecha privada")


mi_fecha = Fecha()
mi_fecha.setDia(21)
print(mi_fecha.getDia())
mi_fecha.__privado()


# Principales Métodos Especiales

# Método llamado después de crear el objeto para realizar tareas de inicialización.
__init__(self, args)

# Método exclusivo de las clases de nuevo estilo que se ejecuta antes que __init__ y 
# que se encarga de construir y devolver el objeto en sí. Es equivalente a los 
# constructores de C++ o Java. Se trata de un método estático, es decir, que existe 
# con independencia de las instancias de la clase: es un método de clase, no de objeto, 
# y por lo tanto el primer parámetro no es self, sino la propia clase: cls.
__new__(cls, args)

# Método llamado cuando el objeto va a ser borrado. También llamado destructor, 
# se utiliza para realizar tareas de limpieza
__del__(self)


# Método llamado para crear una cadena de texto que represente a nuestro objeto. 
# Se utiliza cuando usamos print para mostrar nuestro objeto o cuando usamos la 
# función str(obj) para crear una cadena a partir de nuestro objeto.
__str__(self)

# Método llamado cuando se utilizan los operadores de comparación para comprobar 
# si nuestro objeto es menor, mayor o igual al objeto pasado como parámetro. 
# Debe devolver un número negativo si nuestro objeto es menor, cero si son iguales, 
# y un número positivo si nuestro objeto es mayor. Si este método no está definido 
# y se intenta com-parar el objeto mediante los operadores <, <=, > o >= se lanzará 
# una excepción. Si se utilizan los operadores == o != para comprobar si dos objetos 
# son iguales, se comprueba si son el mismo objeto (si tienen el mismo id)
__cmp__(self, otro)

# Método llamado para comprobar la longitud del objeto. Se utiliza, por ejemplo, 
# cuando se llama a la función len(obj) sobre nuestro objeto. Como es de suponer, 
# el método debe devolver la longitud del objeto
__len__(self)

# Revisitando Objetos

# Ahora que sabemos qué son las clases, los objetos, las funciones, y los métodos 
# es el momento de revisitar estos objetos para descubrir su verdadero potencial.

# Diccionarios

# Busca el valor de la clave k en el diccionario. Es equivalente a utilizar D[k] 
# pero al utilizar este método podemos indicar un valor a devolver por defecto si 
# no se encuentra la clave, mientras que con la sintaxis D[k], de no existir la 
# clave se lanzaría una excepción.
D.get(k[, d])

# Comprueba si el diccionario tiene la clave k. Es equivalente a la sin-taxis k in D.
D.has_key(k)

#Devuelve una lista de tuplas con pares clave-valor.
D.items()

#Devuelve una lista de las claves del diccionario
D.keys()

# Borra la clave k del diccionario y devuelve su valor. Si no se encuentra dicha 
# clave se devuelve d si se especificó el parámetro o bien se lanza una excepción
D.pop(k[, d])

# Devuelve una lista de los valores del diccionario
D.values()

# Cadenas

# Devuelve el número de veces que se encuentra sub en la cadena. Los parámetros 
# opcionales start y end definen una subcadena en la que buscar.
S.count(sub[, start[, end]])

# Devuelve la posición en la que se encontró por primera vez sub en la cadena 
# o -1 si no se encontró.S.join(sequence)Devuelve una cadena resultante de concatenar 
# las cadenas de la se-cuencia seq separadas por la cadena sobre la que se llama el método.
S.find(sub[, start[, end]])

# Busca el separador sep en la cadena y devuelve una tupla con la subcadena 
# hasta dicho separador, el separador en si, y la subcadena del separador hasta el final 
# de la cadena. Si no se encuentra el separador, la tupla contendrá la cadena en si y dos 
# cadenas vacías.
S.partition(sep)

# Devuelve una cadena en la que se han reemplazado todas las 
# ocurrencias de la cadena old por la cadena new. Si se especifica el parámetro count, 
# este indica el número máximo de ocurrencias a reemplazar
S.replace(old, new[, count])

#Devuelve una lista conteniendo las subcadenas en las que se 
#divide nuestra cadena al dividirlas por el delimitador sep. En el caso de que no se 
# especifique sep, se usan espacios. Si se especifica maxsplit, este indica el número 
# máximo de particiones a realizar
S.split([sep [,maxsplit]])

# Listas

# Añade un objeto al final de la lista.
L.append(object)

# Devuelve el número de veces que se encontró value en la lista.
L.count(value)

# Añade los elementos del iterable a la lista.
L.extend(iterable)

# Devuelve la posición en la que se encontró la primera ocurrencia de value. 
# Si se especifican, start y stop definen las posiciones de inicio y fin de 
# una sublista en la que buscar.
L.index(value[, start[, stop]])

# Inserta el objeto object en la posición index.
L.insert(index, object)

# Devuelve el valor en la posición index y lo elimina de la lista. Si no se especifica 
# la posición, se utiliza el último elemento de la lista.
L.pop([index])

#Eliminar la primera ocurrencia de value en la lista.
L.remove(value)

# Invierte la lista. Esta función trabaja sobre la propia lista desde la que se invoca 
# el método, no sobre una copia.
L.reverse()

# Ordena la lista. Si se especifica cmp, este debe ser una función que tome como parámetro
# dos valores x e y de la lista y devuelva -1 si x es menor que y, 0 si son iguales y 1 si
# x es mayor que y.El parámetro reverse es un booleano que indica si se debe ordenar la lista 
# de forma inversa, lo que sería equivalente a llamar primero a L.sort() y después a L.reverse().
L.sort(cmp=None, key=None, reverse=False)
