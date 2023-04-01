"""
Edit Distance
Time complexity: O(mn)
ex 1) edit_distance("name", "m") => 3
"""

def edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0 for j in range(n+1)] for i in range(m+1)]
    
    for i in range(m+1):
        dp[i][0] = i
    
    for j in range(n+1):
        dp[0][j] = j
        
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    return dp[m][n]