# https://www.codetree.ai/problems/hide-and-seek/description
import sys
sys.stdin = open('input.txt', 'r')

# 술래는 처음에 정중앙에 위치
# m명의 도망자
# 좌/우 : 오른쪽 보고 시작
# 상/하 : 아래쪽 보고 시작
# h개의 나무
# 도망자와 나무는 겹쳐질 수 있음
# k번 반복

# 1. 술래와의 거리가 3이하인 도망자들은 움직임
# 바라보고 있는 방향으로 1칸 움직일 시 칸 내부일 때
# 술래가 있는 경우 움직이지 않음
# 움직이려는 칸에 나무가 있어도 움직일 수 있음
# 바라보고 있는 방향으로 1칸 움직일 시 칸 밖일 때
# 방향을 반대로 틀음 -> 1칸 이동(술래 X 경우)
# 2. 술래가 움직임
# 위 방향으로 시작해 달팽이 모양으로 움직임
# 끝에 도달하면 지나온 길의 반대로 중앙으로 돌아옴
# 해당하는 방향으로 1칸 움직임 (달팽이 모양의 방향)
# 3. 시야에 해당하는 도망자를 잡음 (술래의 시야는 3칸)
# 나무가 놓여 있는 칸이라면 도망자를 잡지 못함
# 턴 수 * 잡은 도망자의 수만큼 점수를 얻게 됨

N, M, H, K = map(int,input().split())
# 1: 좌우 / 2: 상하
runner = []
for _ in range(M):
    # (r, c, d)
    r, c, d = map(int, input().split())
    if d == 1:
        runner.append([r - 1, c - 1, d, 1])
    elif d == 2:
        runner.append([r - 1, c - 1, d, 2])
# (r, c)
tree = [list(map(int, input().split())) for _ in range(H)]
dir_arr = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def runner_move():
    global runner
    new_runner = []
    while runner:
        r, c, d, p = runner.pop()
        if abs(r - sr) + abs(c - sc) <= 3:
            nr, nc = r + dir_arr[p][0], c + dir_arr[p][1]
            if 0 <= nr < N and 0 <= nc < N:
                if (nr, nc) != (sr, sc):
                    r, c = nr, nc
            else:
                p = (p + 2) % 4
                nr, nc = r + dir_arr[p][0], c + dir_arr[p][1]
                if (nr, nc) != (sr, sc):
                    r, c = nr, nc
        new_runner.append((r, c, d, p))
    runner = new_runner


def seeker_move():
    global sr, sc, sd, max_step, step, in_and_out, s_flag
    nr, nc = sr + dir_arr[sd][0], sc + dir_arr[sd][1]
    step += 1
    if nr == 0 and nc == 0:
        max_step, step, s_flag = N, 1, 1
        in_and_out = -1
        sd = 2
    elif nr == N // 2 and nc == N // 2:
        max_step, step, s_flag = 1, 0, 0
        in_and_out = 1
        sd = 0
    else:
        if step == max_step:
            # 방향 전환
            step = 0
            sd = (sd + in_and_out) % 4
            if s_flag:
                max_step += in_and_out
                s_flag = 0
            else:
                s_flag = 1

    sr, sc = nr, nc


def catch_runner():
    global runner
    count = 0
    site = [(sr, sc), (sr + dir_arr[sd][0], sc + dir_arr[sd][1]), (sr + dir_arr[sd][0] * 2, sc + dir_arr[sd][1] * 2)]
    new_runner = []
    while runner:
        rr, rc, d, p = runner.pop()
        if (rr, rc) in site and [rr + 1, rc + 1] not in tree:
            count += 1
        else:
            new_runner.append((rr, rc, d, p))
    runner = new_runner
    return count


score = 0
sr, sc, sd = N // 2, N // 2, 0
max_step, step, s_flag = 1, 0, 0
in_and_out = 1
for k in range(1, K+1):
    runner_move()
    seeker_move()
    catch = catch_runner()
    score += k * catch
    if not runner:
        break
print(score)
