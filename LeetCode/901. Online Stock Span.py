from collections import deque


class StockSpanner:

    def __init__(self):
        self.span = deque() # (price, span)

    def next(self, price: int) -> int:
        if len(self.span) == 0:
            self.span.append((price, 1))
        elif price < self.span[-1][0]:
            self.span.append((price, 1))
        else:
            span = 1
            while len(self.span) != 0 and price >= self.span[-1][0]:
                span += self.span.pop()[1]
            self.span.append((price, span))
        return self.span[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)