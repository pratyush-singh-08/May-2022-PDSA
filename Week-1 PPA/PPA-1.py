def Prime(x):
  c=0
  for i in range(1,x+1):
    if x%i==0:
      c+=1
  if c==2:
    return(True)
  else:
    return(False)

def prime_product(m):
  l=[]
  for i in range(1,m+1):
    if Prime(i):
      l.append(i)
  
  for i in l:
    for j in l:
      if i*j==m:
        return(True)
  return(False)



n = int(input())
print(prime_product(n))