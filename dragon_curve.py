# https://www.acmicpc.net/problem/15685
import sys
sys.stdin = open('input.txt', 'r')

# 드래곤 커브 = 시작점 / 시작 방향 / 세대
# 0세대는 길이가 1인 선분
# 크기가 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수를 구하기
# 0 ≤ x ≤ 100, 0 ≤ y ≤ 100만 유효한 좌표
#  0세대 드래곤 커브 ㅡ
# n세대 드래곤 커브 = n-1세대 + n-1세대를 90도
# 생성 규칙 : 0세대 : →  1세대 : → ↑ 2세대 : → ↑(여기서부터 역순으로 뒤집기) ← ↑ 3세대 → ↑ ← ↑(여기서부터 역순으로 뒤집기) ← ↓ ← ↑
# 방향 90도 변환 규칙 : ↑ to ← / ← to ↓ /  ↓ to → / → to ↑ (해당위치 % 4)
# 시작 방향 고려

N = int(input())
dir_arr = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dragon_map = [[0] * 101 for _ in range(101)]


def draw_dragon_curve():
    # (c, r, d, g)
    for _ in range(N):
        c, r, d, g = list(map(int, input().split()))
        dragon_map[r][c] = 1

        curve = [d]
        for _ in range(g):
            for i in range(len(curve) - 1, -1, -1):
                # 역순으로 방향 뒤집기
                # 이전 generation에서 90도 회전
                curve.append((curve[i] + 1) % 4)

        for d in curve:
            r, c = r + dir_arr[d][0], c + dir_arr[d][1]
            dragon_map[r][c] = 1


answer = 0
def calc_square():
    global answer
    for r in range(100):
        for c in range(100):
            if dragon_map[r][c] and dragon_map[r + 1][c] and dragon_map[r][c + 1] and dragon_map[r + 1][c + 1]:
                answer += 1


draw_dragon_curve()
calc_square()
print(answer)
