t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(input().split())
    new_m = []
    print(matrix)
    for i in range(k):
        for j in range(k):
            print(i,j)
            a = matrix[i][j]
            new_m.append(a)
            
    print(new_m)
        
        