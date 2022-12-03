'''x=int(input())
y=int(input())
z=int(input())
a=[[b,c,d] for b in range(x+1) for c in range(y+1)
for d in range(z+1)
   if (x+y+z !=3)]
print(a)'''

d1=input( )
d2=input( )
dict3={d1[i] : d2[i] for i in range(len(d1))}
print(dict3)
