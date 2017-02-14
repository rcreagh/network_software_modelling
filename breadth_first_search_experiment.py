#! /usr/bin/python
"""This script is to implement the find_graph_components algorithm on a
small randomly generated graph, generated by the networkx library."""

import networkx
import breadth_first_search

graph = networkx.generators.random_graphs.gnm_random_graph(25, 20)

nodes_in_sub_graph = breadth_first_search.breadth_first_search(graph, 5)
print(nodes_in_sub_graph)
