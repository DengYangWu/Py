cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("================================================^_^")
car = 'bmw'
car == 'bmw'

car = 'audi'
car == 'bmw'

car = 'Audi'
print(car.lower())
car.lower() == 'audi'

print("================================================^_^")
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

print("================================================^_^")
requested_topping = ['mushrooms','onions','pineapple']
if 'mushrooms' in requested_topping:    #in的作用是 判断查询列表是否包含这个值
    print(True)
else:
    print(False)

print("================================================^_^")
banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:     #not in表示不包含这个值
    print(user.title() + ",you can post a response if you wish.")

game_action = True
can_edit = False

