class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Create Freq Map

        freq_of_task = {}

        for task in tasks:
            if task not in freq_of_task:
                freq_of_task[task] = 0

            freq_of_task[task] += 1

        #Create max_heap of frequencies
        # pop freq from maxheap and store in queue till time is done of reuse same task


        max_heap = [-x for x in freq_of_task.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque() # Pair of [count, idle time]

        while max_heap or queue:
            time += 1

            if max_heap:
                count =  1 + heapq.heappop(max_heap)
                if count:
                    queue.append([count, time + n])

            
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

            
        return time