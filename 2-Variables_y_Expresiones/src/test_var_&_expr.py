from variables import *
import inspect

def check_variable_in_function(func):
    source_lines, _ = inspect.getsourcelines(func)
    source_code = "".join(source_lines)
    return "mi_variable" in source_code

# Funciones de prueba
def test_mi_variable_contains_mi_variable():
    assert check_variable_in_function(mi_variable) is True