# 1차원적으로 생각하는 습관을 없애자
# 규칙성을 못찾아서 알고리즘 참고함
import sys
dp = [[0 for _ in range(3)] for _ in range(100001)]
# N이 1일때 2일때 3일때
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]
for i in range(4, 100001):
    dp[i][0]=dp[i-1][1]+dp[i-1][2]% 1000000009 # 나눠주지 않으면 메모리초과
    dp[i][1]=dp[i-2][0]+dp[i-2][2]% 1000000009
    dp[i][2]=dp[i-3][0]+dp[i-3][1]% 1000000009
T = int(sys.stdin.readline())
for j in range(T):
    n = int(sys.stdin.readline())
    print(sum(dp[n]) % 1000000009)