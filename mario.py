# Solicitar los numeros
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Mostrar menu de operaciones
print("\nElige la operación que deseas realizar:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingresa el número de la opción: ")

# Evaluar la opción seleccionada
if opcion == "1":
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)
elif opcion == "2":
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)
elif opcion == "3":
    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)
elif opcion == "4":
    if num2 != 0:  # Evitar división entre cero
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
    else:
        print("Error: No se puede dividir entre cero")
else:
    print("Opción no válida")