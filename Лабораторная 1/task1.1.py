numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index_none = numbers.index(None)
total = sum(numbers[:index_none]) + sum(numbers[index_none+1:])
numbers[index_none] = total/len(numbers)
print("Измененный список:", numbers)

    # ИЛИ

# index_none = numbers.index(None)
# numbers[index_none] = 0 # не
# numbers[index_none] = sum(numbers)/len(numbers)
# print("Измененный список:", numbers)
