"""
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:
Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 1:
Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

"""

class Graph:

    def __init__(self, vertices):
        self.V = vertices

        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.V:
            self.V.append(u)

        if u not in self.graph.keys():
            self.graph[u] = []

        if v not in self.graph.keys():
            self.graph[v] = []

        if v not in self.V:
            self.V.append(v)

        self.graph[u].append(v)

    def printAllPathsRec(self, u, d, visited, path, N):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)
        ans = 0

        # print if target reached
        if u == d:
            if len(path) == N:
                ans += 1

        else:
            # Not target reached, check each of its neighbours
            for i in self.graph[u]:
                if visited[i] == False:
                    ans += self.printAllPathsRec(i, d, visited, path, N)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False
        return ans

    def printAllPaths(self, s, d, N):

        if not self.V:
            return 0

        # Call the recursive helper function to print all paths
        return self.printAllPathsRec(s, d, dict([(v, False) for v in self.V]), [], N)


class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        g = Graph([])
        s, e = None, None
        for ir, r in enumerate(grid):
            for ic, c in enumerate(r):
                if c == 1:
                    s = (ir, ic)
                if c == 2:
                    e = (ir, ic)
                    continue
                if c == -1:
                    continue

                if ic > 0 and grid[ir][ic-1] != -1:
                    g.addEdge((ir, ic), (ir, ic-1))

                if ic < len(r)-1 and grid[ir][ic+1] != -1:
                    g.addEdge((ir, ic), (ir, ic+1))

                if ir > 0 and grid[ir-1][ic] != -1:
                    g.addEdge((ir, ic), (ir-1, ic))

                if ir < len(grid) - 1 and grid[ir+1][ic] != -1:
                    g.addEdge((ir, ic), (ir+1, ic))

        return g.printAllPaths(s, e, len(g.V))

grid = [[1,0,0,0],
        [0,0,0,0],
        [0,0,2,-1]]

grid = [[1,0,0,0],
        [0,0,0,0],
        [0,0,0,2]]
#grid = [[1,-1,2]]

s = Solution()
print (s.uniquePathsIII(grid))