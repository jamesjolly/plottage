#!/usr/bin/python
"""
dagfucius 0.1
Copyright (C) 2013, James Jolly
See MIT-LICENSE.txt for legalese and README.md for usage.
"""

from collections import defaultdict

class dagfucius:

	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, node_from, node_to, weight=0):
		self.graph[node_from].append((node_to, weight))

	def __iter__(self):
		return self.walk()

	def walk(self):
		for node_from, edges in self.graph.items():
			for node_to, weight in edges:
				yield (node_from, node_to, weight)

	def __repr__(self):
		dot = "digraph {"
		for node_from, node_to, weight in self:
			dot += "".join([node_from, " -> ", node_to, " [weight=", str(weight), "];\n"])
		dot += "}"
		return dot

