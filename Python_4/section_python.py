# 切片
players = ['charles','martina','michael','florence','eli']
print(players[0:3])

players = ['charles','martina','michael','florence','eli']
print(players[1:4])

players = ['charles','martina','michael','florence','eli']
print(players[2:])

players = ['charles','martina','michael','florence','eli']
print(players[-3:])

players = ['charles','martina','michael','florence','eli']
print("Here are the first three pplayers on my team:")
for player in players[:3]:
    print(player.title())
