from PIL import Image
import numpy as np


class Timer:
    def __init__(self, max_time: float):
        self.max_time = max_time
        self.current_time = 0.0

    def tick(self, time_delta: float):
        self.current_time += time_delta
        if self.current_time >= self.max_time:
            self.current_time = 0.0
            return True
        return False

    def get_percent_full(self) -> float:
        return self.current_time / self.max_time


def hex_to_rgb(hex_color: str) -> np.ndarray:
    hex_color = hex_color.lstrip("#")
    return np.array([int(hex_color[i : i + 2], 16) for i in (0, 2, 4)])


def mute_color(hex_color: str) -> str:
    rgb = hex_to_rgb(hex_color)
    rgb = 0.5 * rgb
    return "#" + "".join(f"{int(x):02x}" for x in rgb)


def make_gif(grids: list[list[list[int]]], color_map: dict[int, str]):
    #! doesn't work
    grids_np = np.array(grids)
    frames = [Image.fromarray(grid) for grid in grids_np]
    frame_one = frames[0]
    frame_one.save(
        "my_awesome.gif",
        format="GIF",
        append_images=frames,
        save_all=True,
        duration=100,
        loop=1,
    )
