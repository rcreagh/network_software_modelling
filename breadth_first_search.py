#! usr/bin/python
""" This script is a naive implementation of breadth first search using the
Networkx pachage for my own learning purposes."""

class Vertex(object):
  def __init__(self, name, parent, depth):
    """Initialize vertex.

    Args:
      name: Arbitrary name of the node
      parent: Parent vertex of the vertex in a tree.
      depth: Number of edges between the vertex itself and the root vertex.
    """
    self.name = name
    self.parent = parent
    self.depth = depth

def breadth_first_search(graph, root_vertex):
  """ Traverse a graph breadth first. NOTE: This is WIP.

  Args:
    graph: The graph we want to traverse.
    root_vertex: The root vertex we will traverse from.
  Returns:
    Currently, all vertices in the tree or subgraph. Ultimately, will also
    return the parent of each vertex and distance from the root vertex."""
  
  sub_graph = []
  queue = []
  # Set initial distance from root vertex.
  current_distance_from_root_vertex = 0
  # Add root node to sub_graph.
  sub_graph.append(Vertex(root_vertex, None, 0))
  queue.append(root_vertex)
  while len(queue) > 0:
    current_vertex = queue[0]
    del queue[0]
    current_distance_from_root_vertex += 1
    for s in graph.neighbors(current_vertex):
      if s not in [data.name for data in sub_graph]:
        new_vertex = Vertex(
          s, current_vertex, current_distance_from_root_vertex)
        sub_graph.append(new_vertex)
        queue.append(s)
  return sub_graph
