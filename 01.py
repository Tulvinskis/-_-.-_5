words = input().split('$')
count = sum(1 for word in words if len(set('aeiou') & set(word.lower())) == 1)
print(count)
