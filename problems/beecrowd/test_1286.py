
import unittest
from unittest.mock import patch


def solve_test (input_lines_iter, output_collector):
  input_gen = (line for line in input_lines_iter)

  def mock_input (): 
    return next(input_gen)

  original_input = __builtins__.input
  original_print = __builtins__.print

  __builtins__.input = mock_input
  __builtins__.print = lambda *args, **kwargs: output_collector.append(" ".join(map(str, args)))

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

  __builtins__.input = original_input
  __builtins__.print = original_print

class TestBEE1286 (unittest.TestCase):
  def test_sample_cases (self):
    input_data = [
      "6",
      "10",
      "15 5",
      "23 4",
      "21 2",
      "16 4",
      "19 5",
      "18 2",
      "7",
      "8",
      "10 4",
      "12 4",
      "20 3",
      "22 3",
      "21 2",
      "15 5",
      "38 2",
      "0"
    ]
    expected_output = [
      "62 min.",
      "81 min."
    ]

    output_collector = []
    solve_test(input_data, output_collector)

    self.assertEqual(output_collector, expected_output)

if __name__ == '__main__':
  unittest.main()
