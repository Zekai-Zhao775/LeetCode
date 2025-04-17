class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cursor = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.cursor + 1]
        self.history.append(url)
        self.cursor += 1

    def back(self, steps: int) -> str:
        self.cursor = max(0, self.cursor - steps)
        return self.history[self.cursor]

    def forward(self, steps: int) -> str:
        self.cursor = min(self.cursor + steps, len(self.history) - 1)
        return self.history[self.cursor]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)