# https://www.acmicpc.net/problem/17144
import sys
sys.stdin = open('input.txt', 'r')

# 1. 미세먼지 확산 -> 동시에 일어남
# 인접한 네방향으로 확산됨
# 인접한 칸에 공기 청정기가 있거나 칸이 없으면 확산이 안됨
# 확산되는 양은 A/5 (소수점 버림)
# 남은 양은 A - (A/5) * 확산된 방향의 갯수
# 2. 공기 청정기 작동
# 위쪽 공기 청정기에서 나오는 바람은 반시계 방향으로 회전함
# 아래쪽 공기 청정기에서 나오는 바람은 시계 방향으로 회전함
# 바람이 불면 바람의 방향대로 미세먼지가 한 칸씩 움직임
# 공기 청정기에서 부는 바람은 미세먼지가 없음
# 공기 청정기로 들어간 미세먼지는 정화됨 (= 없어짐)
# T초 후의 미세먼지 양 구하기
# 공기 청정기의 위치는 -1로 표현됨

R, C, T = map(int, input().split())
dust_map = []
# (r, c, amount)
# 공기청정기는 항상 1번 열에 설치
purifier = []
for r in range(R):
    tmp = list(map(int, input().split()))
    for c in range(C):
        if tmp[c] == -1:
            # 공기 청정기
            purifier.append(r)

    dust_map.append(tmp)
dir_arr = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def spread():
    global dust_map
    # 먼지의 이동은 동시에 일어남
    new_dust = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if dust_map[r][c] > 0:
                amount = dust_map[r][c]
                count = 0
                for dr, dc in dir_arr:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and dust_map[nr][nc] != -1:
                        count += 1
                        new_dust[nr][nc] += int(amount // 5)
                # print(f'{r=}{c=}{amount=}{count=}')
                new_dust[r][c] += (dust_map[r][c] - int(amount // 5) * count)
            elif dust_map[r][c] == -1:
                new_dust[r][c] = -1

    dust_map = [d[::] for d in new_dust]


def clear():
    # 공기 청정기 위쪽
    # 오, 위, 왼, 아
    r, c = purifier[0], 1
    key, wind = 0, 0
    while True:
        nr, nc = r + dir_arr[key][0], c + dir_arr[key][1]
        if nr == R or nc == C or nr == -1 or nc == -1:
            key = (key + 1) % 4
            continue
        if r == purifier[0] and c == 0:
            break
        dust_map[r][c], wind = wind, dust_map[r][c]
        r, c = nr, nc
    # 공기 청정기 아래쪽
    # 오, 아, 왼, 위
    r, c = purifier[1], 1
    key, wind = 0, 0
    while True:
        nr, nc = r + dir_arr[key][0], c + dir_arr[key][1]
        if nr == R or nc == C or nr == -1 or nc == -1:
            key = (key + 3) % 4
            continue
        if r == purifier[1] and c == 0:
            break
        dust_map[r][c], wind = wind, dust_map[r][c]
        r, c = nr, nc


for _ in range(T):
    spread()
    clear()

answer = 0
for r in range(R):
    for c in range(C):
        if dust_map[r][c] > 0:
            answer += dust_map[r][c]
print(answer)
