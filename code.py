T=int(input("Enter the number : "))
d=T// 86400
h=(T % 86400) // 3600
mn=(T % 3600) // 60
se= (T%3600)%60
print(d,"d :",h,"h :",mn,"mn :",se,"sec")