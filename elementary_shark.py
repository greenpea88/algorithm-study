import sys

sys.stdin = open("input.txt", "r")
# https://www.acmicpc.net/problem/21608

# 1. 비어 있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 자리
# 2. 1.이 여러 개면 후보 중에 인접한 칸 중 비어 있는 자리가 가장 많은 자리
# 3. 2.도 여러 개면 행의 번호가 가장 작은 칸
# 4. 3.도 여러 개면 열의 번호가 가장 작은 칸

N = int(input())

shark_like = [[] for _ in range(N * N)]
seats = [[0] * N for _ in range(N)]

dir_arr = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def select_seats():
    for _ in range(N * N):
        info = list(map(int, input().split()))
        shark_num = info[0]
        shark_like[shark_num - 1] = info[1:]

        # (r, c, like, empty)
        candi = []
        for r in range(N):
            for c in range(N):
                if seats[r][c] == 0:
                    like, empty = 0, 0
                    for dr, dc in dir_arr:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N:
                            if seats[nr][nc] in shark_like[shark_num - 1]:
                                # 좋아하는 학생이 있는 경우
                                like += 1
                            elif seats[nr][nc] == 0:
                                # 자리가 빈 경우
                                empty += 1
                    candi.append((r, c, like, empty))
        pick = sorted(candi, key=lambda x: (-x[2], -x[3], x[0], x[1]))[0]
        seats[pick[0]][pick[1]] = shark_num


def calc_prefer():
    # 인접한 칸의 좋아하는 학생 수
    # 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000
    total_prefer = 0
    for r in range(N):
        for c in range(N):
            prefer = 0
            shark_num = seats[r][c]
            like = shark_like[shark_num - 1]
            for dr, dc in dir_arr:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and seats[nr][nc] in like:
                    prefer += 1
            total_prefer += 10 ** (prefer - 1) if prefer else 0
    return total_prefer


select_seats()
ans = calc_prefer()
print(ans)
