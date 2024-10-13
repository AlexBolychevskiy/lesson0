n = int(input('Ввведите число:'))
a =[]
for i in range(1,20):
    for j in range(1,i):
                 if n % (i+j) == 0:
                   a.append([j]+[i])
c = str(a)
res_c = c.translate({ord(i): None for i in '[,],(,)'})
result = res_c.replace(' ','')
while n >= 3 and n<=20 :
   print(f'{n} -', result)
   break
#n = int(input('Ввведите число:'))
#a = [(j,i)
   #for i in range(1,20)
   #for j in range(1,i) if n % (j + i) == 0]
#c = str(a)
#res_c = c.translate({ord(i): None for i in '[,],(,)'})
#result = res_c.replace(' ','')
#while n >= 3 and n<=20 :
   #print(f'{n} -', result)
   #break
#result = f'{j}+{i}'
#print(result)
# print(f'{j}+{i}')

#def get_matrix(n):
    #for i in range(1,20):
        #for j in range(1,i):
            #if n % (j + i) == 0:
             # row = []
              #row.append([j]+[i])
    #return row
#result1 = get_matrix(6)
#print(result1)