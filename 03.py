m = int(input())
def find_min_max(sequence):
    fmin = min(sequence)
    fmax = max(sequence)
    return fmin, fmax

for i in range(m):
    first_sequence = list(map(int, input().split()))
    second_sequence = list(map(int, input().split()))
    fmin, fmax = find_min_max(first_sequence)
    condition = (fmin + fmax) // 2
    numbers_in_range = [num for num in second_sequence if fmin < num < condition]
    print(fmin, fmax)
    for num in numbers_in_range:
        print(num)
