def solve():
    while True:
        N = int(input())
        if N == 0:
            break

        P = int(input())
        orders = []
        for _ in range(N):
            time, pizzas = map(int, input().split())
            orders.append((time, pizzas))

        dp = [0] * (P + 1)

        for time, pizzas in orders:
            for j in range(P, pizzas - 1, -1):
                dp[j] = max(dp[j], dp[j - pizzas] + time)
        print(f"{dp[P]} min.")


solve()
