N, M, K = map(int, input().split()) #N:배열크기 M:숫자가 더해지는 횟수,K:연속 최대 횟수
arr = list(map(int,input().split()))
arr.sort(reverse=True)
fnum = int(arr[0])
snum = int(arr[1])
result = 0
cnt = 0

for i in range(M):
    if cnt == K:
        result += snum
        cnt = 0

    else:
        result += fnum
        cnt += 1
print(result)