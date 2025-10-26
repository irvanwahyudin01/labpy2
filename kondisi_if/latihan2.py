a=input("inputkan nilai a= ")
b=input("inputkan nilai b= ")
c=input("inputkan nilai c= ")

a=int(a)
b=int(b)
c=int(c)

if (a>b and a>c and b>c) :
    k=c,b,a
elif (a>b and a>c and c>b) :
    k=b,c,a
elif (b>c and b>a and c>a) :
    k=a,c,b
elif (b>c and b>a and a>c) :
    k=c,a,b
elif (c>b and c>a and b>a) :
    k=a,b,c
elif (c>b and c>a and a>b) :
    k=b,a,c

print("Urutan bilangan ", end=' ')
for t in k :
    print(t,end=' ')
        