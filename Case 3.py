def sum_negative_between_max_min(arr):
    # Если в массиве меньше 2 элементов, между ними ничего быть не может
    if len(arr) < 2:
        return 0
        
    # Находим индексы первого встреченного максимального и минимального элементов
    max_idx = arr.index(max(arr))
    min_idx = arr.index(min(arr))
    
    # Определяем, какой индекс меньше (левая граница), а какой больше (правая граница)
    left_bound = min(max_idx, min_idx)
    right_bound = max(max_idx, min_idx)
    
    # Инициализируем сумму нулем
    total_sum = 0
    
    # Проходим по элементам строго между левой и правой границей
    # не включает сами границы
    for i in range(left_bound + 1, right_bound):
        if arr[i] < 0:
            total_sum += arr[i]
            
    return total_sum

# Пример использования:
# Максимум = 10 (индекс 3), Минимум = -9 (индекс 6)
# Элементы между ними: -5, 2. Отрицательный из них только -5.
A = [3, -1, 4, 10, -5, 2, -9, 7]
result = sum_negative_between_max_min(A)
print(f"Сумма отрицательных элементов между максимумом и минимумом: {result}")