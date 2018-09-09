
# 操作列表
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)

print("------------------------------------------")

margician1 = ['alice','david','carolina']
for magician1 in margician1:

    print(magician1.title()+",that was a great trick!")
    print("I can't wait to see your next trick," + magician1.title() + "\n")
    print("Thank you everyone,that was a great magic show!")

print("------------------------------------------")

for value in range(1,5):
    print(value)

print("-------------------------------------------")

number = list(range(1,10))
print(number)

print("-------------------------------------------")

even_numbers = list(range(2,20,2))
print(even_numbers)

print("--------------------------------------------")

# 列表解析
squares = [value**2 for value in range(1,11)]
print(squares)

#动手
print("--------------------------------------------")

for num in range(1,21):
    print(num)
print("--------------------------------------------")
bignum = [value for value in range(1,1000001)]
print(min(bignum))
print(max(bignum))
print(sum(bignum))

# 打印奇数
for oddnumber in range(1,21):
    if(oddnumber%2!=0):
        print(oddnumber)
print("--------------------------------------------")
# 能被3整除
for oddnumber2 in range(3,30,3):
    print(oddnumber2)
# 立方
for ten in range(1,10):
    print(ten**3)

#立方解析
analysis = [ten**3 for ten in range(1,11)]
print(analysis)



