import sys

sys.stdin = open("input.txt", "r")

# https://www.acmicpc.net/problem/16234
# 조건에 맞는 내용 구현 -> bfs

N, L, R = map(int, input().split())
pp_map = [list(map(int, input().split())) for _ in range(N)]

# 국경선을 공유하는 두 나라의 인구차가 L 이상 R 이하라면 국경선을 하루동안 열음
# 조건에 해당하는 국경선이 모두 열리면 인구 이동 시작
# 인접한 칸만을 이용해 이동 = 연합
# 연합을 이루고 있는 각 칸의 인구수 = 연합의 인구수 / 연합을 이루고 있는 칸의 갯수 -> 소수점은 버림 = 각 칸의 인구수가 됨
# 연합 해제 후 국경선을 닫음
# 인구 이동이 발생하지 않을 때까지 반복 -> 국경이 열리지 않으면 인구 이동이 발생하지 않음 = opened의 key의 갯수가 N*N과 동일

dir_arr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = 0

opened = {}


def open_line():
    # = 하나의 block으로 합치기 = flood and fill
    visit = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visit[r][c]:
                opened[(r, c)] = {"uni": [(r, c)], "total": pp_map[r][c]}
                visit[r][c] = 1
                stack = [(r, c)]
                while stack:
                    cr, cc = stack.pop(0)
                    for dr, dc in dir_arr:
                        nr, nc = cr + dr, cc + dc
                        if (
                            0 <= nr < N
                            and 0 <= nc < N
                            and visit[nr][nc] == 0
                            and L <= abs(pp_map[cr][cc] - pp_map[nr][nc]) <= R
                        ):
                            visit[nr][nc] = 1
                            stack.append((nr, nc))
                            opened[(r, c)]["uni"].append((nr, nc))
                            opened[(r, c)]["total"] += pp_map[nr][nc]


def mov_pp():
    for k in opened.keys():
        uni = opened.get(k)["uni"]
        new_pp = opened.get(k)["total"] // len(uni)
        for cr, cc in uni:
            pp_map[cr][cc] = new_pp


def close_line():
    global opened
    opened = {}


while True:
    open_line()
    if len(opened.keys()) == N * N:
        break
    mov_pp()
    close_line()
    ans += 1

print(ans)
