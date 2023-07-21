from variables import *
# import inspect

# def check_variable_in_function(func):
#     source_lines, _ = inspect.getsourcelines(func)
#     source_code = "".join(source_lines)
#     return "mi_variable" in source_code

# # Funciones de prueba
# def test_mi_variable_contains_mi_variable():
#     assert check_variable_in_function(mi_variable) is True


def test_mi_variable(capsys):
    mi_variable()
    stdout, stderr = capsys.readouterr()
    assert stdout == "42\n"

def test_mi_variable2(capsys):
    mi_variable2()
    stdout, stderr = capsys.readouterr()
    assert stdout == 42

def test_mi_variable3(capsys):
    mi_variable3()
    stdout, stderr = capsys.readouterr()
    assert stdout == 42

def test_mi_variable4(capsys):
    mi_variable4()
    stdout, stderr = capsys.readouterr()
    assert stdout == 42

def test_mi_variable5(capsys):
    assert mi_variable5() != None

def test_sanke_case():
    assert snake_case() != None

def test_sanke_case2():
    assert (snake_case2() != snake_case()) and (snake_case2() != None)


def test_area_cuadrado():
    assert area_cuadrado(3) ==  9
    assert area_cuadrado(11) == 121
    assert area_cuadrado(42) == 1764

def test_area_cubo():
    assert area_cubo(42) == 74088
    assert area_cubo(7) == 343
    assert area_cubo(.1) == 0.0010000000000000002

def test_area_triangulo():
    assert area_triangulo(42, 7) == 147.0
    assert area_triangulo(45, 3) == 67.5
    assert area_triangulo(99, 101) == 4999.5