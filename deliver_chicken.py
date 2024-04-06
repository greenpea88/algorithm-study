import sys

sys.stdin = open("input.txt", "r")

# N*N 사이즈의 지도
# 0 : 빈칸 / 1 : 집 / 2 : 치킨집
# 최대 M개의 치킨집만 남길 때 도시의 치킨 거리가 가장 작게되는 값
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합

# 모든 값을 확인 -> dfs

N, M = map(int, input().split())
# city_map = [list(map(int, input().split())) for _ in range(N)]
house, chicken = [], []

for r in range(N):
    city = list(map(int, input().split()))
    for c in range(N):
        if city[c] == 1:
            house.append((r, c))
        elif city[c] == 2:
            chicken.append((r, c))

check = [0] * len(chicken)

# 치킨 거리의 최솟값을 구하기
# 치킨 거리 = 집과 가장 가까운 치킨집 사이의 거리
min_dist = 2**31 - 1


def dfs(idx, num):
    global min_dist
    if M == num:
        dist = 0
        for hr, hc in house:
            min_chicken = 2**31 - 1
            for i in range(len(check)):
                if check[i]:
                    ch_dist = abs(chicken[i][0] - hr) + abs(chicken[i][1] - hc)
                    min_chicken = min(ch_dist, min_chicken)
            dist += min_chicken
        min_dist = min(min_dist, dist)
        return

    for i in range(idx, len(chicken)):
        if not check[i]:
            check[i] = 1
            dfs(i + 1, num + 1)
            check[i] = 0


dfs(0, 0)
print(min_dist)
