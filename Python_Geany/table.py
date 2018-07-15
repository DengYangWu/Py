
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)


motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popend_motorcycles = motorcycles.pop()
print(motorcycles)
print(popend_motorcycles)

motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycles I owned was a '+first_owned.title() + '.')

