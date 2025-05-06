def merge_sort(arr):
    if len(arr) > 1:
        mid, left, right = len(arr) // 2, arr[:mid], arr[mid:]
        merge_sort(left), merge_sort(right)
        arr[:] = [left.pop(0) if left and (not right or left[0] < right[0]) else right.pop(0) for _ in arr]
        # This step merges left and right efficiently, maintaining sorted order.

arr = list(map(int, input("Enter data to be sorted: ").split()))
print("Original:", arr)
merge_sort(arr)
print("Sorted:", arr)