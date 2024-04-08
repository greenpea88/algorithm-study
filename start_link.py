# https://www.acmicpc.net/problem/14889
import sys

sys.stdin = open('.input.txt', 'r')

# 첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)
# 둘째 줄부터 N개의 줄에 S / 각 줄은 N개의 수
# i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수

N = int(input())
specs = [list(map(int, input().split())) for _ in range(N)]

# backtracking -> 가능한 모든 경우를 확인
# dfs

# start / link 팀의 능력치를 최소로 하고자 함
# i와 j 사람이 같은 팀일 경우 능력치의 합은 Sij + Sji
# 팀원의 수는 N / 2
visit = [0] * N # start에 존재 여부를 확인
answer = 2**31 - 1


def calc():
    start, link = 0, 0
    for i in range(N):
        for j in range(N):
            if visit[i] and visit[j]:
                # start에 속하는 경우
                start += specs[i][j]
            elif not visit[i] and not visit[j]:
                # start에 속하지 않으므로 link에 속하는 경우
                link += specs[i][j]

    global answer
    answer = min(answer, abs(start - link))
    return


def select(lv,idx):
    if lv == N // 2:
        calc()
        return

    for i in range(idx, N):
        if not visit[i]:
            visit[i] = 1
            select(lv + 1, i + 1)
            visit[i] = 0


select(0, 0)
print(answer)
