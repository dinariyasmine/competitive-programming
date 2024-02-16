class RandomizedSet:

    def __init__(self):
        self.randomizedSet = set()

    def insert(self, val: int) -> bool:
        if val in self.randomizedSet:
            return False
        else:
            self.randomizedSet.add(val)
            return True
        
    def remove(self, val: int) -> bool:
        if val in self.randomizedSet:
            self.randomizedSet.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.randomizedSet))
