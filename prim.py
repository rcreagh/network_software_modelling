#! usr/bin/python
"""This script is an implementation of Prim's greedy algorithm for learning
purposes. Prim's algorithm is a greedy approach to finding a (there may be more
than one) minimal spanning tree of a graph, using Python's networkx library."""

import math
import networkx
import priority_queue
import random

# NOTE: WIP

def prim(graph, root_node):
  """ Implementation of Prim's Greedy Algorithm.

  Args:
    graph: Graph which we are trying to find a minimal spanning tree for.
  """

  seen_nodes = []
  queue = [] # TODO - alter priority queue to be suitable for this problem.
  parents = {root_node: None}

  queue.append((0, root_node))

  while queue:
    priority, next_node = min(queue)
    for neighbor in graph.neighbors(next_node):
      if neighbor in queue:
        if graph[next_node][neighbor]['weight'] < queue[]

# TODO: COMPLETE
