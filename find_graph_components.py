#! /usr/bin/python
"""This script is for finding all the components in a graph genrated by the
networkx library using depth first search."""

import networkx

def find_components(graph):
  """Find all components of a graph.

  Args:
    graph: Graph made up of vertices and edges.
  Yields:
    Each component in the graph.
  """
  seen_vertices = set()
  for vertex in graph.nodes():
    if vertex not in seen_vertices:
      component = find_individual_component(graph, vertex)
      yield component
      seen_vertices.update(component)

def find_individual_component(graph, vertex):
  """Find the component containing vertex.

  Args:
    graph: Graph made up of vertices and edges.
    vertex: Single vertex in graph.
  Returns:
    Component containing vertex.
  """
  component = set()
  component.add(vertex)
  _find_component(graph, vertex, component)
  return component

def _find_component(graph, vertex, component):
  """ Function to aid in finding all vertices in the same component as vertex.
  Args:
    graph: Graph made up of vertices and edges. 
    vertex: Single vertex in graph.
    component: Component containing vertex.
  """
  for n in graph.neighbors(vertex):
    if n not in component:
      component.add(n)
      _find_component(graph, n, component)
