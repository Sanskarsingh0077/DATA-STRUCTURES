def selection_sort(arr):
    a = arr.copy()
    n = len(a)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j

        a[i], a[min_idx] = a[min_idx], a[i]

    return a


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", arr)
    print("Selection Sort:", selection_sort(arr))