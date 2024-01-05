import time
import json

def generar_secuencia_fibonacci(n):
    secuencia_fibonacci = [0, 1]
    for i in range(2, n):
        secuencia_fibonacci.append(secuencia_fibonacci[i-1] + secuencia_fibonacci[i-2])
    return secuencia_fibonacci

print("Secuencia de Fibonacci (10 primeros números)")
print(generar_secuencia_fibonacci(10))
print()

def fib_naive(n):
    if n <= 1:
        return n
    else:
        return fib_naive(n-1) + fib_naive(n-2)

print("Solución Recursiva Ingenua")
print("fib(5):", fib_naive(5))  
print("fib(6):", fib_naive(6)) 
print()

print("Identificar Subproblemas Superpuestos")
print("fib(5) =", fib_naive(5))
print()


def fib_memo(n, memo={}):
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

print("Implementar Memoización")
print("fib_memo(5):", fib_memo(5)) 
print("fib_memo(6):", fib_memo(6))  
print()

def medir_tiempo(func, *args):
    tiempo_inicio = time.time()
    resultado = func(*args)
    tiempo_fin = time.time()
    return resultado, tiempo_fin - tiempo_inicio

resultado_ingenuo, tiempo_ingenuo = medir_tiempo(fib_naive, 30)

resultado_memo, tiempo_memo = medir_tiempo(fib_memo, 30)

print("Medir la Diferencia de Tiempo")
print("Enfoque Ingenuo - Resultado:", resultado_ingenuo, "Tiempo:", tiempo_ingenuo)
print("Enfoque con Memoización - Resultado:", resultado_memo, "Tiempo:", tiempo_memo)
print()

datos_memorización = {}
fib_memo(30, datos_memorización)  
with open('datos_memo.json', 'w') as archivo_json:
    json.dump(datos_memorización, archivo_json)
print("Datos de Memoización almacenados en 'datos_memo.json'")
