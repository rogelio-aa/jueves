# EJERCICIO NUMERO 1
print(sorted([int(input("ingrese el numero: ")) for _ in range (5)]))


# EJERCICIO NUMERO 2
lista1 = list(map(int, input("Ingrese 5 números para la primera lista: ").split()))
lista2 = list(map(int, input("Ingrese 5 números para la segunda lista: ").split())); resultado = [a * b for a, b in zip(lista1, lista2)]; print(resultado)