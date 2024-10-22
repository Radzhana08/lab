disk_ob=1.44
list=100
strc=50
symbols=25
o_symbols=4

book=list*strc*symbols*o_symbols
disk=disk_ob*1024*1024
books=disk/book

print("Количество книг, помещающихся на дискету:", int(books))
