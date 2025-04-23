class RecentCounter:

    def __init__(self):
        self.times=deque()#creating queue

    def ping(self, t: int) -> int:
        self.times.append(t) # Add the current time to the 'times' deque.

        while self.times and self.times[0] < t-3000:# Remove any timestamps that are outside the 3000ms window (t - 3000).
            self.times.popleft()#first element in queue removed
        return len(self.times)# Return the number of pings that are within the last 3000ms.
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)