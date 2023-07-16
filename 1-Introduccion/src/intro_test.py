from intro import *

def test_hello():
	assert hello() == "Hello World!"
	

def test_hola():
	assert hola() == "¡Hola Mundo!"
	
def test_string():
	assert string() == "Esto es un string"

def test_hola_otra_vez(capsys):
	hola_otra_vez()
	stdout, stderr = capsys.readouterr()
	assert stdout == "¡Hola Mundo!\n"

def test_monty_python(capsys):
	monty_python()
	stdout, stderr = capsys.readouterr()
	assert stdout == "'Are you suggesting coconuts migrate?'\n"
	
def test_alert(capsys):
	alert()
	stdout, stderr = capsys.readouterr()
	assert stdout == "Alert! Alert! Alert! \n"
	
def test_separador(capsys):
	separador()
	stdout, stderr = capsys.readouterr()
	assert stdout == "Alert-Alert-Alert\n"
	
	
def test_ends(capsys):
	ends()
	stdout, stderr = capsys.readouterr()
	assert stdout == "Hola!"


#####################################
    # Operaciones
#####################################

def test_suma():
	assert suma() == 7
	
def test_suma2():
	assert suma2(5, 9) == 14
	assert suma2(542 , 753) == 1295
	assert suma2( -45321, 35431) == -9890

def test_resta():
	assert resta() == 1

def test_resta2():
	assert resta2(22, 17) == 5
	assert resta2(754, 684) == 70
	assert resta2(186, 295) == -109
	
def test_resta3():
	assert resta2(22, 17, 1) == 4
	assert resta2(754, 484, 102) == 1687
	assert resta2(186, 295, 33) == -142

def test_mul():
	assert mul(5, 9) == 45
	assert mul(47, 13) == 661
	
def test_mul2():
	assert mul2(7, 9) == 63
	assert mul2(42, 13) == 546
	
def test_div():
	assert div(5, 2) == 2.5
	assert div(81, 3) == 27
	assert div(465, -5) == -93
	
def test_div2():
	assert div2(5, 2) == 2
	assert div2(81, 7) == 11
	assert div2(465, 35) == 13
	
def test_div3():
	assert div3(5, 2) == 1
	assert div3(81, 7) == 4
	assert div3(465, 35) == 10
	