from itertools import count

import pygame
from pygame import Color, Vector2

from network import Network, Node, Edge

pygame.font.init()
FONT = pygame.font.Font(None, 36)

FRAMERATE = 60

SCREEN_SIZE_HEIGHT = 600

WHITE = Color("white")
BG_COLOR = Color("#202020")


NEXT_NODE = count(0)

ARROW_HEAD_SIZE = 12


class NetworkApp:
    NODES_RADIUS = 20

    def __init__(self, network: Network | None = None):
        self.network = network if network is not None else Network()
        self.nodes_positions: dict[Node, Vector2] = {}
        self.running = True

        self.node_mouse_down = None
    
    def add_node(self, position: Vector2):
        node = next(NEXT_NODE)
        self.network.add_node(node)
        self.nodes_positions[node] = position
    
    def add_edge(self, edge: Edge):
        try:
            self.network.add_edge(edge)
        except ValueError as e:
            print(e)
    
    def mouse_on_node(self, position: Vector2) -> Node | None:
        for node, node_position in self.nodes_positions.items():
            if (node_position - position).length_squared() <= self.NODES_RADIUS**2:
                return node
        return None
    
    def process_event(self, event: pygame.Event):
        if event.type == pygame.QUIT:
            self.running = False
            return
        mouse_pos = Vector2(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.node_mouse_down = self.mouse_on_node(mouse_pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                node_mouse_up = self.mouse_on_node(mouse_pos)
                if self.node_mouse_down is not None and node_mouse_up is not None:
                    self.add_edge((self.node_mouse_down, node_mouse_up))
                self.node_mouse_down = None
            elif event.button == 2:
                self.add_node(Vector2(mouse_pos))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                print(self.network)

    def _draw_node(self, node: Node, position: Vector2):
        pygame.draw.circle(self.surface, WHITE, position, self.NODES_RADIUS, 3)
        text = FONT.render(str(node), True, WHITE)
        text_rect = text.get_rect(center=position + Vector2(self.NODES_RADIUS * 1.5, 0))
        self.surface.blit(text, text_rect)
    
    def _draw_edge(self, from_: Vector2, to_: Vector2):
        direction = (to_ - from_).normalize()
        arrow_base = to_ - 2 * direction * self.NODES_RADIUS
        edge_start = from_ + direction * self.NODES_RADIUS
        edge_end = to_ - direction * self.NODES_RADIUS
        arrow_left = arrow_base + direction.rotate(30) * ARROW_HEAD_SIZE
        arrow_right = arrow_base + direction.rotate(-30) * ARROW_HEAD_SIZE
        pygame.draw.line(self.surface, WHITE, arrow_left, edge_end, 2)
        pygame.draw.line(self.surface, WHITE, arrow_right, edge_end, 2)
        pygame.draw.line(self.surface,
            WHITE,
            edge_start,
            edge_end,
            2
        )
    
    def draw_network(self):
        for node, position in self.nodes_positions.items():
            self._draw_node(node, position)

        for edge in self.network.edges():
            p1 = self.nodes_positions[edge[0]]
            p2 = self.nodes_positions[edge[1]]
            self._draw_edge(p1, p2)

    def run(self):
        pygame.init()
        self.surface = pygame.display.set_mode((SCREEN_SIZE_HEIGHT, SCREEN_SIZE_HEIGHT))
        background = pygame.Surface((SCREEN_SIZE_HEIGHT, SCREEN_SIZE_HEIGHT))
        background.fill(BG_COLOR)
        pygame.display.set_caption("Network App")
        clock = pygame.time.Clock()
        while self.running:
            time_delta = clock.tick(FRAMERATE) / 1000.0
            for event in pygame.event.get():
                self.process_event(event)
            self.surface.blit(background, (0, 0))
            self.draw_network()
            pygame.display.update()
        pygame.quit()
