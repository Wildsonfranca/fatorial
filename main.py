# from math import factorial
# n = int(input('Digite um numero para calcular seu fatorial:'))
# f = factorial(n)
# print('O fatorial de {} é {}.'.format(n,f))
#modo tradicional
#numero = int(input('informe um numero para saber o seu fatorial:'))
# if numero > 0:
#     fatorial =1
#     for item in range(1,numero +1):
#         fatorial = fatorial * item
#     print(fatorial)    
# função oara calcular fatorial 
def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n-1)
   
# programa principal 
n = int(input('Informe um numero inteiro:'))

# exibe o resultado o fatorial
print(f'Fatorial de {n}: {calcular_fatorial(n)}.')

   
    