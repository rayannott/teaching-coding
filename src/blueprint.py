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
    
    def rotate(self):
        self.subgrid = list(zip(*reversed(self.subgrid)))
    
    def flip(self):
        self.subgrid = list(reversed(self.subgrid))

    def serialize(self) -> str:
        return json.dumps(self.subgrid)

    @classmethod
    def deserialize(cls, json_str: str):
        subgrid = json.loads(json_str)
        return cls(subgrid=subgrid)

    def __repr__(self):
        _str = ''
        for row in self.subgrid:
            _str += ''.join(str(cell) for cell in row) + '\n'
        return f"Blueprint(\n{_str})"