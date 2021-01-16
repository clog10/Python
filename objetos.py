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

    # Declaración de metodo privado
    # Al intentar llamarlo Python lanzará una excepción quejándose de que no existe,
    # (evidentemente existe, pero no lo podemos ver porque es privado)
    def __privado(self):
        print("fecha privada")


mi_fecha = Fecha()
mi_fecha.setDia(21)
print(mi_fecha.getDia())
mi_fecha.__privado()
