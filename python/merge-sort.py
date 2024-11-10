# CLRS P1 C2 Merge Sort

def merge(A: List[int], l: int, m: int, r: int) -> None:
    llen = m - l + 1
    rlen = r - m
    
    L = [i for i in A[l:m + 1]]
    R = [i for i in A[m:r]]

    k = l
    q = 0
    p = 0

    while q < llen  and p < rlen:
        if L[q] > R[p]:
            A[k] = R[p]
            p += 1
        else:
            A[k] = L[q]
            q += 1
        k += 1

    while q < llen:
        A[k] = L[q]
        q += 1; k += 1
    while p < rlen:
        A[k] = R[p]
        p += 1; k += 1

def merge_sort(A: List[int], l: int, r: int) -> None:
    if l == r:
        return
    m = (r-l) / 2
    merge_sort(A, l, m)
    merge_sort(A, m + 1, r)
    merge(A, l, m, r)
