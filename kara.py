def karatsuba(x, y):
    # Converte para strings para facilitar a manipulação dos dígitos
    x_str, y_str = str(x), str(y)

    # Condição de base para a recursão
    if len(x_str) == 1 or len(y_str) == 1:
        return x * y

    # Encontrando o ponto médio para dividir os números
    n = max(len(x_str), len(y_str))
    m = n // 2

    # Divide os números em partes menores
    a, b = int(x_str[:-m] or 0), int(x_str[-m:] or 0)
    c, d = int(y_str[:-m] or 0), int(y_str[-m:] or 0)

    # Recursivamente calcula os produtos interiores
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    # Calcula o resultado final usando os produtos interiores
    result = (10**(2*m) * ac) + (10**m * ad_bc) + bd

    return result

def test_karatsuba():
    # Exercício 1
    result1 = karatsuba(1234, 5678)
    result2 = karatsuba(11111111, 22222222)
    result3 = karatsuba(12345678, 87654321)

    print("Exercício 1:")
    print("1234 * 5678 =", result1)
    print("11111111 * 22222222 =", result2)
    print("12345678 * 87654321 =", result3)

    # Exercício 2
    result4 = karatsuba(123, 456789)
    result5 = karatsuba(12345, 678)
    result6 = karatsuba(123456, 7890123)

    print("\nExercício 2:")
    print("123 * 456789 =", result4)
    print("12345 * 678 =", result5)
    print("123456 * 7890123 =", result6)

    # Exercício 3
    import time

    sizes = [10, 50, 100]
    for size in sizes:
        num1 = int('1' + '0' * (size - 1))
        num2 = int('1' + '0' * (size - 1))

        start_time = time.time()
        _ = karatsuba(num1, num2)
        karatsuba_time = time.time() - start_time

        start_time = time.time()
        _ = num1 * num2
        traditional_time = time.time() - start_time

        print(f"\nExercício 3 - Tamanho: {size} dígitos")
        print("Tempo (Karatsuba):", karatsuba_time)
        print("Tempo (Multiplicação Tradicional):", traditional_time)

if __name__ == "__main__":
    test_karatsuba()
