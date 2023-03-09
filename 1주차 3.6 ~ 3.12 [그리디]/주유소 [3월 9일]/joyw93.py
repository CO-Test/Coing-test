N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

cost = 0

min = price.pop(0)

for i in range(N-1):
    cost += min*distance[i]
    if(min > price[i]): min = price[i]
    
print(cost)