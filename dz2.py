def merge_k_lists(lists):
    min_heap = []
    
    # Додавання перших елементів кожного списку до купи
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i][0], i, 0))

    merged_list = []
    
    while min_heap:
        value, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(value)

        # Якщо вийнятий елемент не останній у своєму списку, додати наступний елемент цього списку до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)  # Відсортований список: [1, 1, 2, 3, 4, 4, 5, 6]
