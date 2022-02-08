import sys
dp = [[0 for _ in range(10)] for _ in range(101)]
# 각 자리수에서 맨 뒤에 올수 있는 숫자의 개수(0~9)
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, 101):
    dp[i][0]=(dp[i-1][1])%1000000000
    dp[i][1]=(dp[i-1][0]+dp[i-1][2])% 1000000000
    dp[i][2]=(dp[i-1][1]+dp[i-1][3])% 1000000000
    dp[i][3]=(dp[i-1][2]+dp[i-1][4])% 1000000000
    dp[i][4]=(dp[i-1][3]+dp[i-1][5])% 1000000000
    dp[i][5]=(dp[i-1][4]+dp[i-1][6])% 1000000000
    dp[i][6]=(dp[i-1][5]+dp[i-1][7])% 1000000000
    dp[i][7]=(dp[i-1][6]+dp[i-1][8])% 1000000000
    dp[i][8]=(dp[i-1][7]+dp[i-1][9])% 1000000000
    dp[i][9]=(dp[i-1][8])% 1000000000
N = int(sys.stdin.readline())
print(sum(dp[N]) % 1000000000)