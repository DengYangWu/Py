# 检查两个字符串是否相等
num = '火车'
if num == '高铁':
    print(True)
else:
    print(False)

print("================================================^_^")
Vue = 'VoV'
if Vue.lower() == 'vov':   # 不区分大小写
    print(True)
else:
    print(False)

print("================================================^_^")
if 8<9:
    print(True)
else:
    print(False)

print("================================================^_^")
if 8>0 and 7<10:
    print(True)
else:
    print(False)
print("================================================^_^")

vue = [1,2,3]
table=str(vue)
for num in vue:
    if num == 2:
        print("我已经找到你想要的数字：",num)

print("================================================^_^")
num = ['赵六','崔七']
for number in num:
    if number != '赵六':
        print("我的名字叫：",number)
