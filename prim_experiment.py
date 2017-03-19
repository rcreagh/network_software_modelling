import networkx
import prim

graph = networkx.generators.random_graphs.gnm_random_graph(25, 20)

prim.prim(graph, 1)
