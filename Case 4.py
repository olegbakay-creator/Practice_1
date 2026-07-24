N = int(input("Введите количество голов: "))

print(f"Введено число: {N}")

if N <= 3:
    # Если голов 1, 2 или 3, один дракон со всеми головами — лучший вариант
    result = N
    print(f"N <= 3, поэтому результат = {N}")
else:
    # Для N > 3 используем оптимальную стратегию с тройками и двойками
    remainder = N % 3
    quotient = N // 3
    
    print(f"N > 3")
    print(f"Остаток от деления на 3: {remainder}")
    print(f"Частное от деления на 3: {quotient}")
    
    if remainder == 0:
        # Все тройки
        result = 3 ** quotient
        print(f"Остаток 0: используем {quotient} троек")
    elif remainder == 1:
        # Одна тройка превращается в две двойки
        result = 3 ** (quotient - 1) * 4
        print(f"Остаток 1: используем {quotient - 1} троек и 2 двойки (умножаем на 4)")
    else:  # remainder == 2
        # Все тройки и одна двойка
        result = 3 ** quotient * 2
        print(f"Остаток 2: используем {quotient} троек и 1 двойку")

print(f"\nИтоговый результат: {result}")