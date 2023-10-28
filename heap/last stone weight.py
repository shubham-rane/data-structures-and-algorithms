class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #make all numbers negative
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        heapq.heapify(stones)
        while len(stones)>1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)  
            diff = -1 * (x - y)
            if x!=y:
                heapq.heappush(stones, diff)
        if len(stones)==0:
            return 0
        return -1*stones[0]