# https://www.acmicpc.net/problem/14501
import sys

sys.stdin = open('.input.txt', 'r')

# 첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.

# 둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)
# dynamic programing
# -> 작은 문제들이 반복되어서 나타남 = 이전에 사용한 값을 저장해놓고 재사용함
N = int(input())
# T : 걸리는 시간 / P : 받을 수 있는 금액
interviews = [list(map(int, input().split())) for _ in range(N)]

# 얻을 수 있는 최대 수익
dp = [0] * (N + 1)
for i in range(N) :
    for j in range(i + interviews[i][0], N + 1):
        dp[j] = max(dp[j], dp[i] + interviews[i][1])

print(dp[N])


