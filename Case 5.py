N = int(input())

# dp[i] — максимальная сила стаи из i голов
dp = [0] * (N + 1)
dp[0] = 1  # базовый случай: 0 голов — произведение равно 1

for i in range(1, N + 1):
    for j in range(1, 8):  # дракон может иметь от 1 до 7 голов
        if i >= j:
            dp[i] = max(dp[i], dp[i - j] * j)

print(dp[N])