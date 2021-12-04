import functools

class Board:

    def __init__(self, numbers) -> None:
        self.numbers = list(map(lambda x: (x, False), numbers))
        self.won = False

    def getRow(self, index):
        return self.numbers[(index-1)*5:(index*5)]

    def getColumn(self, index):
        indices = [index-1, index+4, index+9, index+14, index+19]
        return [self.numbers[i] for i in indices]

    def markNumber(self, number):
        for num, entryNumber in enumerate(self.numbers):
            if(entryNumber[0] == number):
                self.numbers[num] = (number, True)

    def checkCompleteness(self):
        complete = False
        for i in range(1,6):
            complete = True if functools.reduce(lambda a, b: (0, a[1] and b[1]), self.getRow(i))[1] else complete
            complete = True if functools.reduce(lambda a, b: (0, a[1] and b[1]), self.getColumn(i))[1] else complete
        self.won = complete
        return complete

    def getUnmarkedNumbers(self):
        return list(map(lambda x: x[0], filter(lambda x: not x[1], self.numbers)))
