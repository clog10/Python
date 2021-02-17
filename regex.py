
# Expresiones regulares

# Las expresiones regulares, también llamadas regex o regexp,
# consisten en patrones que describen conjuntos de cadenas de caracteres.

# Patrones

# La expresión regular más sencilla consiste en una cadena simple, que
# describe un conjunto compuesto tan solo por esa misma cadena. Por ejemplo,
# veamos cómo la cadena “python” coincide con la expresión regular “python”
# usando la función match

import re

if re.match("python", "python"):
    print("Coincide")

# Si quisiéramos comprobar si la cadena es “python”,  “jython”, “cython” o
# cualquier otra cosa que termine en “ython”, podríamos utilizar el carácter
# comodín, el punto ‘.’

if re.match(".ython", "python"):
    print("Coincide")
if re.match(".ython", "jython"):
    print("Coincide")


# Para comprobar si la cadena consiste en 3 caracteres seguidos de un punto, 
# por ejemplo, podríamos utilizar lo siguiente

if re.match("...\.", "abc."):
    print("Coincide")

# Si necesitáramos una expresión que sólo resultara cierta para las cadenas 
# “python”, “jython” y “cython” y ninguna otra, podríamos utilizar el carácter 
# ‘|’ para expresar alternativa escribiendo los tres subpatrones completos

re.match("(p|j|c)ython", "python")

# Otra opción consistiría en encerrar los caracteres ‘p’, ‘j’ y ‘c’ entre 
# corchetes para formar una clase de caracteres, indicando que en esa posición 
# puede colocarse cualquiera de los caracteres de la clase.

re.match("[pjc]ython", "python")

# Si quisiéramos comprobar si la cadena es “python0”, “python1”, “python2”, ... , “python9”

re.match("python[0-9]", "python0")

# Si quisiéramos, por ejemplo, que el último carácter fuera o un dígito o una letra simplemente 
# se escribirían dentro de los corchetes todos los criterios, uno detras de otro.

re.match("python[0-9a-zA-Z]", "pythonp")

# Existen secuencias disponibles que se listan a continuación:

# • “\d” : un dígito. Equivale a [0-9]
# • “\D” : cualquier carácter que no sea un dígito. Equivale a [^0-9]
# • “\w” : cualquier caracter alfanumérico. Equivale a [a-zA-Z0-9_]
# • “\W” : cualquier carácter no alfanumérico. Equivale a [^a-zA-Z0-9_]
# • “\s” : cualquier carácter en blanco. Equivale a [ \t\n\r\f\v]
# • “\S” : cualquier carácter que no sea un espacio en blanco. Equivale a [^ \t\n\r\f\v]

# Veamos ahora cómo representar repeticiones de caracteres, dado que no sería de 
# mucha utilidad tener que, por ejemplo, escribir una expresión regular con 30 caracteres 
# ‘\d’ para buscar números de 30 dígitos. Para este menester tenemos los caracteres 
# especiales +, * y ?, además de las llaves {}.

# El carácter + indica que lo que tenemos a la izquierda, sea un carácter como ‘a’, 
# una clase como ‘[abc]’ o un subpatrón como (abc), puede encontrarse una o mas veces. 
# Por ejemplo la expresión regular “python+” describiría las cadenas “python”, “pythonn” 
# y “pythonnn”, pero no “pytho”, ya que debe haber al menos una n.

# El carácter * es similar a +, pero en este caso lo que se sitúa a su izquierda puede 
# encontrarse cero o mas veces.

# El carácter ? indica opcionalidad, es decir, lo que tenemos a la izquier-da puede o no 
# aparecer (puede aparecer 0 o 1 veces).

# Finalmente las llaves sirven para indicar el número de veces exacto que puede aparecer 
# el carácter de la izquierda, o bien un rango de veces que puede aparecer. Por ejemplo 
# {3} indicaría que tiene que aparecer exac-tamente 3 veces, {3,8} indicaría que tiene 
# que aparecer de 3 a 8 veces, {,8} de 0 a 8 veces y {3,} tres veces o mas (las que sean).

# Otro elemento interesante en las expresiones regulares, para terminar, es la especificación 
# de las posiciones en que se tiene que encontrar la cadena, esa es la utilidad de ^ y $, que 
# indican, respectivamente, que el elemento sobre el que actúan debe ir al principio de la cadena 
# o al final de esta.


# Usando el módulo re

# Al llamar al método group sin parámetros se nos devuelve el grupo 0 de la cadena reconocida. 
# El grupo 0 es la subcadena reconocida por la expresión regular al completo, aunque no existan 
# paréntesis que delimiten el grupo
mo = re.match("http://.+net", "http://mundogeek.net")
print(mo.group())

# Podríamos crear grupos utilizando los paréntesis, como aprendimos en la sección anterior, 
# obteniendo así la parte de la cadena que nos interese.
mo = re.match("http://(.+)net", "http://mundogeek.net")
print(mo.group(0))
print(mo.group(1))

# El método groups, por su parte, devuelve una lista con todos los grupos, 
# exceptuando el grupo 0, que se omite.
mo = re.match("http://(.+)(.{3})", "http://mundogeek.net")
print(mo.groups())

# La función search del módulo re funciona de forma similar a match; contamos 
# con los mismos parámetros y el mismo valor de retorno. La única diferencia 
# es que al utilizar match la cadena debe ajustarse al patrón desde el primer 
# carácter de la cadena, mientras que con searchbuscamos cualquier parte de la 
# cadena que se ajuste al patrón. Por esta razón el método start de un objeto 
# MatchObject obtenido mediante la función match siempre devolverá 0, mientras 
# que en el caso de searchesto no tiene por qué ser así.

# Otra función de búsqueda del módulo re es findall. Este toma los mismos parámetros 
# que las dos funciones anteriores, pero devuelve una lista con las subcadenas que 
# cumplieron el patrón.

# Otra posibilidad, si no queremos todas las coincidencias, es utilizar finditer, 
# que devuelve un iterador con el que consultar uno a uno los distintos MatchObject.

