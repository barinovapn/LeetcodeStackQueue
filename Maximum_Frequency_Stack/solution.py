from collections import deque

class FreqStack:
    def __init__(self):
        self.freqStacks = deque()
        self.maxFreq = 0
        self.freqCount = {}

    def push(self, val: int) -> None:
        freq = self.freqCount.get(val, 0) + 1
        self.freqCount[val] = freq

        if freq > self.maxFreq:
            self.freqStacks.append(deque())
            self.maxFreq = freq

        self.freqStacks[freq-1].append(val)

    def pop(self) -> int:

        val = self.freqStacks[self.maxFreq-1].pop()
        self.freqCount[val] -= 1
        if not self.freqStacks[self.maxFreq-1]:
            self.freqStacks.pop()
            self.maxFreq -= 1

        return val