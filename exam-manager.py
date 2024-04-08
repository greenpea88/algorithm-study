# https://www.acmicpc.net/problem/13458
import sys

sys.stdin = open('input.txt', 'r')

# 총 N개의 시험장
# i번 시험장에 있는 응시자의 수는 Ai명
# 총감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 B명이고, 부감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 C명
# 총감독관은 오직 1명만 있어야 하고, 부감독관은 여러 명

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

# 응시생을 감독하기 위한 감독관의 최소수
answer = 0
for i in range(N):
    A[i] -= B
    answer += 1
    if A[i] > 0 :
        # 총 감득으로 감시를 하지 못한다면
        pp, left = divmod(A[i], C)
        answer += pp
        if left:
            answer += 1
print(answer)
