#N:배열크기 M:숫자가 더해지는 횟수,K:연속 최대 횟수
N, M, K = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort(reverse=True)

fnum = int(arr[0])
snum = int(arr[1])
result = 0

#num: 가장 큰 수가 더해지는 횟수
#K+1 : 반복되는 수열 길이
num = int(M/(K+1))*K + M % (K+1)

result = num*fnum
result += (M-num)*snum
print(result)