class UndergroundSystem:

    def __init__(self):
        self.checkHistory = [] # [id, [startStation, t], [endStation, t]]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkHistory.append([id, [stationName, t], None])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        for history in self.checkHistory:
            if id == history[0] and history[2] == None:
                history[2] = [stationName, t]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time_total = 0
        count = 0

        for history in self.checkHistory:
            if history[1][0] == startStation and history[2] != None:
                if history[2][0] == endStation:
                    time_total += history[2][1] - history[1][1]
                    count += 1

        return time_total / count




# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)