import sys

sys.stdin = open("input.txt", "r")

# 청소하는 영역의 갯수 구하기 -> 조건에 맞게 구현 = BFS
# N*M 크기의 직사각형
# 칸 -> 벽 or 빈 칸

# 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우, 반시계 방향으로 90도 회전한다.
# 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
# 1번으로 돌아간다.

N, M = map(int, input().split())
# 로봇 청소기 위치, 방향
sr, sc, d = map(int, input().split())
# 0 = 빈칸, 1 = 벽
room_map = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
dir_arr = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # (r,c)


def bfs():
    global d
    stack = [(sr, sc)]
    visit[sr][sc] = 1
    ans = 1
    while stack:
        cur_r, cur_c = stack.pop(0)
        # 주변 4칸 중 빈칸이 있는 경우
        # 반시계 방향으로 탐색
        flag = 0
        for _ in range(4):
            d = (d + 3) % 4
            nr, nc = cur_r + dir_arr[d][0], cur_c + dir_arr[d][1]
            if 0 <= nr < N and 0 <= nc < M and not room_map[nr][nc]:
                if not visit[nr][nc]:
                    visit[nr][nc] = 1
                    stack.append((nr, nc))
                    ans += 1
                    flag = 1
                    break
        # 청소할 곳이 없다면 후진
        if flag == 0:
            nr, nc = cur_r - dir_arr[d][0], cur_c - dir_arr[d][1]
            if 0 <= nr < N and 0 <= nc < M and room_map[nr][nc] != 1:
                stack.append((nr, nc))
            else:
                break
    return ans


res = bfs()
print(res)
