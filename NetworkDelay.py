import collections
import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        distances = {node: float('inf') for node in range(1, n + 1)}
        distances[k] = 0
        priority_queue = [(0, k)] 

        while priority_queue:
            current_time, current_node = heapq.heappop(priority_queue)

            if current_time > distances[current_node]:
                continue

            for neighbor, travel_time in graph[current_node]:
                new_time = current_time + travel_time

                if new_time < distances[neighbor]:
                    distances[neighbor] = new_time
                    heapq.heappush(priority_queue, (new_time, neighbor))

        max_time = 0
        for node in range(1, n + 1):
            max_time = max(max_time, distances[node])

        if max_time == float('inf'):
            return -1
        else:
            return max_time