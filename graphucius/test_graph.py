#!/usr/bin/python
"""
plottage 0.1
Copyright (C) 2013, James Jolly
See MIT-LICENSE.txt for legalese and README.md for usage.
"""

from graphucius import graph
import unittest

class TestGraph(unittest.TestCase):

  def setUp(self):
    self.c_EDGES = [
      (0, 1, 0),
      (1, 2, 0),
      (1, 3, 0),
      (1, 4, 0),
      (3, 5, 0)
    ]
    self.graph = graph()
    for node_from, node_to, weight in self.c_EDGES:
      self.graph.add_edge(node_from, node_to, weight)

  def test_bfs(self):
    nodes = [node_id for node_id in self.graph.bfs(0)]
    self.assertEqual(nodes, range(6))
  
  def test_dfs(self):
    nodes = [node_id for node_id in self.graph.dfs(0)]
    self.assertEqual(nodes, [0, 1, 4, 3, 5, 2])

  def test_iter_edges(self):    
    edges_listed = [edge for edge in self.graph.iter_edges()]
    self.assertEqual(self.c_EDGES, edges_listed)

if __name__ == '__main__':
    unittest.main()

