class FrequencyTracker(object):
    def __init__(self) -> None:
        self.num = Counter()
        self.freq= Counter()
        
    def add(self, number):
        self.freq[self.num[number]] -= 1
        self.num[number] += 1
        self.freq[self.num[number]] += 1
        
    def deleteOne(self, number):
        if self.num[number]:
            self.freq[self.num[number]] -= 1
            self.num[number] -= 1
            if self.num[number] == 0: 
                del self.num[number]
            self.freq[self.num[number]] += 1

    def hasFrequency(self, frequency):
        return self.freq[frequency] > 0

