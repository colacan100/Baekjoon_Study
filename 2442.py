import sys
N = int(sys.stdin.readline())
star = '*'
blank = ' '
count = 1
for i in range(N):
    print(blank*(N-i-1)+ star*count)
    count += 2