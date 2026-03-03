def suma(a: int, b: int) -> int:
    return a + b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir por 0")
    return a / b


def main():
    print(suma(2, 3))
    print(divide(10, 2))

if __name__ == "__main__":
    main()