def calcular(num1, num2, opcion):

    if opcion == "1":
        return num1 + num2

    elif opcion == "2":
        return num1 - num2

    elif opcion == "3":
        return num1 * num2

    elif opcion == "4":
        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return num1 / num2

    else:
        raise ValueError("Opción no válida.")


def main():

    print("=== CALCULADORA EN PYTHON ===")

    while True:

        print("\nSelecciona una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == "5":
            print("Gracias por usar la calculadora.")
            break

        if opcion not in ["1", "2", "3", "4"]:
            print("Opción no válida.")
            continue

        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            resultado = calcular(num1, num2, opcion)

            print("Resultado:", resultado)

        except ValueError:
            print("Error: Ingresa números válidos.")

        except ZeroDivisionError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()