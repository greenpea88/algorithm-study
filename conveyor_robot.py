import sys

sys.stdin = open("input.txt", "r")

# https://www.acmicpc.net/problem/20055

# 길이 N인 컨베이어 벨트 -> 길이 2*N인 벨트가 컨베이어 벨트를 위아래로 감싸고 있음
# 벨트는 1~2N까지 번호가 매겨져 있음
# 1번 : 올리는 위치 / N번 : 내리는 위치
# 1. 벨트와 로봇이 같이 한 칸 이동
# 2. 먼저 올라간 로봇부터 벨트 회전 방향으로 이동 가능하면 이동 / 불가능 시 이동하지 않음
# 이동 가능? 이동하려는 칸에 로봇이 없으며 내구도가 1이상
# 3. 올리는 위치(=1번) 에 내구도가 0 이상이면 로봇을 올림
# 4. 내구도가 0인 칸이 K개 이상이면 과정 종료
# 내구도 : 로봇이 올라가거나 로봇이 해당 칸으로 이동하면 -1

# 조건 구현 -> bfs

N, K = map(int, input().split())
# len = 2N
conv = list(map(int, input().split()))

robot = [0] * N


def mov_belt():
    global conv, robot
    conv = [conv[-1]] + conv[:-1]
    robot = [robot[-1]] + robot[:-1]
    # N번째 칸의 로봇은 내려야 함
    robot[N - 1] = 0


def mov_robot():
    for idx in range(N - 2, -1, -1):
        if robot[idx] == 1 and robot[idx + 1] == 0 and conv[idx + 1] > 0:
            robot[idx], robot[idx + 1] = 0, 1
            conv[idx + 1] -= 1
    robot[N - 1] = 0

    if conv[0] > 0:
        robot[0] = 1
        conv[0] -= 1


ans = 0
while True:
    mov_belt()
    mov_robot()
    ans += 1
    if conv.count(0) >= K:
        break

print(ans)
