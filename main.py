user_input = input("Введите строку: ")
count = 0
for char in user_input:
    if char == 'е':
        count += 1
print("Количество вхождений буквы 'е':", count)