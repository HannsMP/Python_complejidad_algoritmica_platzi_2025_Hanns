from time import time_ns

class Chronometer:
    def start(self):
        self.time_start = time_ns()

    def stop(self):
        self.time_end = time_ns()

        return self.time_end - self.time_start