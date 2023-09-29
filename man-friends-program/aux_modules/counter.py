class Counter(object):
    def __init__(self):
        self.counter = 0
        self.closed = True

    def add(self):
        if self.closed:
            raise IOError("Счётчик закрыт")
        self.counter += 1

    def __enter__(self):
        self.closed = False
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.closed = True

    def __str__(self):
        return str(self.counter)