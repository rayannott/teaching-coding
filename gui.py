from itertools import count
import pathlib
import datetime

import pygame
from pygame import Color, Vector2

from network import Network, Node, Edge

pygame.font.init()
FONT = pygame.font.Font(None, 36)

FRAMERATE = 60

SCREEN_SIZE = (1000, 600)

WHITE = Color("white")
BG_COLOR = Color("#202020")

ARROW_HEAD_SIZE = 12


SAVES_DIR = pathlib.Path("saves")


import random
def generate_n_random_colors(n: int) -> list[Color]:
    return [
        Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
        for _ in range(n)
    ]


COLORS = generate_n_random_colors(15)


ALL_NETWORK_PATHS = list(SAVES_DIR.glob('*.json'))
ptr = count(-1)


class NetworkGui:
    NODES_RADIUS = 20

    def _reload(self, network_path: pathlib.Path | None = None):
        self.network_path = network_path
        self.network = Network.load(network_path) if network_path is not None else Network()
        self.running = True

        self.node_mouse_down = None
    
    def __init__(self, network_path: pathlib.Path | None = None):
        self._reload(network_path)
    
    def get_next_network_path(self) -> pathlib.Path | None:
        return ALL_NETWORK_PATHS[next(ptr) % len(ALL_NETWORK_PATHS)]
    
    def process_nodes_event(self, n1: Node, n2: Node):
        if n1 == n2:
            self.remove_node(n1)
        elif (n1, n2) in self.network.edges():
            self.network.remove_edge((n1, n2))
        else:
            self.network.add_edge((n1, n2))
    
    def remove_node(self, node: Node):
        self.network.remove_node(node)

    def add_node(self, position: Vector2):
        node = next(self.network.next_node_gen)
        self.network.add_node(node)
        self.network.nodes_positions[node] = position
    
    def mouse_on_node(self, position: Vector2) -> Node | None:
        for node, node_position in self.network.nodes_positions.items():
            if (node_position - position).length_squared() <= self.NODES_RADIUS**2:
                return node
        return None
    
    def process_event(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False
            return
        
        is_shift_mode = pygame.key.get_mods() & pygame.KMOD_SHIFT
        
        # mouse events
        mouse_pos = Vector2(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button in {4, 5}:
                if event.button == 4:
                    self.NODES_RADIUS += 1
                else:
                    self.NODES_RADIUS = max(1, self.NODES_RADIUS - 1)
            self.node_mouse_down = self.mouse_on_node(mouse_pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                node_mouse_up = self.mouse_on_node(mouse_pos)
                if self.node_mouse_down is not None and node_mouse_up is not None and not is_shift_mode:
                    self.process_nodes_event(self.node_mouse_down, node_mouse_up)
                elif self.node_mouse_down is None and node_mouse_up is None:
                    self.add_node(Vector2(mouse_pos))
                self.node_mouse_down = None
        elif event.type == pygame.MOUSEMOTION:
            if is_shift_mode and self.node_mouse_down is not None:
                self.network.nodes_positions[self.node_mouse_down] = mouse_pos
        
        # keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                print(self.network)
            elif event.key == pygame.K_b:
                print(list(self.network.bfs(0)))
            elif event.key == pygame.K_d:
                print(list(self.network.dfs(0)))
            elif event.key == pygame.K_c:
                print(self.network.connected_components())
            elif event.key == pygame.K_s:
                self.network.dump(
                    SAVES_DIR / f"network{datetime.datetime.now().timestamp():.0f}.json"
                    if self.network_path is None
                    else self.network_path
                )
                global ALL_NETWORK_PATHS
                ALL_NETWORK_PATHS = list(SAVES_DIR.glob('*.json'))
            elif event.key == pygame.K_n:
                self._reload(self.get_next_network_path())
            elif event.key == pygame.K_SPACE:
                self._reload()

    def _draw_node(self, 
            node: Node,
            position: Vector2,
            color: Color = WHITE,
            thickness: int = 3
        ):
        pygame.draw.circle(self.surface, color, position, self.NODES_RADIUS, thickness)
        text = FONT.render(str(node), True, WHITE)
        text_rect = text.get_rect(center=position + Vector2(self.NODES_RADIUS * 1.5, 0))
        self.surface.blit(text, text_rect)
    
    def _draw_edge(self, 
            from_: Vector2,
            to_: Vector2,
            color: Color = WHITE,
            thickness: int = 2
        ):
        direction = (to_ - from_).normalize()
        arrow_base = to_ - 2 * direction * self.NODES_RADIUS
        edge_start = from_ + direction * self.NODES_RADIUS
        edge_end = to_ - direction * self.NODES_RADIUS
        arrow_left = arrow_base + direction.rotate(30) * ARROW_HEAD_SIZE
        arrow_right = arrow_base + direction.rotate(-30) * ARROW_HEAD_SIZE
        pygame.draw.line(self.surface, color, arrow_left, edge_end, thickness)
        pygame.draw.line(self.surface, color, arrow_right, edge_end, thickness)
        pygame.draw.line(self.surface,
            color,
            edge_start,
            edge_end,
            thickness
        )
    
    def draw_network(self):
        # for node, position in self.nodes_positions.items():
        #     self._draw_node(node, position)
        for i, cc in enumerate(self.network.connected_components()):
            color = COLORS[i]
            for node in cc:
                self._draw_node(node, self.network.nodes_positions[node], color)

        for edge in self.network.edges():
            p1 = self.network.nodes_positions[edge[0]]
            p2 = self.network.nodes_positions[edge[1]]
            self._draw_edge(p1, p2)

    def run(self):
        pygame.init()
        self.surface = pygame.display.set_mode(SCREEN_SIZE)
        background = pygame.Surface(SCREEN_SIZE)
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
