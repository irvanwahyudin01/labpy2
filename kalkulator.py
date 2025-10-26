a=int(input("inputkan bilangan pertama : "))
b=int(input("inputkan bilangan kedua   : "))

print("list  operasi")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. bagi")
print("===========================")
c=input("pilih operasi yang akan dilakukan : ")

if c == "1" :
	h=a+b
elif c == "2" :
	h=a-b
elif c == "3" :
	h=a*b
elif c == "4" :
	h=a/b
elif c == "" :
	h="Anda belum memilih operasi"
else :
	h="Anda belum memilih operasi"
print ("hasil dari operasi adalah : ",h)
