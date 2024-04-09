# # https://www.acmicpc.net/problem/14502
import sys
sys.stdin = open('input.txt', 'r')

# 연구소 = 빈 칸(0), 벽(1), 바이러스(2)
# 일부칸은 이미 바이러스가 있음
# 바이러스는 상하좌우 인접한 칸으로 이동 가능
# 벽은 3개를 세울 수 있음

N, M = map(int, input().split())
lab_map = [list(map(int, input().split())) for _ in range(N)]

# 얻을 수 있는 안전 영역의 최대값 구하기 -> dfs

res_max = -(2**32)
dir_arr = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def spread_virus(): # bfs
    tmp_lab = [l[::] for l in lab_map]
    stack = []
    for r in range(N):
        for c in range(M):
            if lab_map[r][c] == 2:
                stack.append((r, c))

    while stack:
        cr, cc = stack.pop(0)
        for dr, dc in dir_arr:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < M and not tmp_lab[nr][nc]:
                tmp_lab[nr][nc] = 2
                stack.append((nr, nc))

    global res_max
    count = 0
    for l in tmp_lab:
        count += l.count(0)
    res_max = max(res_max, count)


def set_wall(count):
    if count == 3:
        spread_virus()
        return

    for r in range(N):
        for c in range(M):
            if lab_map[r][c] == 0:
                lab_map[r][c] = 1
                set_wall(count + 1)
                lab_map[r][c] = 0


set_wall(0)
print(res_max)


