cars = ['bmw','audi','toyota','subaru']
print(len(cars))

travel = ['巴黎','北京','悉尼','新西兰','洛杉矶']
print(travel)
travel = ['巴黎','北京','悉尼','新西兰','洛杉矶']
travel.sort()
print(travel)

print(travel)

travel.sort(reverse=True)
print(travel)

travel.reverse()
print(travel)


travel.reverse()
print(travel) 

nub = len(travel)
print('我有'+str(nub)+'个地方想去！！！')

room = ['亚洲','欧洲','非洲','大洋洲','南美洲','北美洲','南极洲']
print(room[0])
print(room[1].title())
print(room[-1])

room = ['亚洲','欧洲','非洲','大洋洲','南美洲','北美洲','南极洲']
message = "小米今天要去"+ room[4].title() +"了！！！"
print(message)

room[0] = '某某洲'
print(room)

room.append('亚洲')
print(room)

room.insert(1,'第八大洲')
print(room)

del room[0]
print(room)

room.pop()
print('删除的是：'+room.pop())

room.remove('第八大洲')
print(room)

room = ['亚洲','欧洲','非洲','大洋洲','南美洲','北美洲','南极洲']
room.sort()
print(room)

room.sort(reverse=True)
print(room);

print(sorted(room))

room.reverse()
print(room)

room.reverse
print(room)

print(len(room))
