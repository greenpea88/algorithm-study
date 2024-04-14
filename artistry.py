# https://www.codetree.ai/training-field/frequent-problems/problems/artistry/description
import sys

sys.stdin = open("input.txt", "r")

# 각 칸의 색깔을 1이상 10이하의 숫자로 표현
# 같은 색은 하나의 그룹
# 예술 점수는 모든 그룹 쌍의 조화로움의 합으로 정의
# 조화로움 = (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수 ) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값 x 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수
# 초기 예술 점수 = 모든 그룹간의 조화로움의 합

# 1. 그림 회전
# 회전은 가운데를 기준으로 십자 선을 그어 십자선 / 그 외 부분으로 나누어 진행
# 십자선 : 통째로 반시계 방향 90도 회전
# 그 외 : 개별적으로 시계 방향 90도 회전
# 2. 예술 점수 계산
# 초기 + 1회 + 2회 + 3회의 값을 구하기

N = int(input())
mid = N // 2
paint_map = [list(map(int, input().split())) for _ in range(N)]
dir_arr = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def calc_score():
    visit = [[0] * N for _ in range(N)]
    group = {}
    for r in range(N):
        for c in range(N):
            if not visit[r][c]:
                visit[r][c] = 1
                color = paint_map[r][c]
                stack = [(r, c)]
                group[(r, c)] = [(r, c)]
                while stack:
                    cr, cc = stack.pop(0)
                    for dr, dc in dir_arr:
                        nr, nc = cr + dr, cc + dc
                        if (
                            0 <= nr < N
                            and 0 <= nc < N
                            and paint_map[nr][nc] == color
                            and not visit[nr][nc]
                        ):
                            visit[nr][nc] = 1
                            group[(r, c)].append((nr, nc))
                            stack.append((nr, nc))

    groups = list(group.keys())
    s = 0
    for a in range(len(groups) - 1):
        for b in range(a + 1, len(groups)):
            a_group = group[groups[a]]
            b_group = group[groups[b]]
            a_point = len(a_group)
            b_point = len(b_group)
            a_color = paint_map[groups[a][0]][groups[a][1]]
            b_color = paint_map[groups[b][0]][groups[b][1]]
            near = 0
            for ar, ac in a_group:
                for dr, dc in dir_arr:
                    nr, nc = ar + dr, ac + dc
                    if (nr, nc) in b_group:
                        near += 1
            # (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수 ) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값 x 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수
            s += (a_point + b_point) * a_color * b_color * near
    return s


def rotate():
    global paint_map
    new_paint = [[0] * N for _ in range(N)]
    # 십자 회전 (반시계)
    # nr, nc = N - c - 1, r
    for r in range(N):
        new_paint[mid][r] = paint_map[r][mid]
    for c in range(N):
        new_paint[N - c - 1][mid] = paint_map[mid][c]

    # 정사각형 회전 (시계)
    # nr, nc = c, N - r - 1
    for sr, sc in [(0, 0), (0, mid + 1), (mid + 1, 0), (mid + 1, mid + 1)]:
        for r in range(mid):
            for c in range(mid):
                nr, nc = sr + c, sc + mid - r - 1
                new_paint[nr][nc] = paint_map[sr + r][sc + c]

    paint_map = [p[::] for p in new_paint]


score = calc_score()
for _ in range(3):
    rotate()
    score += calc_score()
print(score)
