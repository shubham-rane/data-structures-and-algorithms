class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        heapq.heapify(distances)
        for point in points:
            dist = point[0]**2 + point[1]**2
            #heapify does the sorting based on the first element of the sublist which over here is the distance
            heapq.heappush(distances, [dist, point[0], point[1]])
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(distances)[1:])
        
        return ans