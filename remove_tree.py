# https://www.codetree.ai/training-field/frequent-problems/problems/tree-kill-all/description
import sys

sys.stdin = open("input.txt", "r")

# 제초제 : k의 범위만큼 대각선으로 퍼짐 (벽이 있는 경우 가로막혀 전파되지 않음)
# 1. 인접한 4개의 칸 중 나무가 있는 칸 수만큼 나무가 성장 (동시 발생)
# 2. 기존에 있던 나무들은 인접한 4개의 칸 중 벽 / 다른 나무 / 제초제가 없는 칸에 번식 (동시 발생)
# -> 각 칸의 나무 그루 수 // 번식이 가능한 칸의 개수
# 3. 나무가 가장 많이 박멸되는 칸에 제초제를 뿌림 (1. 많이 박멸 / 2. 행 / 3. 열) -> dfs
# -> 나무가 없는 칸에 뿌리면 제초제가 전파되지 않음
# -> 나무가 있는 칸에 뿌리면 4개의 대각선 방향으로 k칸만큼 전파됨 (벽이 있거나 나무가 없는 칸을 만나기 전까지)
# -> 제초제가 뿌려진 칸에는 c년 만큼 남아있다가 c+1년 째 사라짐
# -> 제초제가 있던 곳에 새로 뿌려지는 경우에는 다시 c년간 유지

N, M, K, C = map(int, input().split())
# tree_map = [list(map(int, input().split())) for _ in range(N)]
# 총 나무의 그루 수는 1 이상 100 이하의 수로, 빈 칸은 0, 벽은 -1
tree_map = []
tree = []
wall = []
for r in range(N):
    tmp = list(map(int, input().split()))
    for c in range(N):
        if tmp[c] > 0:
            tree.append((r, c))
        if tmp[c] == -1:
            wall.append((r, c))
    tree_map.append(tmp)

dir_arr = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def grow():
    global tree_map, tree
    # print(f'{remover=}')
    new_map = [[0] * N for _ in range(N)]
    new_tree = []
    for tr, tc in tree:
        # print(f'=========={tr=} {tc=}============')
        new_tree.append((tr, tc))
        spread = []
        g_count, s_count = 0, 0
        for key in range(0, 8, 2):
            nr, nc = tr + dir_arr[key][0], tc + dir_arr[key][1]
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in remover:
                if not tree_map[nr][nc]:
                    spread.append((nr, nc))
                    new_tree.append((nr, nc))
                    s_count += 1
                if tree_map[nr][nc] > 0:
                    g_count += 1
        new_map[tr][tc] = tree_map[tr][tc] + g_count
        for sr, sc in spread:
            new_map[sr][sc] += new_map[tr][tc] // s_count

    tree_map = [t[::] for t in new_map]
    for wr, wc in wall:
        tree_map[wr][wc] = -1
    tree = new_tree


def find_best():
    global remover
    max_remove = -(2**32)
    cur_remover = []
    for r, c in tree:
        # print(f'============={r=} {c=}==============')
        if tree_map[r][c] > 0:
            rm = tree_map[r][c]
            killed = [(r, c)]
            for key in range(1, 8, 2):
                nr, nc = r + dir_arr[key][0], c + dir_arr[key][1]
                for _ in range(K):
                    if 0 <= nr < N and 0 <= nc < N:
                        # print(f'{nr=} {nc=} {tree_map[nr][nc]=}')
                        if tree_map[nr][nc] > 0:
                            killed.append((nr, nc))
                            rm += tree_map[nr][nc]
                        elif tree_map[nr][nc] == 0:
                            killed.append((nr, nc))
                            break
                        elif tree_map[nr][nc] < 0:
                            break
                    else:
                        break
                    nr, nc = nr + dir_arr[key][0], nc + dir_arr[key][1]
            # print(f'{rm=}')
            if rm > max_remove:
                # if mr
                max_remove = rm
                # mr, mc = r, c
                cur_remover = killed[::]

    for kr, kc in cur_remover:
        remover_map[kr][kc] = C + 1
        if tree_map[kr][kc] > 0:
            tree_map[kr][kc] = 0
            tree.remove((kr, kc))
    remover = list(set(remover + cur_remover))
    return max_remove


def reduce_remover():
    global remover
    new_remover = []
    while remover:
        rr, rc = remover.pop()
        remover_map[rr][rc] -= 1
        if remover_map[rr][rc] > 0:
            new_remover.append((rr, rc))
    remover = new_remover


remove = 0
remover = []
remover_map = [[0] * N for _ in range(N)]
for _ in range(M):
    print("=====================start======================")
    print(f'{remover=}')
    for t in tree_map:
        print(t)
    print(tree)
    reduce_remover()
    grow()
    print("=====================grow======================")
    for t in tree_map:
        print(t)
    print(tree)
    remove += find_best()
    print(f'{remove=}')

print(remove)
