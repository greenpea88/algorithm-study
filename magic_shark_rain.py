# https://www.acmicpc.net/problem/21610
import sys

sys.stdin = open("input.txt", "r")

# 시작하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름 생김

# 1. 구름 이동 (d 방향으로 s칸) -> 경계를 넘어서 이동 가능
# 2. 비내림 (바구니 물 +1)
# 3. 구름 사라짐
# 4. 2.에서 물 증가한 칸에 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가
# -> 경계를 넘어가는 칸은 인접한 칸이 아님
# 5. 바구니 물이 2 이상인 칸에 구름 생성 + 물 양 -2-> 3.에서 구름이 사라진 칸에는 구름이 생기지 않음

N, M = map(int, input().split())
cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
rain_map = [list(map(int, input().split())) for _ in range(N)]

# 방향은 총 8개의 방향이 있으며, 8개의 정수로 표현 / 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dir_arr = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


def mov_cloud(d, s):
    global cloud
    moved = []
    while cloud:
        cr, cc = cloud.pop(0)
        nr, nc = (cr + dir_arr[d][0] * s) % N, (cc + dir_arr[d][1] * s) % N
        moved.append((nr, nc))

    # deep copy
    cloud = moved[::]


def rain():
    global rain_map, cloud
    for cr, cc in cloud:
        rain_map[cr][cc] += 1
    for cr, cc in cloud:
        for idx in range(1, 8, 2):
            nr, nc = cr + dir_arr[idx][0], cc + dir_arr[idx][1]
            if 0 <= nr < N and 0 <= nc < N and rain_map[nr][nc]:
                rain_map[cr][cc] += 1


def generate_cloud():
    global cloud
    new_cloud = []
    for r in range(N):
        for c in range(N):
            if rain_map[r][c] >= 2 and (r, c) not in cloud:
                new_cloud.append((r, c))
                rain_map[r][c] -= 2
    cloud = new_cloud[::]


def calc_total():
    total = 0
    for r in rain_map:
        total += sum(r)
    return total


for _ in range(M):
    D, S = map(int, input().split())
    mov_cloud(D - 1, S)
    rain()
    generate_cloud()

ans = calc_total()
print(ans)
