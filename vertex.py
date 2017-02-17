#! usr/bin/python
"""This script creates an object of class vertex."""

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

  def __repr__(self):
    """Change print format to show name, parent and depth of vertices."""
    return '\n' + str(
      self.name) + ', ' + str(self.parent) + ', ' + str(self.depth)
