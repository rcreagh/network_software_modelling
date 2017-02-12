#! usr/bin/python
"""This script implements Kruskal's greedy algorithm for finding the minimum 
spanning tree of a graph. This is a naive and inefficient approach and is for
learning purposes only."""

import networkx
import find_graph_components

def kruskal(graph):
  """Kruskal's minimum spanning tree algorithm.

  Args:
    graph: A weighted graph.
  Returns:
    Minimum spanning tree.
  """
  # Create a graph with the same nodes as graph and no edges.
  minimum_spanning_tree = networkx.Graph()
  for i in graph.nodes():
    minimum_spanning_tree.add_node(i)

  # Track the size of the tree
  current_tree_size = 0

  # Make a list from the edges of graph.
  edges = list(graph.edges(data=True))
  for i in range(len(edges)):
    edge = min(edges, key=lambda e: e[2]["weight"])
    edges.remove(edge)
    # If edge points in same component already, would create a cycle.
    if edge[1] in find_graph_components.find_individual_component(
        minimum_spanning_tree, edge[0]):
      pass
    else:
      minimum_spanning_tree.add_edge(edge[0], edge[1], weight=edge[2]["weight"])
      # Increase current tree size by 1
      current_tree_size += 1
    # Stop if tree size is equal to number of nodes - 1
    if current_tree_size >= graph.order():
      break
  return minimum_spanning_tree
