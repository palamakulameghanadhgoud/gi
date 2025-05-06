def insertion_sort(arr):
    for i in range(1, len(arr)):
        key, j = arr[i], i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = list(map(int, input("Enter list with spaces: ").split()))
print(f"Original: {arr}")
insertion_sort(arr)
print(f"Sorted: {arr}")