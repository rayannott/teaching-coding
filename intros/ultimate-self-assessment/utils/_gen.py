from math import ceil
import random
import pathlib
import json
import time
from typing import TypedDict
import csv


def clip(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


class Transaction(TypedDict):
    timestamp: int
    sender: str
    receiver: str
    amount: float


with pathlib.Path("data/bank_data.csv").open() as f:
    reader = csv.DictReader(f)
    IBANS = [row["iban"] for row in reader]


def generate_transactions(dest: pathlib.Path, seed: int = 42, num_files: int = 50):
    if dest.exists():
        print(f"Folder {dest} already exists. Skipping.")
        return

    dest.mkdir(parents=True)

    TRANSACTIONS_PER_FILE = 200_000
    FILE_NAMES = [f"transactions_{i}.jsonl" for i in range(num_files)]

    random.seed(seed)

    TIME_INTERVAL = (1735689600, 1872375000)
    IBAN_WEIGHTS = [random.uniform(0.6, 1) for _ in IBANS]

    def _gen_one() -> Transaction:
        s, r = "", ""
        while s == r:
            s, r = random.choices(IBANS, k=2, weights=IBAN_WEIGHTS)
        return {
            "timestamp": random.randint(*TIME_INTERVAL),
            "sender": s,
            "receiver": r,
            "amount": round(clip(random.expovariate(1 / 50), 0, 1000), 2),
        }

    t0 = time.perf_counter()

    for i, f in enumerate(pathlib.Path(dest, name).open("w") for name in FILE_NAMES):
        for _ in range(TRANSACTIONS_PER_FILE):
            print(json.dumps(_gen_one()), file=f)
        f.close()
        print(f"Generated: {i + 1}/{num_files} ", end="\r")

    t1 = time.perf_counter()

    print(f"Done in {t1 - t0:.2f} seconds.")
    print(
        f"Folder size: {sum(f.stat().st_size for f in dest.glob('*.jsonl')) / 1e6:.2f} MB."
    )
