from excepcion import NegativeNumberError


def main():
    try:
        numero = ingrese_numero()
        print(f"El número ingresado es válido: {numero}")
    except Exception as error:
        print(f"Error: {error}")

if __name__ == '__main__':
    main()
 