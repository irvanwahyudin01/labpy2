a=input("inputkan nilai a= ")
b=input("inputkan nilai b= ")
c=input("inputkan nilai c= ")
d=input("inputkan nilai D= ")

a=int(a)
b=int(b)
c=int(c)
d=int(d)

if (a>b and a>c and a>d) :
    print("nilai a adalah terbesar")
elif (b>c and b>c and b>d) :
    print("nilai b adalah terbesar")
elif (c>a and c>b and c>d) :
    print("nilai c adalah terbesar")
elif (d>a and d>b and d>c) :
    print("nilai d adalah terbesar")
else :
    print("ketiga nilai sama")