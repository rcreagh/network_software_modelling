#! usr/bin/python
"""This script experiments with Kruskal's greedy algorithm on a small random
complete undirected weighted graph."""

import networkx
import numpy
import kruskals_greedy_algorithm

def random_complete_undirected_weighted_graph(n):
  """Generate a complete undirected weighted graph.

  Args:
    n: Number of nodes in the graph
  Returns:
    Graph: Complete undirected weighted graph.
  """
  # Generate an nXn matrix.
  matrix_of_weights = numpy.random.random((n, n))
  graph = networkx.Graph()
  for i in range(n):
    for j in range(i+1, n):
      graph.add_edge(i, j, weight = matrix_of_weights[i, j])
  return graph

randomly_generated_graph = random_complete_undirected_weighted_graph(10)
minimal_spanning_tree = kruskals_greedy_algorithm.kruskal(randomly_generated_graph)
print (minimal_spanning_tree.edges(data=True))
