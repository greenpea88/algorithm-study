# https://www.acmicpc.net/problem/14499
import sys
sys.stdin = open('input.txt', 'r')

# 주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태
# 처음에는 주사위의 모든 면이 0
# 지도의 각 칸에는 정수가 쓰여져 있음
# 주사위를 굴렸을 때 이동한 칸에 쓰여있는 수가 0이면 주사위 바닥면에 있는 숫자가 칸에 복사됨
# 0이 아닌 경우에는 칸에 있는 값이 주사위 바닥면으로 복사됨 -> 칸에 있는 수는 0
# 주사위를 바깥으로 이동시키려고 하는 경우 해당 명령 무시 + 출력 안함

N, M, x, y, K = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(N)]
# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
orders = list(map(int, input().split()))

dice = [0] * 6
dir_arr = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def turn(d):
    if d == 1: # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif d == 2: # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif d == 3: # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    elif d == 4: # 남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]


for o in orders:
    nr, nc = x + dir_arr[o-1][0], y + dir_arr[o-1][1]
    if not 0 <= nr < N or not 0 <= nc < M:
        continue

    turn(o)
    if map_info[nr][nc] == 0:
        map_info[nr][nc] = dice[5]
    else:
        dice[5] = map_info[nr][nc]
        map_info[nr][nc] = 0
    x, y = nr, nc
    # 주사위 맨 윗면에 있는 수를 출력
    print(dice[0])

