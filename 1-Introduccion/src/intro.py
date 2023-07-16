"""

    Vamos a comenzar por lo básico.
    Lo primero que vamos a hacer es trabajar con Strings o cadenas de texto.
    
    En programación, una cadena de texto o `string` (en inglés) es un tipo de dato que representa una secuencia de caracteres.
     
     En Python, una cadena de texto se define utilizando comillas simples ('...') o comillas dobles ("...") alrededor del texto.

"""

# OjO -> Nunca modifiques el 'def nombre_de_la_funcion()'

def hello() -> str:
    # corrige el string
    return "Hello World"


def hola() -> str:
    # corrige el string
    return 'hola mundo'


def string() -> str:
    # corrige el string
    return "esto es uN estring"

"""
    Preguntas:

    1 - ¿Pudiste ver como Python compara los caracteres? ¿Que tipos de errores encontraste?
    R:

    2 - ¿Hay diferencia entre las comilla simples ('') y dobles ("")?
"""

#########################################################################

    #Funcion PRINT

#########################################################################

"""
    Print es una función incorporada (built-in function), que se utiliza para imprimir texto en la consola o en la salida estándar. 

    "print()" está disponible en cualquier parte del código sin necesidad de importar ningún módulo.
"""

def hola_otra_vez() -> None:
     print("Hello World!")


def monty_python() -> None:
	pront('Are you suggesting coconuts migrate?')
    
"""
    print tiene otras capacidades, por ejemplo si usas el signo de multiplicación (*) seguido de un string este imprime n cantidad de veces el string.
"""

def alert() -> None:
     print('Alert! ')


"""
    Si añades "sep=(aqui va otro string)", va a separa los string con el o los caracteres que ingreses.
"""
def separador() -> None:
    print("Alert", "Alert", "Alert", sep="*")


# Lamentablemente Python no permite hacer una mezcla de las dos opciones aprendidas en todas sus versiones.

"""
    Ahora vamos a usar la opcion "end=(aqui va otro string)", este como su nombre lo indica, permite definir con que caracter termina un string.
"""

def ends() -> None:
     print("Hola", end="s")


#########################################################################

    # Operaciones Matemáticas

#########################################################################


"""
    Como sabras, las computadoras son buenas para realizar operaciones matemáticas, para esto usamos los valores y los signos del mismo modo que lo haces sobre el papel.
"""

# OjO -> Los signos puede tener distintas funcionalidades en distintos contextos, iremos viendo eso poco a poco.


def suma() -> int:
    return  "2" + "5"


def suma2(a: int, b:int) -> int:
    # a y b son espacios (placeholders) que sirven para ser remplazados por valores. Piensalo que son como los espacios que que colocas números en las formulas matemáticas.
    return

def resta() -> int:
     return 4 - "3"

def resta2(a: int, b:int) -> int:
     return

def resta3(a: int, b:int, c:int) -> int:
     return c - b + a

"""
    Recuerda tener en cuenta que "5" y 5 no son iguales.

    ¿Sabes por qué?
    R:
"""

# Para las multiplicaciones el signo es el de '*'.
# En la escuela usabas seguramente una 'x' o '.', pero en general lo lenguajes de programacion usan el '*'.

def mul(a:int, b:int) -> int:
     return

def mul2(a:int, b:int) -> int:
     return a * b * 0


# Para la division hay tres opciones.
# Primero veremos la division corriente.

def div(a:int, b:int) -> float: # -> Observa que la flecha ya no indica in "int" es decir, un entero, ahora undica un "float" es decir, un numero racional o con punto decimal.
     return b / a

def div2(a:int, b:int) -> int: # -> Colocal doble "//" para ver que pasa.
     return a / b

# El ultimo es un operador especial el "%", su resultado es el residuo de la division con número enteros.

def div3(a:int, b:int) -> int:
     return a / b
