import random
import pathlib
import json


def generate_transactions(dest: pathlib.Path, seed: int = 42, N: int = 100_000):
    if dest.exists():
        print(f"File {dest} already exists. Skipping.")
        return
    with dest.open("w") as f:
        ...
