import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        graph = {i: [] for i in range(n)}
        for i in range(len(edges)):
            a, b = edges[i]
            prob = succProb[i]
            graph[a].append((b, prob))
            graph[b].append((a, prob))

        pq = [(-1.0, start_node)]  
        max_prob = [0] * n  
        max_prob[start_node] = 1.0

        while pq:
            prob, node = heapq.heappop(pq)
            prob = -prob 

            if node == end_node:
                return prob

            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob 
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor)) 

        return 0.0
