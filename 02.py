K = int(input())
sequence = list(map(int, input().split()))

unique_numbers_set = set()

for num in sequence:
    unique_numbers_set.add(num)

print(*unique_numbers_set)
