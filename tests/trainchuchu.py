#("Результат:", 5 // 3)
#print("Результат:", max(5, 6, 3, 0, 2, -3, 5))
#print("Результат:", abs(-5))
#print("Результат: ", 7, 15, "." , sep="", end="!\n")
#print('second  "\t \\ l\ni\nn\ne"')
#input("введите свой возраст: ")


import pytest


#number = 5 #int
#digit = 4.5456456 #float
#word = "Result: " #string
#boolean = False #bool

#str_num = '5'
#print(word, str(boolean))

#print(word + str(number + int(str_num)))


#num1 = int(input("Введите первое число: "))

#num2 = int(input("Введите второе число: "))

##num1 += 5

#print("result: " , num1 + num2)
#print("result: ", num1 - num2)
#print("result: ", num1 / num2)
#print("result: ",num1 * num2)


#word = "hi" #str
#print(word * 2)

#
#word = True




# user_data = int(input("Введите число: "))
#
# isHappy = True
#
# if  isHappy or user_data == 6:
#     print("user is happy")
# elif user_data == 5:
#     print("Number is 5")
# elif user_data == 7:
#     print("Number is 7")
# else:
#     print("user is unhappy")

# if user_data != 5:
#     print ("Мы на месте")
#     if user_data > 6:
#         print("Number is biggest than 5")



# data = input()
#
# number = 5 if data == "Five" else 0
#
#
# # if data == "Five":
# #     number = 5
# # else:
# #     number = 0
# print(number)


# for i in range(1, 6, 2):
#     print(i)



# count = 0
# word = "Hello world!"
# for i in word:
#     if i == "w":
#         count += 1
#
#         print("count:", count)

# isHasCar = True
#
# while isHasCar:
#      if input("Enter_Date: ") == "Stop":
#          isHasCar = False

# for i in range(1, 11):
#     if i == 5:
#         break
#
#     if i % 2 == 0:
#         continue
#
#     print(i)


# found = None
# for i in "hello":
#     if i == "r":
#         found = True
#         break
# else:
#     found = False
# print(found)


# nums = [5, 6, 7, 8, 9, 1.23412, True, "Hello", [5, 7 [9]]]
#
#
# nums[0] = 50
# nums[6] = False
#
#
# print(nums[-2][0])

# numbers = [5, 2, 7]
# # numbers[3] = 100
# numbers.append(100)
# numbers.insert(1, True)
#
# b = [5, 6, 8]
# numbers.extend(b)
# #numbers.reverse()
# numbers.sort()
#
# # numbers.pop()
# numbers.pop()
# numbers.remove(6)
#
# # numbers.clear()
#
# print(len(numbers))
#
# print(numbers)

# nums = [5, 2, 7, "50", False ]
#
# for el in nums:
#     el *= 2
#     print(el)


# n = int(input("Enter length: "))
#
# user_list = []
#
# i = 0
#
# while i < n:
#     string = "Enter element #" + str(i + 1) + ": "
#     user_list.append(input(string))
#     i += 1
# print(user_list)


# def test_func(word):
#     print(word, end = "")
#     print( "!" )
#
#
# test_func("Hi")
# test_func(5)
# test_func(5.6)




# nums1 = [5, 6, 7, 8]
#
# min = nums1[0]
# for el in nums1:
#     if el < min:
#         min = el
#
# print(min)
#
# nums2 = [5.4, 7.2, 2.3, 2.1, 4.2]
#
# min2 = nums2[0]
# for el in nums2:
#     if el < min2:
#         min2 = el
#
# print(min)



# def minimal(l):
#     min_number = l[0]
#     for el in l:
#         if el < min_number:
#             min_number = el
#
#     return min_number
#
#
#
# nums1 = [5, 6, 7, 8]
# min1 = minimal(nums1)
#
# nums2 = [5.4, 7.2, 1.9, 2.3, 2.1, 4.2]
# min2 = minimal(nums2)
#
# if min1 < min2:
#     print(min1)
# else:
#     print(min2)


# func = lambda x, y: x * y
# res = func(5,2)
# print(res)

# try:
#     x = int(input("Введите число: "))
#     x += 5
#     print(x)
# except  ValueError:
#     print("Введите лучше число!")


# x = 0
# while x == 0:
#     try:
#         x = int(input("Введите число: "))
#         x += 5
#         print(x)
#     except  ValueError:
#         print("Введите лучше число!")

# try:
#     x = 5 / 0
#     x = int(input())
# except ZeroDivisionError:
#     print("Деление на ноль нельзя!")
# except ValueError:
#     print("Вы ввели что то не так")
# else:
#     print("else")
# finally:
#     print("Finally")


class Cat:
    name = None
    age = None
    isHappy = None


    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy
    def get_data(self):
        print(self.name, "age:", self.age, ". isHappy:", self.isHappy)


cat1 = Cat()
cat1.set_data("Barsik",1.5,True )


cat2 = Cat()
cat2.set_data("Down", 2, False)

cat1.get_data()
cat2.get_data()

print(cat1.name)
print(cat2.name)









