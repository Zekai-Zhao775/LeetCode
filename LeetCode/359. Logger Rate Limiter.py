from collections import defaultdict


class Logger:

    def __init__(self):
        # record the timestamp of each message when the last time they are printed
        self.messages = defaultdict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messages:
            self.messages[message] = timestamp
            return True
        elif self.messages[message] + 10 > timestamp:
            return False
        else:
            self.messages[message] = timestamp
            return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)