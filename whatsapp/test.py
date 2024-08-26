numbers = []
with open('./client/numbers.txt', 'r') as file:
    print(file.readlines())
    # for num in file.readlines():
    #     print(num)
    #     numbers.append(num.rsplit())

# numbers.append('256879')
# numbers.append('256654')
# numbers.append('256132')
# numbers.append('256417')

print(numbers)

