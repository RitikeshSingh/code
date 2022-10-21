x=[[1, 4, 5],[-5, 8, 9]]
y=[[1,2,3],[4,5,6]]
for i, j in zip(x, y):
    for a,b in zip(i,j):
        print (a+b)

    