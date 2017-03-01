#! usr/bin/python
""" This script implements a min_2_heap data structure. This is for educational
purposes only. In practice, an ready built module would be used.

#TODO Add doc strings and tests.

def parent(i):
    return (i - 1) // 2 # Force integer division.

def left_child(i):
    return 2 * i + 1

def right_child(i):
    return 2 * i + 2

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

def siftup(L, i):
    p = parent(i)
    if p < 0: return # no parent: nowhere to go
    while L[p] > L[i]:
        swap(L, i, p) # swap and ascend
        i = p
        p = parent(i)
        if p < 0: return

def siftdown(L, i):
    while True:
        c0 = left_child(L, i)
        c1 = right_child(L, i) # ie c0+1
        if c1 < len(L) and L[c1] < L[c]:
            # right child exists, and is smaller than left
            # so consider right child only
            c = c1
        else:
            # consider left only
            c = c0

        if c < len(L) and L[i] > L[c]:
            # c exists, and is smaller than its parent
            # so swap and iterate
            swap(L, i, c)
            i = c
        else:
            # no swap -> we are finished
            return

def popmin(L):
    m = L[0] # get min
    L[0] = L[-1] # move last element of last layer to root
    del L[-1]
    siftdown(L, 0) # siftdown from root
    return m

def add(L, x):
    L.append(x) # put x after last element of last layer
    siftup(L, len(L) - 1) # siftup from the element we just added
