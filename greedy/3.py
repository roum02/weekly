# 각 자리가 0~9로만 이루어진 문자열 S, 왼쪽부터 하나씩 
# 모든 숫자를 확인하며 숫자 사이에 x또는 +연산자로
# 만들어질 수 있는 가장 큰 수 구하기

s = input("s를 입력하세요:")
result = 0
max = 0
for i in range(0, len(s)):
  if max * int(s[i]) > max + int(s[i]):
     max = max * int(s[i])
  else:
    max = max + int(s[i])
  result = max
print(result)