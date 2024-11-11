# CLRS P2 C7 Quick Sort

def partition(A: List[int], s: int, e: int) -> int:
    l = s; h = s
    pivot = A[e]
    while h < e:
        if A[h] <= pivot:
            a[l], a[h] = a[h], a[l]
            l += 1
        h += 1
    A[l], A[e] = A[e], A[l]
    return l

def quick_sort(A: List[int], s: int, e: int) -> None:
    if s < e:
        pivot = partition(A, s, e)
        quick_sort(A, s, pivot - 1)
        quick_sort(A, pivot + 1, e)

