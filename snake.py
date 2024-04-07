# https://www.acmicpc.net/problem/3190
import sys

sys.stdin = open("input.txt", "r")

# 뱀은 매 초마다 이동
# 게임 시작시 몸 길이 1, (0,0)에 위치, 오른쪽
# 1. 몸 길이를 늘려 다음칸에 위치시킴
# 2. 벽이나 자신의 몸에 부딪히면 끝
# 3. 이동한 칸에 사과가 있다면 사과는 없어지고 꼬리는 움직이지 않음 (= 몸 길이가 한 칸 늘음)
# 4. 이동한 칸에 사과가 없다면 몸길이가 줄어서 꼬리칸이 비워짐 (= 전체적인 몸 길이는 변하지 않음)
# simulation

N = int(input())
K = int(input())
# apple = [list(map(int, input().split())) for _ in range(K)]
snake_map = [[0] * N for _ in range(N)]
for _ in range(K):
    ar, ac = map(int, input().split())
    snake_map[ar-1][ac-1] = 1

L = int(input())
# X초, C : L(완쪽), D(오른쪽) -> 90도 회전
movement = [list(map(str, input().split())) for _ in range(L)]

dir_arr = [(-1, 0), (0, 1), (1, 0), (0, -1)]

sec = 0
snake = [(0, 0)]
hr, hc = 0, 0
d_key = 1
while True:
    sec += 1
    # head = snake[-1]
    nr, nc = hr + dir_arr[d_key][0], hc + dir_arr[d_key][1]

    if not 0 <= nr < N or not 0 <= nc < N or (nr, nc) in snake:
        break

    snake.append((nr, nc))
    hr, hc = nr, nc
    if snake_map[nr][nc]:
        snake_map[nr][nc] = 0
    else:
        snake = snake[1:]
        # snake_tail = snake[0]
    if movement and int(movement[0][0]) == sec:
        d = movement[0][1]
        movement.pop(0)
        if d == "L":
            d_key = (d_key - 1) % 4
        elif d == "D":
            d_key = (d_key + 1) % 4


print(sec)
