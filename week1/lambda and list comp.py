print((lambda x: x*2)(10))

print((lambda x, y: x + y)(8, 7))

dirty_data = ['monday ', 'tuesday  ', '  wednesday']
for day in dirty_data:
    print((lambda x: x.strip())(day))

clean_data = []
for day in dirty_data:
    clean_data.append(day.strip())
print(clean_data)

clean_data2 = [day.strip() for day in dirty_data]
print(clean_data2)
