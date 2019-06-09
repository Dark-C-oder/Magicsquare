given=[]
for i in range(0,3):
    given.append(list(map(int,input().split( ))))

square = [[[8,1,6], [3,5,7], [4,9,2]], [[6,1,8], [7,5,3], [2,9,4]], [[4,9,2], [3,5,7], [8,1,6]], [[2,9,4], [7,5,3], [6,1,8]], [[8,3,4], [1,5,9], [6,7,2]], [[4,3,8], [9,5,1], [2,7,6]], [[6,7,2], [1,5,9], [8,3,4]], [[2,7,6], [9,5,1], [4,3,8]]]
count = 0
counter = []
for i in range(0,8):
    for j in range(0,3):
        for k in range(0,3):
            count += abs(square[i][j][k] - given[j][k])
    counter.append(count)
    count = 0

print(min(counter))