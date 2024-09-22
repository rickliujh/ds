package main

func Heapsort[T any](arr *[]T, cmp compare[T]) []T {
	heap := &Heap[T]{
		size: len(*arr),
		arr:  append(make([]T, 1), *arr...),
		cmp:  cmp,
	}

	heap.buildHeap()
	for i := heap.size; i > 1; i-- {
		heap.swap(1, i)
		heap.heapify(1, heap.swap)
	}

	return heap.arr[1:]
}

type compare[T any] func(l, r T) int

type Heap[T any] struct {
	size int
	arr  []T
	cmp  compare[T]
}

func (h *Heap[T]) leftChild(pidx int) int {
	return 2 * pidx
}

func (h *Heap[T]) rightChild(pidx int) int {
	return 2*pidx + 1
}

func (h *Heap[T]) parent(cidx int) int {
	if cidx == 1 {
		return 1
	}
	return cidx / 2
}

func (h *Heap[T]) swap(a, b int) {
	tmp := h.arr[a]
	h.arr[a] = h.arr[b]
	h.arr[b] = tmp
}

func (h *Heap[T]) heapify(i int, swap func(i, j int)) {
	if i > h.size {
		return
	}

	l := h.leftChild(i)
	r := h.rightChild(i)

	largest := i
	if l <= h.size && h.cmp(h.arr[l], h.arr[largest]) > 0 {
		largest = l
	}
	if r <= h.size && h.cmp(h.arr[r], h.arr[largest]) > 0 {
		largest = r
	}

	if largest != i {
		swap(largest, i)
		h.heapify(largest, swap)
	}
}

func (h *Heap[T]) buildHeap() {
	for i := range h.size / 2 {
		h.heapify(i, h.swap)
	}
}

type Id[T any, ID comparable] func(t T) ID

type PriorityQueue[T any] struct {
	Heap[T]
	indexes map[any]int
	id      Id[T, any]
}

func NewPriorityQueue[T any](cmp compare[T], id Id[T, any]) PriorityQueue[T] {
	return PriorityQueue[T]{
		Heap[T]{
			size: 0,
			arr:  make([]T, 10),
			cmp:  cmp,
		},
		map[any]int{},
		id,
	}
}

func (q *PriorityQueue[T]) Peek() T {
	return q.arr[1]
}

func (q *PriorityQueue[T]) Pop() T {
	obj := q.arr[1]
	q.swap(1, q.size)
	q.size--
	q.heapify(1)
	delete(q.indexes, q.id(obj))
	return obj
}

func (q *PriorityQueue[T]) Push(obj T) {
	q.size++
	i := q.size

	if len(q.arr) <= i {
		q.arr = append(q.arr, obj)
	} else {
		q.arr[i] = obj
	}
	q.indexes[q.id(obj)] = i

	q.yfipaeh(obj, i)
}

func (q *PriorityQueue[T]) swap(l, r int) {
	idl := q.id(q.arr[l])
	idr := q.id(q.arr[r])
	q.Heap.swap(l, r)
	q.indexes[idl] = r
	q.indexes[idr] = l
}

// heapify from top down
func (q *PriorityQueue[T]) heapify(i int) {
	q.Heap.heapify(i, q.swap)
}

// yfipaeh from bottom up
func (q *PriorityQueue[T]) yfipaeh(obj T, i int) {
	for ; i > 1 && q.cmp(q.arr[q.parent(i)], q.arr[i]) < 0; i = q.parent(i) {
		q.swap(i, q.parent(i))
	}
}

func (q *PriorityQueue[T]) Modify(obj T) {
	i := q.indexes[q.id(obj)]

	old := q.arr[i]
	q.arr[i] = obj

	if q.cmp(obj, old) <= 0 { // if val of index i decreases
		// build the heap top down from i
		q.heapify(i)
		return
	} else { // if val of index i increases
		// adjust heap bottom up
		q.yfipaeh(obj, i)
	}
}
