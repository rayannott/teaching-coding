import re
import json

from src.grid import Grid


class Blueprint:
    def __init__(
        self,
        grid: Grid | None = None,
        start: tuple[int, int] | None = None,
        end: tuple[int, int] | None = None,
        /,
        subgrid: list[list[int]] | None = None,
    ):
        if subgrid is not None:
            self.subgrid = subgrid
        elif grid is not None and start is not None and end is not None:
            self.subgrid = [
                row[start[1] : end[1] + 1] for row in grid[start[0] : end[0] + 1]
            ]
        else:
            raise ValueError("Invalid arguments")

    def get_rotated(self) -> "Blueprint":
        return Blueprint(subgrid=list(zip(*reversed(self.subgrid))))

    def get_flipped(self):
        return Blueprint(subgrid=list(reversed(self.subgrid)))

    def serialize(self) -> str:
        return json.dumps(self.subgrid)

    @classmethod
    def deserialize(cls, json_str: str):
        subgrid = json.loads(json_str)
        return cls(subgrid=subgrid)

    @classmethod
    def from_rle(cls, rle: str):
        SIZE_RE = re.compile(r"x = (\d+), y = (\d+)")
        NUMBER_SYMBOL_RE = re.compile(r"(\d+)?([bo$])")
        lines = rle.split("\n")
        size = SIZE_RE.match(lines[0])
        if size is None:
            raise ValueError("Invalid RLE format")
        m, n = map(int, size.groups())
        subgrid = [[0 for _ in range(m)] for _ in range(n)]
        row_idx = 0
        col_idx = 0
        other_lines_merged = "".join(
            line for line in lines[1:] if not line.startswith("#")
        )
        for num, symbol in NUMBER_SYMBOL_RE.findall(other_lines_merged):
            num = int(num) if num else 1
            if symbol == "$":
                row_idx += num
                col_idx = 0
                continue
            value = 1 if symbol == "o" else 0
            for i in range(num):
                subgrid[row_idx][col_idx] = value
                col_idx += 1

        return cls(subgrid=subgrid).get_flipped().get_rotated()

    def __hash__(self) -> int:
        return hash(str(self.subgrid))

    def __repr__(self):
        _str = ""
        for row in self.subgrid:
            _str += "".join(str(cell) for cell in row) + "\n"
        return f"Blueprint(\n{_str})"
