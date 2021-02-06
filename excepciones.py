
# Las excepciones son errores detectados por Python durante la ejecución del programa.
# Cuando el intérprete se encuentra con una situación excepcional, como el intentar dividir
# un número entre 0 o el intentar acceder a un archivo que no existe, este genera o lanza
# una excepción, informando al usuario de que existe algún problema.

# En Python se utiliza una construcción try-except para capturar y tratar las excepciones.
# El bloque try (intentar) define el fragmento de código en el que creemos que podría producirse
# una excepción. El blo-que except (excepción) permite indicar el tratamiento que se llevará a
# cabo de producirse dicha excepción. Muchas veces nuestro tratamiento de la excepción consistirá
# simplemente en imprimir un mensaje más amigable para el usuario, otras veces nos interesará
# registrar los errores y de vez en cuando podremos establecer una estrategia de resolución del
# problema.

def dividir(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        print("division entre cero")
    finally:
        print("Limpiando")


dividir(5,0)

# Excepciones propias

# También es interesante comentar que como programadores podemos crear y lanzar nuestras
# propias excepciones. Basta crear una clase que herede de Exception o cualquiera de sus
# hijas y lanzarla con raise.


class MiError(Exception):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return "Error" + str(self.valor)


try:
    if 80 > 20:
        raise MiError(33)
except MiError:
    print("Error")


# Excepciones disponibles por defecto

# BaseException: Clase de la que heredan todas las excepciones.
# Exception(BaseException): Super clase de todas las excepciones que no sean de salida.
# GeneratorExit(Exception): Se pide que se salga de un generador.
# StandardError(Exception): Clase base para todas las excepciones que no tengan que ver con salir del intérprete.
# ArithmeticError(StandardError): Clase base para los errores aritméticos.
# FloatingPointError(ArithmeticError): Error en una operación de coma flotante.
# OverflowError(ArithmeticError): Resultado demasiado grande para poder representarse.
# ZeroDivisionError(ArithmeticError): Lanzada cuando el segundo argumento de una operación de división o módulo era 0.
# AssertionError(StandardError): Falló la condición de un estamento assert.
# AttributeError(StandardError): No se encontró el atributo.
# EOFError(StandardError): Se intentó leer más allá del final de fichero.
# EnvironmentError(StandardError): Clase padre de los errores relacio-nados con la entrada/salida.
# IOError(EnvironmentError): Error en una operación de entrada/salida.
# OSError(EnvironmentError): Error en una llamada a sistema.
# WindowsError(OSError): Error en una llamada a sistema en Windows.
# ImportError(StandardError): No se encuentra el módulo o el elemento del módulo que se quería importar.
# LookupError(StandardError): Clase padre de los errores de acceso.
# IndexError(LookupError): El índice de la secuencia está fuera del rango posible.
# KeyError(LookupError): La clave no existe.
# MemoryError(StandardError): No queda memoria suficiente.
# NameError(StandardError): No se encontró ningún elemento con ese nombre.
# UnboundLocalError(NameError): El nombre no está asociado a ninguna variable.
# ReferenceError(StandardError): El objeto no tiene ninguna referencia fuerte apuntando hacia él.
# RuntimeError(StandardError): Error en tiempo de ejecución no especificado.
# NotImplementedError(RuntimeError): Ese método o función no está implementado.
# SyntaxError(StandardError): Clase padre para los errores sintácticos.
# IndentationError(SyntaxError): Error en la indentación del archivo.
# TabError(IndentationError): Error debido a la mezcla de espacios y tabuladores.
# SystemError(StandardError): Error interno del intérprete.
# TypeError(StandardError): Tipo de argumento no apropiado.
# ValueError(StandardError): Valor del argumento no apropiado.
# UnicodeError(ValueError): Clase padre para los errores relacionados con unicode.
# UnicodeDecodeError(UnicodeError): Error de decodificación unicode.
# UnicodeEncodeError(UnicodeError): Error de codificación unicode.
# UnicodeTranslateError(UnicodeError): Error de traducción unicode.
# StopIteration(Exception): Se utiliza para indicar el final del iterador.
# Warning(Exception): Clase padre para los avisos.
# DeprecationWarning(Warning): Clase padre para avisos sobre características obsoletas.
# FutureWarning(Warning): Aviso. La semántica de la construcción cambiará en un futuro.
# ImportWarning(Warning): Aviso sobre posibles errores a la hora de importar.
# PendingDeprecationWarning(Warning): Aviso sobre características que se marcarán como obsoletas en un futuro próximo.
# RuntimeWarning(Warning): Aviso sobre comportmaientos dudosos en tiempo de ejecución.
# SyntaxWarning(Warning): Aviso sobre sintaxis dudosa.
# UnicodeWarning(Warning): Aviso sobre problemas relacionados con Unicode, sobre todo con problemas de conversión.
# UserWarning(Warning): Clase padre para avisos creados por el programador.
# KeyboardInterrupt(BaseException): El programa fué interrumpido por el usuario.
# SystemExit(BaseException): Petición del intérprete para terminar la ejecución.
