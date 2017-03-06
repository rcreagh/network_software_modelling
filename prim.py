#! usr/bin/python
"""This script is an implementation of Prim's greedy algorithm for learning
purposes. Prim's algorithm is a greedy approach to finding a (there may be more
than one) minimal spanning tree of a graph, using Python's networkx library."""

import networkx

def prim(graph):
  """ Implementation of Prim's Greedy Algorithm.

  Args:
    graph: Graph which we are trying to find a minimal spanning tree for.
  """

  # Initialize count of the number of nodes in the tree.
  current_tree_size = 0

  seen_nodes = set()
  unseen_nodes = set()

  for i in range(len(edges)):
    unseen_nodes.add(graph[i])

TODO: COMPLETE
