numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
m=0
sum=0
for i in range (0, len(numbers)):
    if numbers[i] ==None:
        m=i
        i=i+1
    else:
        sum=sum+numbers[i]

Sr=sum/(len(numbers))
numbers[m]=Sr

print("Измененный список:", numbers)
