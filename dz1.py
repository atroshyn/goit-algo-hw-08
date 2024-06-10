import heapq

def min_cost_to_connect_cables(cable_lengths):
    # Ініціалізація мінімальної купи
    heapq.heapify(cable_lengths)
    total_cost = 0

    # Поки в купі більше одного кабелю
    while len(cable_lengths) > 1:
        # Витягнути два найменші кабелі
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        # Об'єднати їх і додати результат назад до купи
        combined_length = first + second
        heapq.heappush(cable_lengths, combined_length)

        # Додати витрати на об'єднання до загальних витрат
        total_cost += combined_length

    return total_cost

# Приклад використання
cable_lengths = [4, 3, 2, 6]
print("Мінімальні витрати на об'єднання кабелів:", min_cost_to_connect_cables(cable_lengths))  # Мінімальні витрати на об'єднання кабелів: 29
