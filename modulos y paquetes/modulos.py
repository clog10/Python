
# Modulos

# Para facilitar el mantenimiento y la lectura los programas demasiado largos
# pueden dividirse en módulos, agrupando elementos relaciona-dos. Los módulos
# son entidades que permiten una organización y división lógica de nuestro código.
# Los ficheros son su contrapartida física: cada archivo Python almacenado en disco
# equivale a un módulo.

def mi_funcion():
    print("Una función")


class MiClase:
    def __init__(self):
        print("Una clase")


print("Un módulo")

# Si quisiéramos utilizar la funcionalidad definida en este módulo en nuestro programa 
# tendríamos que importarlo. Para importar un módulo se utiliza la palabra clave import 
# seguida del nombre del módulo, que consiste en el nombre del archivo menos la extensión.
# Vayamos al archivo programa.py
