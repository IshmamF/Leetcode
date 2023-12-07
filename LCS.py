def longestCommonSubsequence(self, text1: str, text2: str) -> int:

  N, M = len(text1), len(text2) 
  # Empty row and column for empty string and having an initial row to access
  dp = [[0] * (M+1) for _ in range(N+1)]

  for i in range(1,N+1):
      for j in range(1,M+1):
          # if the two strings are equal, then add one and access the value to it's diagonal 
          # you reach the diagonal because that's the longest length of the subsequence for
          # the sub problems
          if text1[i-1] == text2[j-1]:
              dp[i][j] = 1 + dp[i-1][j-1]
          else:
          # otherwise get the mox of the row above and the column to the left
          # it signifies the number of subsequence of incrementing on one string and not the other
              dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  return dp[N][M]

# Slightly modified answer from NeetCode.io
