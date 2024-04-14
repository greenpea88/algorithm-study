# https://www.codetree.ai/training-field/frequent-problems/problems/tail-catch-play/description
import sys

sys.stdin = open("input.txt", "r")

# 3명 이상이 한 팀
# 모든 사람들은 자기 앞 사람의 허리를 잡고 움직임
# 맨 앞 = 머리 사람 / 맨 끝 = 꼬리 사람
# 주어진 이동 선을 따라서만 이동함
# 1. 각 팀은 머리 사람을 따라서 한 칸 이동
# 2. 각 라운드마다 공이 정해진 선을 따라 던져짐
# 3. 공이 던져지는 경우에 해당 선에 사람이 있으면 최초에 공을 만나는 사람이 점수를 얻게 됨
# 머리 사람으로부터 k번째 사람이라면 k ** 2만큼 점수를 얻음
# 공을 획득한 팀의 경우에는 머리사람과 꼬리사람이 바뀜
# 각 팀이 획득한 거리의 총 합

N, M, K = map(int, input().split())
# 0은 빈칸, 1은 머리사람, 2는 머리사람과 꼬리사람이 아닌 나머지, 3은 꼬리사람, 4는 이동 선
teams = {}
game_map = [list(map(int, input().split())) for _ in range(N)]


dir_arr = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def initialize():
    visit = [[0] * N for _ in range(N)]
    team_num = 5
    for r in range(N):
        for c in range(N):
            if game_map[r][c] == 1:
                visit[r][c] = 1
                game_map[r][c] = team_num
                stack = [(r, c)]
                team = [(r, c)]
                while stack:
                    sr, sc = stack.pop(0)
                    for dr, dc in dir_arr:
                        nr, nc = sr + dr, sc + dc
                        if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc]:
                            # 꼬리는 제일 마지막 -> 머리에서부터 얻은 3 값을 넣으면 꼬리가 제일 마지막에 갈 수 없음
                            if game_map[nr][nc] == 2 or (
                                (r, c) != (sr, sc) and game_map[nr][nc] == 3
                            ):
                                visit[nr][nc] = 1
                                game_map[nr][nc] = team_num
                                stack.append((nr, nc))
                                team.append((nr, nc))
                teams[team_num] = team
                team_num += 1


def pp_move():
    for team in teams.values():
        # 꼬리
        tr, tc = team.pop()
        game_map[tr][tc] = 4
        # 머리
        hr, hc = team[0]
        for dr, dc in dir_arr:
            nr, nc = hr + dr, hc + dc
            if 0 <= nr < N and 0 <= nc < N and game_map[nr][nc] == 4:
                teams[game_map[hr][hc]] = [(nr, nc)] + team
                game_map[nr][nc] = game_map[hr][hc]
                break


def throw_ball(k):
    # 반시계 방향
    d = (k // N) % 4
    offset = k % N
    if d == 0:
        sr, sc = offset, 0
    elif d == 1:
        sr, sc = N - 1, offset
    elif d == 2:
        sr, sc = N - 1 - offset, N - 1
    elif d == 3:
        sr, sc = 0, N - 1 - offset

    score = 0
    for _ in range(N):
        if 0 <= sr < N and 0 <= sc < N and game_map[sr][sc] > 4:
            team_num = game_map[sr][sc]
            score = (teams[team_num].index((sr, sc)) + 1) ** 2
            teams[team_num].reverse()
            break
        sr, sc = sr + dir_arr[d][0], sc + dir_arr[d][1]
    return score


initialize()
score = 0
for k in range(K):
    pp_move()
    s = throw_ball(k)
    score += s

print(score)
