name = ['曹操','李白','拿破仑','毛泽东']
print(name.pop(0)+ ':\t拒绝来共进早餐！')
name.append('小刘')
print(name)

print('我找来了更大的餐桌~')
name.insert(0,'小星')
name.insert(1,'小秀')
name.insert(3,'小熊')
name.append('晓晓')
print(name)
print('得知餐桌无法及时送到,只能容纳2个人了~')
print('抱歉,这次无法邀请\t'+name.pop(1))
print('抱歉,这次无法邀请\t'+name.pop(2))
print('抱歉,这次无法邀请\t'+name.pop(3))
print('抱歉,这次无法邀请\t'+name.pop(4))
print('抱歉,这次无法邀请\t'+name.pop(1))
print('抱歉,这次无法邀请\t'+name.pop(2))
print(name)
del name[0]
del name[0]
print(name)
print('本次邀请以结束')
