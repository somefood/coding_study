n, m = map(int, input().strip().split(' '))

# for i in range(m):
#     for j in range(n):
#         print('*', end='')
#     print()

answer = ('*'*n +'\n') * m
print(answer)