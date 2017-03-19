#! usr/bin/python
"""This script is an implementation of Prim's greedy algorithm for learning
purposes. Prim's algorithm is a greedy approach to finding a (there may be more
than one) minimal spanning tree of a graph, using Python's networkx library."""

import math
import networkx
import priority_queue
import random

def prim(graph, root_node):
  """ Implementation of Prim's Greedy Algorithm.

  Args:
    graph: Graph which we are trying to find a minimal spanning tree for.
  """

  seen_nodes = []
  queue = [] # TODO - alter priority queue to be suitable for this problem.
  parents = {root_node: None}

  queue.append((root_node, 0))

  n, p = min(queue)

  while queue:
  next_node, priority = min(queue)

# TODO: COMPLETE
