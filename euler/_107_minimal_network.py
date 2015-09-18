"""
Client of EdgeWeightedGraph and KruskalMST. Finds the maximum reduction
in edge weight obtained by removing edges from a graph such that the
remaining edges still span the graph.

The graph is parsed from an input file passed to this script via a
positional argument.

--------------------

execution:
python euler/_107_minimal_network.py euler/assets/107_network.txt

output:
259679
Duration: 0.0077478885650634766s
"""

import sys, time

from lib.graph_edge import Edge, EdgeWeightedGraph
from lib.mst import KruskalMST

start_time = time.time()
with open(sys.argv[1]) as f:
    # read through file to determine number of vertices in graph
    g = EdgeWeightedGraph(len(f.readlines()))
with open(sys.argv[1]) as f:
    for i, line in enumerate(f):
        weights = line.strip().split(',')
        for j, weight in enumerate(weights):
            if j >= i and weight != '-':
                g.add_edge(Edge(i, j, int(weight)))

mst = KruskalMST(g)
reduction = 0
for e in g.edges():
    if e not in mst.mst:
        reduction += e.get_weight()

print(reduction)
print('Duration: {0}s'.format(time.time() - start_time))


