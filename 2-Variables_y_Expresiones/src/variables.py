#######################################################################

#   VARIABLES

#######################################################################

"""
    Para poder trabajar y transformar los datos sin perderlos
    es necesario guiardarlos en algún tipo de contenedor.

    Esos contenedores los llamamos "Variables"

    Para declarar (crear) una variable solo hace falta crear un nombre,
    como por ejemplo: 'mi_variable' y asignarle un valor con el signo '='.
"""

def mi_variable() -> None:
    mi_variable: int = #asignale el numero 42 a mi_variable
    print(mi_variable)

########################################################################


"""
    En general, para todos los lenguajes de programación la asignacion de valores se hace por medio del signo '='.

    Puedes nombrar una variable casi como quieras pero hay ciertas reglas.
"""

# 1 - no puede empezar por un número


def mi_variable2() -> None:
    # Pero puede ser seguida de un número
    # lleva el número al final de la declaracion del nombre
    mi_variable = 42 
    print(mi_variable)



# 2 - sola pueden contener caracteres alfabeticos (a-z y A-Z), númericos (0-9) y underscore (_)

def mi_variable3() -> None:
    # Hazme funcionar
    mi_variable? = 42 
    print(mi-variable)
          

# 3 - no debe contener espacios

def mi_variable4() -> None:
    # Hazme funcionar
    mi variable = 42


# No solo puede contener el caracter '_' sino que ademas pueden empezar por ese caracter
def mi_variable5() -> None:
    _a_que_si_puedo = #dale cualquier valor
    print(_a_que_si_puedo)

"""

    Sin embargo, tanto variables, como funciones, métodos y demas que
    empiecen por '_' tiene un significado especial.end=

    Por otro lado, aunque las variables pueden escribirce en casi cualquier caracter unicode (utf-8), es mejor atenerse al alfabeto
    en ingles para evitar problemas de lectura y compatibilidad.

"""

#   Convenciones

"""
    Aunque hay muchas manera de nombrar las variables, en Python
    se usa un convención que se llama 'snake_case', esta convecion tiene 2 reglas:

    1 - uso de minusculas para escribir la variable

        variable = X

    2 - si se compone de varia palabras, estas son unidas usando "_"

        hoa_soy_una_variable = x
"""

def snake_case() -> any:
    # crea una variable, dale un valor y retornala

    return  # colaca_la_antes_del_#


def snake_case2() -> any:
    # crea una nueva variable con un nuevo valor
    
    return  # colaca_la_antes_del_#

"""
    Normalmente Una variable escrita solo con mayusculas es
    para indicar una 'Constante'. 

    En otros lenguajes las constantes contienen valores que no pueden
    ser modificados, pero en Python no existen las constantes, sin 
    embargo existe la convecion de escribir todo en mayuscula para
    indicar que el valor contenido debe funcionar como tal.

    ejemplo:
        PI = 3.14 

    De este modo se entiende que PI es un valor que no debe ser modificado.    
"""


#####################################################################

# Operaciones con variables

#####################################################################


"""
    Las variables también funcionan como variables matematicas
    en una ecuación, es decir, que sus valores en cierto modo pueden ser modificados.
"""


def area_cuadrado(a: int) -> int:

    resultado = "?"
    return # no olvides retornar el resultado

def area_cubo(a: int) -> int:
    
    resultado = "?"
    return

def area_triangulo(base: int, altura: int) -> int:
    
    resultado = "?"
    return


"""
    Hay otras Operaciones que podemas realizar con otro tipo de datos
    y las variables, pero de momento con este manejo es suficiente.

    Una última cosa!!!!

    En álgebra, es normal usar una sola letra bara la variables,
    ya se trate de valore conocidos usando "A","B","C".... o
    valore desconocidos como "X","Y","Z"....


    En programacion, lo ideal es que el nombre describa el tipo 
    de dato que representa, como la base y la altura en la funcion
    de area_triangulo().
"""