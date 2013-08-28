
from collections import defaultdict

class graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, node_from, node_to, weight=0):
		self.graph[node_from].append((node_to, weight))

	def __iter__(self):
		return self.iter_edges()

	def iter_edges(self):
		for node_from, edges in self.graph.items():
			for node_to, weight in edges:
				yield (node_from, node_to, weight)

	def search(self, start_node, search_type="bfs"):
		q = [start_node]
		visited = set()
		while len(q) > 0:
			node_id = q.pop() if search_type == "dfs" else q.pop(0)
			if node_id in visited:
			  continue
			visited.add(node_id)
			yield node_id
			for child_id, child_weight in self.graph[node_id]:
				q.append(child_id)

	def bfs(self, start_node):
		return self.search(start_node, search_type="bfs")

	def dfs(self, start_node):
		return self.search(start_node, search_type="dfs")

	def __repr__(self):
		dot = "digraph {\n"
		for node_from, node_to, weight in self:
			dot += "%s -> %s [weight=%s];\n" \
				% (node_from, node_to, str(weight))
		dot += "}"
		return dot

