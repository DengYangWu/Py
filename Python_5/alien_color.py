# 满足条件
alien_color = ['green','yellow','red']
if 'green' in alien_color:
    print("玩家获得了5个点")
else:
    print("...")

print("================================================^_^")
# 不满足条件
alien_color = ['red','blue','orange']
if 'green' in alien_color:
    print("玩家获得了5个点")
else:
    print("...")

print("================================================^_^")

# if-else结构1
alien = 'green'
if alien == 'red':
    print("玩家获得10个点")
if alien == 'green':
    print("玩家获得5个点")
if alien == 'green':
    print("玩家获得5个点")
print("！@#￥%……&*（）")
# if-else结构2
alien = 'green'
if alien == 'red':
    print("玩家获得10个点")
elif alien == 'green':
    print("玩家获得5个点")
elif alien == 'green':
    print("玩家获得5个点")

print("================================================^_^")

saucer_man = 'yellow'
if 'green' == saucer_man:
    print("玩家获得5个点")
elif 'yellow' == saucer_man:
    print("玩家获得10个点")
else:
    print("玩家获得15个点")

print("================================================^_^")
# 人生的不同阶段
age = input("请输入你的年龄：")
print(age)
if age < 2:
    print("He was a baby")
elif age >= 2 and age<4:
    print("He was a big-baby")
elif age >= 4 and age<13:
    print("He was a child")
elif age >= 13 and age<20:
    print("He was a puber")
elif age >= 20 and age<65:
    print("He was a adult")
elif age >=65:
    print("old man")
else:
    print("old man")