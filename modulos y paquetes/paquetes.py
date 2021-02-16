# Paquetes

# Si los módulos sirven para organizar el código, los paquetes sirven para 
# organizar los módulos. Los paquetes son tipos especiales de módulos (ambos 
# son de tipo module) que permiten agrupar módulos relacionados. Mientras los 
# módulos se corresponden a nivel físico con los archivos, los paquetes se 
# representan mediante directorios.

# Para hacer que Python trate a un directorio como un paquete es necesario 
# crear un archivo __init__.py en dicha carpeta. En este archivo se pueden 
# definir elementos que pertenezcan a dicho paquete, como una constante DRIVER 
# para el paquete bbdd, aunque habitualmente se trata-rá de un archivo vacío. 
# Para hacer que un cierto módulo se encuentre dentro de un paquete, basta con 
# copiar el archivo que define el módulo al directorio del paquete.

# Para encontrar algún módulo o paquete que cubra una cierta necesidad, puedes 
# consultar la lista de PyPI (Python Package Index) en http://pypi.python.org/
