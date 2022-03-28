from collections import Counter

error_codes = []

with open('errors.txt') as f:
    for line in f:
        error_code = line.split(' ')[1]
        error_codes.append(error_code)

d = Counter(error_codes)
results = sorted(d, key=d.get, reverse=True)

print("The top three error codes found are:")
for code in results[:3]:
    print(code)

print(results)

