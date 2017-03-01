#! usr/bin/python
""" This script implements a min_2_heap data structure. This is for educational
purposes only. In practice, an ready built module would be used.

#TODO Add doc strings and tests.

def parent(i):
  """ Get the parent of a given node.

  Args:
    i: Integer - the index of the node in question.
  """
  # Force integer division. Therefore, regardless of the branch, the parent
  # node will be returned.
  return (i - 1) // 2

def left_child(i):
  """ Get the left child of a given node.

  Args:
    i: Integer - the index of the node in question.
  """
  return 2 * i + 1

def right_child(i):
  """ Get the right child of a given node.

  Args:
    i: Integer - the index of the node in question.
  """
  return 2 * i + 2

def swap(L, i, j):
  """ Swaps two nodes.

  Args:
    L: List - current heap.
    i: Integer - node 1 to be swapped.
    j: Integer - node 2 to be swapped.
 """
  L[i], L[j] = L[j], L[i]

def siftup(L, i):
  """ Loop which swaps a node with its parent as long as the value of the
  parent is smaller than the value of the node.

  Args:
    L: List - current heap.
    i: Integer - the index of the node in question.
  """
  p = parent(i)
  # p can only be 0 if already at the root node, as we parent(i) returns
  # (i - 1) // 2.
  if p < 0: return
  while L[p] > L[i]:
    swap(L, i, p) # swap and ascend
    i = p
    p = parent(i)
    if p < 0: return

def siftdown(L, i):
  """ If a parent is larger than either one of its children, it swaps with it.

  Args:
    L: List - our current heap.
    i: Integer - the index of the node in question.
  """
  while True:
    c0 = left_child(L, i)
    c1 = right_child(L, i)
    if c1 < len(L) and L[c1] < L[c]:
      # Right child exists, and is smaller than left, so consider right child
      # only.
      c = c1
    else:
      # Consider left only.
      c = c0

    if c < len(L) and L[i] > L[c]:
      # c exists, and is smaller than its parent, so swap and iterate
      swap(L, i, c)
      i = c
    else:
      return

def popmin(L):
  """ This is the key activity. Pops out the lowest priority node and replaces
  it with the last node in the heap, then sifts this node down.

  Args:
    L: List - our current heap.
  Returns:
    m: Lowest priority node in the heap.
  """
  m = L[0] # get min
  L[0] = L[-1] # move last element of last layer to root
  del L[-1]
  siftdown(L, 0) # siftdown from root
  return m

def add(L, x):
  """ Add a new node to the heap.

  Args:
    L: List - our current heap.
    x: Node to be added to the heap.
  """   
  L.append(x) # put x after last element of last layer
  siftup(L, len(L) - 1) # siftup from the element we just added
