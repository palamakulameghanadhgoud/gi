def heapify(arr, n, i):
    key = arr[i]  # Initialize largest as root
    j = 2 * i  # left child index (1-based index)

    while j <= n:
        if j < n and arr[j] < arr[j+1]:
            j+=1
        if arr[j] > key:
            arr[j//2] = arr[j]
            j = 2*j
        else:
            break
    arr[j//2] = key

def heap_sort(arr):
    n = len(arr) - 1  # Adjust for 1-based index

    # Build a max heap
    for i in range(n // 2, 0, -1):
        heapify(arr, n, i)

    i = n
    while i >= 1:
        arr[1], arr[i] = arr[i], arr[1]
        i -= 1
        heapify(arr, i, 1)


# Example usage (1-based index, so prepend a dummy element)
user_input = list(map(int, input("Enter space-separated integers: ").split()))
arr = [None] + user_input  # Prepend a dummy element to maintain 1-based index
print("before sorting ",arr[1:])
heap_sort(arr)
print("Sorted array:", arr[1:])
