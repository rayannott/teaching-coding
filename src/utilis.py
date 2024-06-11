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
