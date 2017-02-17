#! usr/bin/python
""" This script is a naive implementation of breadth first search using the
Networkx pachage for my own learning purposes."""

import networkx
import vertex
from collections import deque

def naive_breadth_first_search(graph, root_vertex):
  """ Traverse a graph breadth first. NOTE: This is WIP.

  Args:
    graph: The graph we want to traverse.
    root_vertex: The root vertex we will traverse from.
  Returns:
    Currently, all vertices in the tree or subgraph. Ultimately, will also
    return the parent of each vertex and distance from the root vertex."""
  
  sub_graph = []
  queue = []
  # Add root node to sub_graph.
  sub_graph.append(vertex.Vertex(root_vertex, None, 0))
  queue.append(vertex.Vertex(root_vertex, None, 0))
  while len(queue) > 0:
    current_vertex = queue[0]
    del queue[0]
    for s in graph.neighbors(current_vertex.name):
      if s not in [data.name for data in sub_graph]:
        new_vertex = vertex.Vertex(
          s, current_vertex.name, current_vertex.depth + 1)
        sub_graph.append(new_vertex)
        queue.append(new_vertex)
  return sub_graph
