class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)
        q=deque()
        time = 0 

        while heap or q:
            time +=1
            if heap:
                cnt = heapq.heappop(heap)
                if cnt + 1 < 0:
                    q.append([cnt+1,time+n])
            else:
                time = q[0][1]
            if q and q[0][1] == time:
                heapq.heappush(heap,q.popleft()[0])
        return time
