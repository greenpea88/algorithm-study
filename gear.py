import sys

sys.stdin = open("input.txt", "r")

# 조건을 구현 -> bfs

# key : 자석의 번호 / value : 확인할 자석
check = {1: [0], 2: [0, 1], 3: [1, 2], 4: [2]}


# (톱니바퀴 번호, 방향)
# 1 : 시계 방향, -1 : 반시계 방향
def bfs(mag, num, dr):
    will_rotate = [0] * 4
    will_rotate[num - 1] = dr
    stack = [(num, dr)]
    while stack:
        n, r = stack.pop(0)
        for c in check[n]:
            if mag[c][2] != mag[c + 1][-2]:
                # 자석이 반대방향일 경우 회전
                if will_rotate[c] == 0:
                    stack.append((c + 1, -r))
                    will_rotate[c] = -r
                elif will_rotate[c + 1] == 0:
                    stack.append((c + 2, -r))
                    will_rotate[c + 1] = -r

    for idx in range(4):
        if will_rotate[idx] == 1:
            # 시계 방향 회전
            mag[idx] = [mag[idx][-1]] + mag[idx][:-1]
        elif will_rotate[idx] == -1:
            # 반시계 방향 회전
            mag[idx] = mag[idx][1:] + [mag[idx][0]]
    return mag


# N극은 0, S극은 1
mag = [list(map(int, input())) for _ in range(4)]
# 회전 횟수
K = int(input())

for _ in range(K):
    mag_num, d = map(int, input().split())
    mag = bfs(mag, mag_num, d)

score = 0
for idx in range(4):
    score += 2**idx * mag[idx][0]

print(score)
