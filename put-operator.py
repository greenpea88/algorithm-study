import sys

sys.stdin = open("input.txt", "r")

# 모든 경우의 수를 만들어보는 문제 -> dfs
# 우선 순위를 무시하고 앞에서부터 계산
# 식의 결과가 최대 / 최소인 것읠 값 반환

# 수의 갯수
N = int(input())
# 주어진 수의 순서는 바꿀 수 없음
numbers = list(map(int, input().split()))
# 연산자 : +, -, *, /
# N-1개의 연산자
operators = list(map(int, input().split()))

res_min = 2**32 - 1
res_max = -(2**32)


def exe_operator(num1, num2, op_idx):
    if op_idx == 0:
        return num1 + num2
    elif op_idx == 1:
        return num1 - num2
    elif op_idx == 2:
        return num1 * num2
    elif op_idx == 3:
        # 나눗셈은 정수 나눗셈으로 몫만 취함
        # 음수 나눗셈 -> 양수로 변환한 뒤 몫을 음수로 바꿈
        return num1 // num2 if num1 > 0 else -(-num1 // num2)


def dfs(res, count):
    global res_max, res_min
    if count == N - 1:
        res_max = max(res, res_max)
        res_min = min(res, res_min)
        return

    for idx in range(4):
        if operators[idx]:
            operators[idx] -= 1
            dfs(int(exe_operator(res, numbers[count + 1], idx)), count + 1)
            operators[idx] += 1


dfs(numbers[0], 0)
print(res_max)
print(res_min)
