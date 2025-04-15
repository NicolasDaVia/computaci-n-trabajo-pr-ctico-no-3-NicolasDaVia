from excepcion import NegativeNumberError

def ingrese_numero():
    
    entrada = input("Ingrese un número positivo para validar: ")
    try:
        valor = float(entrada)
    except ValueError:
        raise ValueError("La entrada debe ser un número.")

    if valor < 0:
        raise NegativeNumberError("El número debe ser positivo.")

    return valor

def main():
    try:
        numero = ingrese_numero()
        print(f"El número ingresado es válido: {numero}")
    except Exception as error:
        print(f"Error: {error}")

if __name__ == '__main__':
    main()
 