def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


class FibCalculator:
    def __init__(self):
        self.cache = {0: 0, 1: 1}

    def calculate(self, n):
        if n in self.cache:
            return self.cache[n]
        else:
            self.cache[n] = self.calculate(n - 1) + self.calculate(n - 2)
            return self.calculate(n)

import sys
sys.setrecursionlimit(15000)
if __name__ == '__main__':
    print(FibCalculator().calculate(5000))
