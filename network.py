import pathlib
import json
from typing import Any, Iterable
from collections import deque
from itertools import count

from pygame import Vector2

Node = int
Edge = tuple[Node, Node]


class Network:
    """Directed Graph object."""
    def __init__(self, 
            adj: dict[Node, list[Node]] | None = None, 
            nodes_positions: dict[Node, Vector2] | None = None,
            node_data: dict[Node, Any] | None = None
        ):
        self.adj: dict[Node, list[Node]] = adj if adj is not None else {}
        self.nodes_positions: dict[Node, Vector2] = nodes_positions if nodes_positions is not None else {}
        self.node_data: dict[Node, Any] = node_data if node_data is not None else {}

        self.next_node_gen = count(len(self.adj))
    
    def __str__(self):
        return f'Network(nodes={list(self.nodes())}, edges={list(self.edges())}; node_data={self.node_data})'

    def add_edge(self, edge: Edge):
        if edge[0] == edge[1]:
            raise ValueError(f'Cannot connect a node to itself')
        if not (edge[0] in self.adj.keys() and edge[1] in self.adj.keys()):
            raise KeyError(f'Cannot connect non-existing nodes')
        if edge[1] in self.adj[edge[0]]:
            raise ValueError(f'Edge {edge} already exists')
        self.adj[edge[0]].append(edge[1])
    
    def add_node(self,
            node: Node,
            position: Vector2 = Vector2(),
            node_data: Any = None
        ):
        self.adj[node] = []
        self.nodes_positions[node] = position
        self.set_node_data(node, node_data)

    def set_node_data(self, node: Node, node_data: Any):
        self.node_data[node] = node_data
    
    def get_node_data(self, node: Node) -> Any:
        return self.node_data[node]

    def remove_node(self, node: Node):
        del self.adj[node]
        del self.nodes_positions[node]
        if node in self.node_data: del self.node_data[node]
        for from_, to_list in self.adj.items():
            if node in to_list:
                to_list.remove(node)
    
    def remove_edge(self, edge: Edge):
        self.adj[edge[0]].remove(edge[1])

    def edges(self) -> Iterable[Edge]:
        for from_, to_list in self.adj.items():
            for to_ in to_list:
                yield (from_, to_)
    
    def nodes(self) -> Iterable[Node]:
        yield from self.adj

    # algorithms

    def bfs(self, start: Node) -> Iterable[Node]:
        queue = deque([start])
        visited = {start}
        while queue:
            node = queue.popleft()
            yield node
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
    
    def dfs(self, start: Node) -> Iterable[Node]:
        stack = [start]
        visited = {start}
        while stack:
            node = stack.pop()
            yield node
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
    
    def shortest_path(self, start: Node, end: Node) -> list[Node]:
        ...

    def connected_components(self) -> list[list[Node]]:
        cc = []
        visited = set()
        for node in self.nodes():
            if node not in visited:
                component = list(self.bfs(node))
                cc.append(component)
                visited.update(component)
        return cc

    # serialization

    def dump(self, filepath: pathlib.Path):
        with filepath.open('w') as f:
            json.dump({
            'adj': self.adj,
            'nodes_positions': {node: list(pos) 
                for node, pos in self.nodes_positions.items()},
            # 'node_data': self.node_data, # TODO: serialize node_data
            }, f, indent=2)
    
    @staticmethod
    def load(filepath: pathlib.Path) -> 'Network':
        with filepath.open() as f:
            data = json.load(f)
        network = Network(
            {int(node): lst for node, lst in data['adj'].items()}, 
            {int(node): Vector2(pos) for node, pos in data['nodes_positions'].items()},
            # data['node_data'] # TODO: deserialize node_data
        )
        return network
    
    def dump_pickle(self, filepath: pathlib.Path):
        ...
    
    @staticmethod
    def load_pickle(filepath: pathlib.Path) -> 'Network':
        ...
