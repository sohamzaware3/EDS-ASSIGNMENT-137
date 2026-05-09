import pandas as pd

numbers = list(map(int, input().split()))

s = pd.Series(numbers)

grouped = s.groupby(s % 2 == 0).mean()

grouped.index = ['Even' if is_even else 'Odd' for is_even in grouped.index]

grouped = grouped.sort_index(ascending=False)

print("Mean of even and odd numbers:")
print(grouped)
