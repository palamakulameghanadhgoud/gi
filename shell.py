def shell_sort(arr):
    gap = len(arr) // 2
    while gap:
        for i in range(gap, len(arr)):
            j, temp = i, arr[i]
            while j >= gap and arr[j - gap] > temp:
                arr[j], j = arr[j - gap], j - gap
            arr[j] = temp
        gap //= 2

arr = list(map(int, input().split()))
print("Original:", arr)
shell_sort(arr)
print("Sorted:", arr)