"""
Programa que retorna el último dígito de un número natural n (leído de izquierda a derecha sin usar strings ni listas ni tuplas ni residuo de la división)
"""

def ultimoV1(i):
	return  i-10 if i-10<10 else ultimoV1(i-10)

print(ultimoV1(9989))


def ultimoV2(i,potencia):
	if i/potencia<10:
		return i-(i//potencia)*potencia
	else:
		return ultimoV2(ultimoV2(i,potencia*10),potencia*10)

print(ultimoV2(987654327987654321234567890,1))