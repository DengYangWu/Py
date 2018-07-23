for value in range(1,5):
	print(value)
number = list(range(1,6))
print(number)
number = list(range(2,11,2))	#打印偶数
print(number)

squares = []	#**表示乘方
for value in range(1,11):
	square = value**2			
	squares.append(square)
print(squares)

squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

di = [1,2,3,4,5,6,7,8,9,0]
print(min(di))
di = range(1,20)
print(min(di))
print(max(di))
print(sum(di))

squares = [value**2 for value in range(1,11)]	#列表解析
print(squares)

num = range(1,21)
for number in num:
	print(number)

bignumber = range(1,1000001)
print(max(bignumber))
print(sum(bignumber))

oddNumber = range(3,20,3)
for odd in oddNumber:
	print(odd)


tab = []
table = list(range(3,30,3))  #只能被3整除的数 打印出来
for tab1 in table:
	tab.append(tab1)
print(tab)

cube = range(1,10)
for cu in cube:
	print(cu**3)   #求立方数

analysis = [value**3 for value in range(1,11)]
print(analysis)
