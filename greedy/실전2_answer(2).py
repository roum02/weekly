# 수열로 접근하기

n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]

data.sort()
first = data[n-1]
second = data[n-2]

count = 0
count = (m//(k+1)) * k
count += m%(k+1)

result = 0
result += count * first
result += (m - count) * second

print(result)