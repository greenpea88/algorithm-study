# # https://www.acmicpc.net/problem/15684
import sys
sys.stdin = open('input.txt', 'r')

# N개의 세로선
# 각 세로선마다 가로선을 놓을 수 있는 위치는 H개 = 점선의 갯수
# 현재 그어져 있는 가로선의 수는 M개

# 인접한 세로선 사이에는 가로선을 놓을 수 있음
# 인접한 점선에 연달아서 가로선을 놓을 수 없음
# i번 세로선의 결과가 i가 나오도록 하기 위해서 추가해야하는 가로선의 최소값
# 정답이 3보다 클 경우 or 불가능한 경우 -1 반환
# dfs

N, M, H = map(int, input().split())
# b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결
# (a, b)
ladder_map = [[0] * N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    ladder_map[a - 1][b - 1] = 1


def check_possible():
    for i in range(N):
        sc = i
        for j in range(H):
            # 가로선 오른쪽
            if ladder_map[j][sc] == 1:
                sc += 1
            # 가로선 왼쪽
            elif sc > 0 and ladder_map[j][sc-1] == 1:
                sc -= 1
        if i != sc:
            return False
    return True


def dfs(sr, sc, count):
    global answer
    if answer <= count:
        return
    if check_possible():
        answer = min(answer, count)
        return
    if count > 3:
        return

    for r in range(sr, H):
        sh = sc if sr == r else 0
        for c in range(sh, N - 1):
            if ladder_map[r][c] == 0:
                ladder_map[r][c] = 1
                dfs(r, c + 2, count + 1)
                ladder_map[r][c] = 0


answer = 4
dfs(0, 0, 0)
answer = -1 if answer > 3 else answer
print(answer)