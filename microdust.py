# https://www.acmicpc.net/problem/17144
import sys
sys.stdin = open('input.txt', 'r')

# 1. 미세먼지 확산 -> 동시에 일어남
# 인접한 네방향으로 확산됨
# 인접한 칸에 공기 청정기가 있거나 칸이 없으면 확산이 안됨
# 확산되는 양은 A/5 (소수점 버림)
# 남은 양은 A - (A/5) * 확산된 방향의 갯수
# 2. 공기 청정기 작동
# 공기청정기는 항상 1번 열에 설치
# 위쪽 공기 청정기에서 나오는 바람은 반시계 방향으로 회전함
# 아래쪽 공기 청정기에서 나오는 바람은 시계 방향으로 회전함
# 바람이 불면 바람의 방향대로 미세먼지가 한 칸씩 움직임
# 공기 청정기에서 부는 바람은 미세먼지가 없음
# 공기 청정기로 들어간 미세먼지는 정화됨 (= 없어짐)
# T초 후의 미세먼지 양 구하기
# 공기 청정기의 위치는 -1로 표현됨

R, C, T = map(int, input().split())
# dust_map = [list(map(int, input().split())) for _ in range(R)]
dust_map = []
# dust = []
purifier = []
for r in range(R):
    tmp = list(map(int, input().split()))
    for c in range(C):
        if tmp[c] == -1:
            purifier.append(r)

    dust_map.append(tmp)
# print(dust_map)
dir_arr = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def spread():
    global dust_map
    tmp_map = [dust[::] for dust in dust_map]
    for r in range(R):
        for c in range(C):
            if dust_map[r][c] > 0:
                amount = dust_map[r][c]
                count = 0
                for dr, dc in dir_arr:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and dust_map[nr][nc] != -1:
                        tmp_map[nr][nc] += amount // 5
                        count += 1
                tmp_map[r][c] = amount - (amount // 5) * count
    dust_map = [t[::] for t in tmp_map]


def purify():
    tmp_map = [dust[::] for dust in dust_map]
    # 위쪽 시계 방향
    # for key in [0, 1, 2, 3]:
    r, c = purifier[0], 0
    wind = 0
    key = 0
    while True:
        nr, nc = r + dir_arr[key][0], c + dir_arr[key][1]
        if nr == R or nc == C or nr == -1 or nc == -1:
            # 벽에 닿으면 방향 변경
            key = (key + 1) % 4
            continue
        if nr == purifier[0] and nc == 0:
            break
        dust_map[r][c], wind = wind, dust_map[r][c]
        r, c = nr, nc

    # 아래쪽 시계 방향
    # for key in [0, 3, 2, 1]:
    r, c = purifier[1], 0
    wind = 0
    key = 0
    while True:
        nr, nc = r + dir_arr[key][0], c + dir_arr[key][1]
        if nr == R or nc == C or nr == -1 or nc == -1:
            # 벽에 닿으면 방향 변경
            key = (key - 1) % 4
            continue
        if nr == purifier[0] and nc == 0:
            break
        dust_map[r][c], wind = wind, dust_map[r][c]
        r, c = nr, nc


for _ in range(T):
    spread()
    purify()


answer = 0
for r in range(R):
    for c in range(C):
        if dust_map[r][c] > 0:
            answer += 1
print(answer)
