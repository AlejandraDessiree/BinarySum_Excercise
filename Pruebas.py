numero_usario = str(input("binario y decimal "))
lista = numero_usario.split(" ")

num1 = lista[0]
num2 = lista[1]

def valor(numero):
    for i in numero:
        if i in '10':
            binario = True
        else:
            binario = False
    return binario

def binario(numero):
    longitud = len(numero)
    decimal = 0
    for i in range(longitud):
        valor = int(numero[i])
        exponente = longitud -  i - 1
        decimal += valor * (2 ** exponente)
    return decimal
    
def decimal(numero):
    numero = int(numero)
    binario = []
    while numero > 0:
        residuo = numero % 2
        binario.append(str(residuo))
        numero = numero // 2
        
    binario.reverse()
    binario_inv = "".join(binario)
    return binario_inv
    
decimal_1 = binario(num1)
num2 = int(num2)
suma = decimal_1 + num2
print(f"La suma en binario es: {decimal(suma)}")