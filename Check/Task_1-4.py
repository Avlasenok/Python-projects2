class MoneyBox:
    def __init__(self, capacity):
        self.value = 0
        self.capacity = capacity

    def can_add(self, v):
        if self.value + v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.value += v
