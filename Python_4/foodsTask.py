my_foods = ['pizza','falafel','carrot cake','123','第一']
# 打印前三个切片
print("The first three items in the list are:")
print(my_foods[:3])
# 打印中间三个
print("Three items from the middle of the list are:")
print(my_foods[1:4])
# 打印后上个切片
print("The last three items in the list are:")
my_foods[-3:]

# 我的披萨
My_pizza = ['pizza1','pizza2']
friend_pizza = My_pizza[:]    #复制列表给friend_pizza
My_pizza.append('pizza3')     #添加我的披萨
print(My_pizza)
friend_pizza.append('pizza4') #添加盆友的披萨
print("------------------------------------------------------------------------")
print("My favorite pizzas are:")
for mine in My_pizza[:]:      #使用for循环打印列表
    print(mine)
print("My friend's favorite pizzas are:")
for friend in friend_pizza[:]:
    print(friend)

print("------------------------------------------------------------------------")
foods = ['pizza','falafel','carrot cake']
for food in foods[:]:
    print(food)


