# https://www.acmicpc.net/problem/15683
import sys
sys.stdin = open('input.txt', 'r')

# 0 : 빈칸 / 6: 벽
# cctv 번호에 따른 감시 방향
# cctv는 90도로 회전 가능
# cctv는 벽을 통과할 수 없음
cctv_mode = {
    1: [[0], [1], [2], [3]],
    2: [[1, 3], [0, 2]],
    3: [[0, 1], [0, 3], [1, 2], [2, 3]],
    4: [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]],
    5: [[0, 1, 2, 3]]
}
dir_arr = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M = map(int, input().split())
office = []
# (종류, r, c)
cctv_arr = []
for r in range(N):
    o = list(map(int, input().split()))
    for c in range(M):
        if o[c] != 0 and o[c] != 6:
            cctv_arr.append((o[c], r, c))
    office.append(o)
res_min = 2**31 - 1


def check(office_map, mode, r, c):
    for d in mode:
        cr, cc = r, c
        while True:
            nr, nc = cr + dir_arr[d][0], cc + dir_arr[d][1]
            if not 0 <= nr < N or not 0 <= nc < M or office_map[nr][nc] == 6:
                break
            if office_map[nr][nc] == 0:
                office_map[nr][nc] = -1
            cr, cc = nr, nc


# 사각지대의 최소 크기를 구하기 -> dfs
# 각 cctv가 어느 방향을 볼 것이지 결정
# 모든 cctv의 방향을 결정하면 종료
def dfs(count, office_map):
    global res_min
    if count == len(cctv_arr):
        count = 0
        for o in office_map:
            count += o.count(0)
        res_min = min(res_min, count)
        return

    tmp_office = [o[::] for o in office_map]
    cn, cr, cc = cctv_arr[count]
    for mode in cctv_mode[cn]:
        check(tmp_office, mode, cr, cc)
        dfs(count+1, tmp_office)
        tmp_office = [o[::] for o in office_map]


dfs(0, office)
print(res_min)


