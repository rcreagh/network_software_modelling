#! usr/bin/python
""" This script is a naive implementation of breadth first search using the
Networkx pachage for my own learning purposes."""

def breadth_first_search(graph, root_vertex):
  """ Traverse a graph breadth first. NOTE: This is WIP.

  Args:
    graph: The graph we want to traverse.
    root_vertex: The root vertex we will traverse from.
  Returns:
    Currently, all vertices in the tree or subgraph. Ultimately, will also
    return the parent of each vertex and distance from the root vertex."""
  
  sub_graph = set()
  queue = []
  queue.append(root_vertex)
  while len(queue) > 0:
    current_vertex = queue[0]
    del queue[0]
    for s in graph.neighbors(current_vertex):
      if s not in sub_graph:
        sub_graph.add(s)
        queue.append(s)
  return sub_graph        
