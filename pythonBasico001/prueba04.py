my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []


for number in my_list:
  if number > 0:
    new_list.append(number)

print(new_list)