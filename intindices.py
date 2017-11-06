def func(arr):
  I = 0
  J = 0
  K = 0
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      for k in range(len(arr[0][0])):
        arr[i][j][k] = (i * 100) + (j * 10) + k
  print(arr[0][0][3]) 
  print(arr[9][3][3]) 
i,j,k = 10, 10, 10
array = [[[0 for x in range(i)] for y in range(j)] for z in range(k)]
func(array)
