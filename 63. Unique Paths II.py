class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]

        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        # Initiate first row
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                dp[0][j] == 0
            else: dp[0][j] = dp[0][j - 1]

        # Initiate first col
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] == 0
            else: dp[i][0] = dp[i - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1]


sol = Solution()
test1 = [[0, 0], [1, 1], [0, 0]]
print sol.uniquePathsWithObstacles(test1)
