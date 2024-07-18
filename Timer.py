import time


class Timer:
    def __init__(self):
        self.start_time = time.time()
        self.elapsed_time = 0
        self.running = True

    def update(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time

    def pause(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False

    def resume(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True

    def reset(self):
        self.start_time = time.time()
        self.elapsed_time = 0
        self.running = True

    def get_time_string(self):
        minutes, seconds = divmod(int(self.elapsed_time), 60)
        return f"{minutes:02d}:{seconds:02d}"
