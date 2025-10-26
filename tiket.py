tr=50000
tv=100000

print("================================")
print("list harga tiket bioskop")
print("1. tiket reguler Rp 50.000")
print("2. tiket vip Rp 100.000")
print("================================")
t=int(input("Pilihlah tiket yang anda ingin :"))
b=int(input("berapa tiket yang ingin di pesan :"))
m=(False,True)[input("apakah anda mempunyai member Y/n ") == "Y"]
if t == 1 :
    tk=tr*b
    if m :
        d=tk*20/100
        tt=tk-d
    else :
        d=0
        tt=tk
if t == 2 :
    tk=tv*b
    if m :
        d=tk*20/100
        tt=tk-d
    else :
        d=0
        tt=tk
print("================================")
print("total        : ",tk)
print("Diskon       : ",int(d))
print("Total bayar  : ",int(tt))
print("================================")
u=(False,True)[input("apakah ingin memesan ulang Y/n ") == "Y"]
while u==True : 
    print("================================")
    print("list harga tiket bioskop")
    print("1. tiket reguler Rp 50.000")
    print("2. tiket vip Rp 100.000")
    print("================================")
    t=int(input("Pilihlah tiket yang anda ingin :"))
    b=int(input("berapa tiket yang ingin di pesan :"))
    m=(False,True)[input("apakah anda mempunyai member Y/n ") == "Y"]
    if t == 1 :
        tk=tr*b
    if m :
        d=tk*20/100
        tt=tk-d
    else :
        d=0
        tt=tk
    if t == 2 :
        tk=tv*b
    if m :
        d=tk*20/100
        tt=tk-d
    else :
        d=0
        tt=tk
    print("================================")
    print("total        : ",tk)
    print("Diskon       : ",int(d))
    print("Total bayar  : ",int(tt))
    print("================================")