# 元组
food = ('Apple','orange','banana','beef','wine')
for foods in food:      #用循环打印元组里的元素
    print(foods)

# food[0] = 'pork'
# print(food)        #核实元组不能被修改

print("================================================^_^")
foods = ('hot','grape')
FOOD = foods+food
for FOODS in FOOD:
    print(FOODS)

