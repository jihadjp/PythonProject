#video 21

'''
i =1 #initialization
while i <= 10: #condition
print(i)
i=i+1 #increment
print("End")
'''


sNum = int(input("Enter start number: ")) # 1
eNum = int(input("Enter end number: "))  # 10

sum = 0

while sNum < eNum: # 1 < 10
    sum = sum + sNum  # 0 = 0 + 1
    print(sNum, end=" + ") # 1 + 2 +
    sNum = sNum + 1 # 2

print(sum,  " = ", sNum + sum)