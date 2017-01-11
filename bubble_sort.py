listA=[3,1,4,5,2]

for i in range(len(listA)):
  for e in range(len(listA)-1):
    if listA[e] > listA[e+1]:
      listA[e],listA[e+1] = listA[e+1],listA[e]
      print(listA)
